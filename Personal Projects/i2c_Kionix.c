/**
 * Kionix Accelerometer ULPM Test Program
 * ----------------------------------------------------------------------------
 * Program modified by Steven Brohl
 * Copyright (C) Sierra Wireless, Inc. Use of this work is subject to license.
 *-----------------------------------------------------------------------------
 */


#include "legato.h"
#include "interfaces.h"
#include "i2c-dev-user.h"

// Bus Number
const int i2cBus = 8;

// Slave Address
unsigned char i2cAddr = 0x1f;

// Define Registers
unsigned char INT_REL    = 0x17;
unsigned char CNTL1      = 0x18;
unsigned char CNTL3      = 0x1a;
unsigned char ODCNTL     = 0x1b;
unsigned char INC1       = 0x1c;
unsigned char INC2       = 0x1d;
unsigned char INC3       = 0x1e;
unsigned char INC4       = 0x1f;
unsigned char TDTRC      = 0x24;
unsigned char TDTC       = 0x25;
unsigned char TTH        = 0x26;
unsigned char TTL        = 0x27;
unsigned char FTD        = 0x28;
unsigned char STD        = 0x29;
unsigned char TLT        = 0x2a;
unsigned char TWS        = 0x2b;
unsigned char BUF_CNTL1  = 0x3a;
unsigned char BUF_CNTL2  = 0x3b;
unsigned char BUF_READ   = 0x3f;
unsigned char BUF_STAT_1 = 0x3c;
unsigned char BUF_STAT_2 = 0x3d;
unsigned char BUF_CLEAR  = 0x3e;
unsigned char ATH        = 0x30;
unsigned char WUFC       = 0x23;

static int I2cAccessBusAddr(uint8_t i2cBus, uint8_t i2cAddr)
{
    const size_t filenameSize = 32;
    char filename[filenameSize];

    snprintf(filename, filenameSize, "/dev/i2c/%d", i2cBus);

    LE_DEBUG("Opening I2C bus: '%s'", filename);
    int fd = open(filename, O_RDWR);
    if (fd < 0 && (errno == ENOENT || errno == ENOTDIR))
    {
        snprintf(filename, filenameSize, "/dev/i2c-%d", i2cBus);
        LE_DEBUG("Opening I2C bus: '%s'", filename);
        fd = open(filename, O_RDWR);
    }

    if (fd < 0)
    {
        if (errno == ENOENT)
        {
            LE_DEBUG(
                "Could not open file /dev/i2c-%d or /dev/i2c/%d: %s", i2cBus, i2cBus, strerror(ENOENT));
        }
        else
        {
            LE_INFO("Could not open file %s': %s", filename, strerror(errno));
        }

        return LE_FAULT;
    }

    if (ioctl(fd, I2C_SLAVE_FORCE, i2cAddr) < 0)
    {
        LE_INFO("Could not set address to 0x%02x: %s", i2cAddr, strerror(errno));
        close(fd);
        return LE_FAULT;
    }

    return fd;
}

static le_result_t SmbusReadReg(uint8_t i2cBus, uint8_t i2cAddr, uint8_t  reg, uint8_t *data)
{
    int i2cFd = I2cAccessBusAddr(i2cBus, i2cAddr);
    if (i2cFd < 0)
    {
        LE_DEBUG("failed to open i2c bus %d for access to address %d", i2cBus, i2cAddr);
        return  LE_FAULT;
    }

    le_result_t result;

    const int readResult = i2c_smbus_read_byte_data(i2cFd, reg);

    if (readResult < 0)
    {
        LE_DEBUG("smbus read failed with error %d", readResult);
        result = LE_FAULT;
    }
    else
    {
        *data = readResult;
        LE_DEBUG("SMBUS READ addr=0x%x, reg=0x%x, data=0x%x", i2cAddr, reg, *data);
        result = LE_OK;
    }

    close(i2cFd);

    return result;
}

static le_result_t SmbusWriteReg(uint8_t i2cBus, uint8_t i2cAddr, uint8_t reg, uint8_t data) 
{
    int i2cFd = I2cAccessBusAddr(i2cBus, i2cAddr);

    if (i2cFd == LE_FAULT)
    {
        LE_ERROR("failed to open i2c bus %d for access to address %d", i2cBus, i2cAddr);
        return LE_FAULT ;
    }

    le_result_t result;

    const int writeResult = i2c_smbus_write_byte_data(i2cFd, reg, data);
    if (writeResult < 0)
    {
        LE_ERROR("smbus write failed with error %d", writeResult);
        result = LE_FAULT;
    }
    else
    {
        LE_DEBUG("SMBUS Write addr 0x%x, reg=0x%x, data=0x%x", i2cAddr, reg, data);
        result = LE_OK;
    }

    close(i2cFd);

    return result;

}

static void normalConfig(void)
{
    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b01010000);
    SmbusWriteReg(i2cBus, i2cAddr, ODCNTL, 0b00000111);
    SmbusWriteReg(i2cBus, i2cAddr, BUF_CNTL2, 0b00000000);
    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b11010000);
}

