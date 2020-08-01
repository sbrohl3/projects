## Kionix Test program
## 03.09.2020
#######################

from smbus2 import SMBus
import RPi.GPIO as GPIO
import time
#from threading import timer

## Define bus address
slv_add = int("0x1f", 16)

## Define interrupt GPIO
INT_GPIO  = 12

## Define registers
INT_REL    = int("0x17", 16)
CNTL1      = int("0x18", 16)
CNTL3      = int("0x1a", 16)
ODCNTL     = int("0x1b", 16)
INC1       = int("0x1c", 16)
INC2       = int("0x1d", 16)
INC3       = int("0x1e", 16)
INC4       = int("0x1f", 16)
TDTRC      = int("0x24", 16)
TDTC       = int("0x25", 16)
TTH        = int("0x26", 16)
TTL        = int("0x27", 16)
FTD        = int("0x28", 16)
STD        = int("0x29", 16)
TLT        = int("0x2a", 16)
TWS        = int("0x2b", 16)
BUF_CNTL1  = int("0x3a", 16)
BUF_CNTL2  = int("0x3b", 16)
BUF_READ   = int("0x3f", 16)
BUF_STAT_1 = int("0x3c", 16)
BUF_STAT_2 = int("0x3d", 16)
BUF_CLEAR  = int("0x3e", 16)
ATH        = int("0x30", 16)
WUFC       = int("0x23", 16)

## Define registers & messages for going into ULPM
tap_values = [{"register" : CNTL1,     "data" : int("01001100", 2)},
               {"register" : CNTL3,     "data" : int("00011000", 2)},
               {"register" : ODCNTL,    "data" : int("00000101", 2)},
               {"register" : INC1,      "data" : int("00100000", 2)},
               {"register" : INC3,      "data" : int("00111111", 2)}, 
               {"register" : INC4,      "data" : int("00000100", 2)},
               {"register" : TDTRC,     "data" : int("00000011", 2)},
               {"register" : TDTC,      "data" : int("01111000", 2)},
               {"register" : TTH,       "data" : int("11111111", 2)},
               {"register" : FTD,       "data" : int("11111010", 2)},
               {"register" : STD,       "data" : int("00100100", 2)},
               {"register" : TLT,       "data" : int("00101000", 2)},
               {"register" : TWS,       "data" : int("10100000", 2)},
               {"register" : BUF_CNTL1, "data" : int("01011110", 2)}, # 01100000 GOOD
               {"register" : BUF_CNTL2, "data" : int("11001110", 2)}, # 11001110 GOOD
               {"register" : CNTL1,     "data" : int("11001100", 2)}]

## Define register values for Motion detection
motion_values = [{"register" : CNTL1,     "data" : int("01000010", 2)},
               {"register" : CNTL3,     "data" : int("00000110", 2)},
               {"register" : INC2,      "data" : int("01111111", 2)},
               {"register" : WUFC,      "data" : int("00000101", 2)},
               {"register" : ATH,      "data" : int("00000010", 2)},
               {"register" : INC1,      "data" : int("00110000", 2)},
               {"register" : INC4,      "data" : int("00000010", 2)},
               {"register" : BUF_CNTL1, "data" : int("01011110", 2)},
               {"register" : BUF_CNTL2, "data" : int("11001110", 2)},
               {"register" : CNTL1,     "data" : int("11000010", 2)}]

combine_values = [{"register" : CNTL1,  "data" : int("01001110", 2)},
               {"register" : CNTL3,     "data" : int("00011111", 2)},
               {"register" : ODCNTL,    "data" : int("00000101", 2)},
               {"register" : INC1,      "data" : int("00100000", 2)},
               {"register" : INC3,      "data" : int("00111111", 2)}, 
               {"register" : INC4,      "data" : int("00000100", 2)},
               {"register" : INC2,      "data" : int("00111111", 2)},
               {"register" : WUFC,      "data" : int("00000101", 2)},
               {"register" : ATH,       "data" : int("00000010", 2)},
               {"register" : TDTRC,     "data" : int("00000011", 2)},
               {"register" : TDTC,      "data" : int("01111000", 2)},
               {"register" : TTH,       "data" : int("11111111", 2)},
               {"register" : FTD,       "data" : int("11111010", 2)},
               {"register" : STD,       "data" : int("00100100", 2)},
               {"register" : TLT,       "data" : int("00101000", 2)},
               {"register" : TWS,       "data" : int("10100000", 2)},
               {"register" : BUF_CNTL1, "data" : int("01011110", 2)}, # 01100000 GOOD
               {"register" : BUF_CNTL2, "data" : int("11001110", 2)}, # 11001110 GOOD
               {"register" : CNTL1,     "data" : int("11001110", 2)}]


## Recommended SMP_TH[9:0] value for 400Hz Kionix & 400Hz Directional-Tap:
## At least 00000011 01011110
## Defined in BUF_CNTL1 & BUF_CNTL2 (see specifications for more details)
## http://kionixfs.kionix.com/en/datasheet/KX122-1037-Specifications-Rev-6.0.pdf


## Define registers & messages for going into Normal Operations Mode (Not tested)
norm_values = [{"register" : CNTL1,     "data" : int("01010000", 2)},
               {"register" : ODCNTL,    "data" : int("00000111", 2)},
               {"register" : BUF_CNTL2, "data" : int("00000000", 2)},
               {"register" : CNTL1,     "data" : int("11010000", 2)}]


def read_reg(reg):
    ## Read data from register
    try:
        return bus.read_byte_data(slv_add, reg)
    except:
        print("\nERROR: could not read register. Aborting ...\n")
        exit(0)


