import nidaqmx

def readVoltage():

    ''' A function for reading analog voltage from NI USB6001 DAQ via the nidaqmx Python library
        Inputs -  
        Outputs - Return True/False, voltage, and string ON/OFF based on whether DAQ detects voltage or not
        Created - 11/27/2020
    '''

    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        voltage = round(task.read(), 1)
        if voltage >= 1: 
            return("ON", voltage, True)
        elif voltage < 1:
            return("OFF", voltage, False)