static void ulpmCombinedConfig(void) 
{
    // read and write register values to configure the Kionix to function with device ULPM for combined event wakeup
    uint8_t registerReading;

    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b01001110);
    SmbusWriteReg(i2cBus, i2cAddr, CNTL3, 0b00011111);
    SmbusWriteReg(i2cBus, i2cAddr, ODCNTL, 0b00000101);
    SmbusWriteReg(i2cBus, i2cAddr, INC1, 0b00100000);
    SmbusWriteReg(i2cBus, i2cAddr, INC3, 0b00111111);
    SmbusWriteReg(i2cBus, i2cAddr, INC4, 0b00000100);
    SmbusWriteReg(i2cBus, i2cAddr, INC2, 0b00111111);
    SmbusWriteReg(i2cBus, i2cAddr, WUFC, 0b00000101);
    SmbusWriteReg(i2cBus, i2cAddr, ATH, 0b00000010);
    SmbusWriteReg(i2cBus, i2cAddr, TDTRC, 0b00000011);
    SmbusWriteReg(i2cBus, i2cAddr, TTH, 0b01111000);
    SmbusWriteReg(i2cBus, i2cAddr, FTD, 0b11111111);
    SmbusWriteReg(i2cBus, i2cAddr, STD, 0b11111010);
    SmbusWriteReg(i2cBus, i2cAddr, TLT, 0b00100100);
    SmbusWriteReg(i2cBus, i2cAddr, TWS, 0b00101000);
    SmbusWriteReg(i2cBus, i2cAddr, BUFF_CNTL1, 0b01011110);   
    SmbusWriteReg(i2cBus, i2cAddr, BUFF_CNTL2, 0b11001110);
    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b11001110);    
    
    //SmbusReadReg(i2cBus, i2cAddr, 0x18, &registerReading);
    //LE_INFO("Register Value is: %d", registerReading);
}

static void ulpmMotionConfig(void) 
{
    // read and write register values to configure the Kionix to function with device ULPM Motion Wakeup
    uint8_t registerReading;

    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b01000010);
    SmbusWriteReg(i2cBus, i2cAddr, CNTL3, 0b00000110);
    SmbusWriteReg(i2cBus, i2cAddr, INC2, 0b01111111);
    SmbusWriteReg(i2cBus, i2cAddr, WUFC, 0b00000101);
    SmbusWriteReg(i2cBus, i2cAddr, ATH, 0b00000010);
    SmbusWriteReg(i2cBus, i2cAddr, INC1, 0b00110000);
    SmbusWriteReg(i2cBus, i2cAddr, INC4, 0b00000010);
    SmbusWriteReg(i2cBus, i2cAddr, BUF_CNTL1, 0b01011110);
    SmbusWriteReg(i2cBus, i2cAddr, BUF_CNTL2, 0b11001110);
    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b11000010);
    
    //SmbusReadReg(i2cBus, i2cAddr, 0x18, &registerReading);
    //LE_INFO("Register Value is: %d", registerReading);
}

static void ulpmTapConfig(void) 
{
    // read and write register values to configure the Kionix to function with device ULPM Tap Wakeup
    uint8_t registerReading;

    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b01001100);
    SmbusWriteReg(i2cBus, i2cAddr, CNTL3, 0b00011000);
    SmbusWriteReg(i2cBus, i2cAddr, ODCNTL, 0b00000101);
    SmbusWriteReg(i2cBus, i2cAddr, INC1, 0b00100000);
    SmbusWriteReg(i2cBus, i2cAddr, INC3, 0b00111111);
    SmbusWriteReg(i2cBus, i2cAddr, INC4, 0b00000100);
    SmbusWriteReg(i2cBus, i2cAddr, TDTRC, 0b00000011);
    SmbusWriteReg(i2cBus, i2cAddr, TDTC, 0b01111000);
    SmbusWriteReg(i2cBus, i2cAddr, TTH, 0b11111111);
    SmbusWriteReg(i2cBus, i2cAddr, FTD, 0b11111010);
    SmbusWriteReg(i2cBus, i2cAddr, STD, 0b00100100);
    SmbusWriteReg(i2cBus, i2cAddr, TLT, 0b00101000);
    SmbusWriteReg(i2cBus, i2cAddr, TWS, 0b10100000);
    SmbusWriteReg(i2cBus, i2cAddr, BUF_CNTL1, 0b01011110);
    SmbusWriteReg(i2cBus, i2cAddr, BUF_CNTL2, 0b11001110);
    SmbusWriteReg(i2cBus, i2cAddr, CNTL1, 0b11001100);
    
    //SmbusReadReg(i2cBus, i2cAddr, 0x18, &registerReading);
    //LE_INFO("Register Value is: %d", registerReading);
}



COMPONENT_INIT
{
    LE_INFO("!!!!!!! -- Reading and Writing to Kionix has started -- !!!!!!!");
    ulpmTapConfig();
}