def write_reg(reg, data):
    ## Write data to register
    try:
        bus.write_byte_data(slv_add, reg, data)
        #print("Wrote data", hex(data), "to register", hex(reg))
    except:
        print("\nERROR: could not write to register. Aborting ...\n")
        exit(0)

def check_buf_trig():
    ## Read data from status registers
    buf_stat_2 = read_reg(BUF_STAT_2)
    
    ## Check if trigger has occurred
    if (buf_stat_2 & int("10000000", 2)) == int("10000000", 2):
        print("\nTrigger has occurred!\n")
    else:
        print("\nTrigger has NOT occurred!\n")


def get_buf_size():
    buf_stat_1 = read_reg(BUF_STAT_1)
    buf_stat_2 = read_reg(BUF_STAT_2)
    
    return buf_stat_1 + ((buf_stat_2 & int("00000111", 2)) << 8)


def read_buf():
    ## Read a 16-bit value from the 2k buffer
    lsb = read_reg(BUF_READ)
    msb = read_reg(BUF_READ) << 8
    
    val = lsb + msb
    
    if val >= 32768:
        val -= 65535
    
    return val

def ulpm(values):
    print("\nConfiguring Kionix for ULPM\n")
    for item in values:
        write_reg(item["register"], item["data"])


def norm():
    print("\n\nConfiguring Kionix for Normal Operations Mode\n")
    for item in norm_values:
        write_reg(int(item["register"], 16), item["data"])


def int_rel():
    read_reg(INT_REL)


def buf_clear():
    write_reg(BUF_CLEAR, 0)


def GPIO_setup():
    ## Clean-up GPIO pins
    GPIO.cleanup
    ## Set GPIO Mode (BOARD or BCM)
    GPIO.setmode(GPIO.BCM)
    ## Set INT1 to GPIO pin
    GPIO.setup(INT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
def relInt(NO_INTERRUPT):
    
    ## Release interrupt
    print("\nReleasing interrupt ...")
    reset = False
    while not reset:
        int_rel()
        if GPIO.input(INT_GPIO) == NO_INTERRUPT:
            print("Done.")
            reset = True
        else:
            print("error: trying again.")
            reset = False
            
    return(reset)
    
def write2File(mode):

    if mode.lower() == "t":
        with open("wakeup_buf_tap_" + str(time.strftime(str("%H") + str("%M") + str("%S"))) + ".csv", "w+")  as f:    
            for i in range(1,2048, 6):
                x = read_buf()
                y = read_buf()
                z = read_buf()
            
                #print(x,y,z)
                f.write(str(x) + "," + str(y) + "," + str(z) + "\n")

    elif mode.lower() == "m":
        with open("wakeup_buf_motion_" + str(time.strftime(str("%H") + str("%M") + str("%S"))) + ".csv", "w+") as f:    
            for i in range(1,2048, 6):
                x = read_buf()
                y = read_buf()
                z = read_buf()
            
                #print(x,y,z)
                f.write(str(x) + "," + str(y) + "," + str(z) + "\n")
        
    elif mode.lower() == "c":
        with open("wakeup_buf_combined_" + str(time.strftime(str("%H") + str("%M") + str("%S"))) + ".csv", "w+")  as f:    
            for i in range(1,2048, 6):
                x = read_buf()
                y = read_buf()
                z = read_buf()
            
                #print(x,y,z)
                f.write(str(x) + "," + str(y) + "," + str(z) + "\n")
                
def configMode():              
    ## Set Kionix to ULPM Mode for tap or motion mode or combined
    config = False
    while not config:
        
        config_res = input("Do you want to set the Kionix for (t)ap detection or (m)otion detection or (c)ombined event detection: ")
        
        if config_res.lower() == "t":
            ulpm(tap_values)
            config = True

        elif config_res.lower() == "m":
            ulpm(motion_values)
            config = True

        elif config_res.lower() == "c":
            ulpm(combine_values)
            config = True

        else:
            print("\nInvalid input! Please enter either \"t\" or \"m\" or \"c\" to continue.\n")
            config = False
        
    if config_res.lower() == "m":
        NO_INTERRUPT = 0
        return([NO_INTERRUPT, config_res])

    elif config_res.lower() == "t":
        NO_INTERRUPT = 1
        return([NO_INTERRUPT, config_res])


    elif config_res.lower() == "c":
        NO_INTERRUPT = 1
        return([NO_INTERRUPT, config_res])
    
def initRun():
    
    ## Wait for Interrupt
    config = configMode()
    interrupt(config[0])
    reset = relInt(config[0])
    return(reset)
    
    
def eventTestMain():
    
    ## Check buffer status & display contents
    time.sleep(2)
    check_buf_trig()

    buf_size = get_buf_size()
    while buf_size < (340 * 6) - 6:
        print("Waiting on buffer...", buf_size)
        time.sleep(0.1)
        buf_size = get_buf_size()

    print("\nWriting 2k buffer data to file...\n")
    mode = config[1] 
    write2File(mode)
    
    return(reset)
    
    
def interrupt(NO_INTERRUPT):

    ## Wait for interrupts
    interrupt_signal = NO_INTERRUPT

    print("\nAwaiting interrupt ...")
    while interrupt_signal == NO_INTERRUPT:
        time.sleep(0.05)
        interrupt_signal = GPIO.input(INT_GPIO)
        
    print("Interrupt detected!!")


## Set up GPIO pins
GPIO_setup()

## Call SMBus
bus = SMBus(1)

## Release any active interrupts
int_rel()

## Clear buffer
buf_clear()

reset = initRun()

while True:
    
    ## Set Kionix to Normal Operations Mode
    if reset:
        norm()
        print("\nMaintaining normal mode operation for 5 minutes then returning to sleep mode...\n")
