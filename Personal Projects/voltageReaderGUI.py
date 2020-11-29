import tkinter
import time
from voltage_read import *

'''
A simple Tkinter program for evaluating the NI USB6001 DAQ

NOTE: You must install the python library, nidaqmx to use this program. --> python3 -m pip install nidaqmx
      
      Install this software package in Windows as well for proper device drivers: https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html#348669

Created 11/28/2020
'''

def readValue():

    ''' A function for reading voltage values from the voltage_read function and displaying them in the GUI
        Input - readVoltage 
        returns - ON/OFF, 0-10v, True/False
    '''

    status = readVoltage()
    window.configure(text = "STATUS: " + str(status[0]) + "\n" + str(status[1]) + "v " + str(status[2]))

## Setup initial Label
root = tkinter.Tk()
root.title("NI USB6001 DAQ READER")
window = tkinter.Label(root, text = "")

while True:
    try:
        ## Read Voltages and keep refreshing the GUI with the latest input
        while True:
            window.pack()
            window.configure(text=readValue())
            root.update()
        root.mainloop()
    except:
        flag = True
        ## If the DAQ is not connected via USB, warn the user
        while flag:
            window.pack()
            window.configure(text="ERROR READING ANALOG INPUT 0.\nPlease ensure your DAQ's USB cable is plugged in correctly and try again.")
            try:
                ## Attempt to read voltage input to determine if DAQ is operational
                if readValue():
                    flag = False
            except:
                pass
            root.update()
        root.mainloop()
