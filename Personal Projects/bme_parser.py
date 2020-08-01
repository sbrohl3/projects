## BME680 Json Parser
## Using the BSEC Driver and Code provide by Alexh-name on Github I was able to  extract data from the BME680 in a Json format
## 
## Developed by Steven Brohl
## 07.30.2020
## https://github.com/alexh-name/bsec_bme680_linux 
##
#################################################################################################################################

import time
import datetime as datetime
import json
import csv
from matplotlib import pyplot as plt
import sys
import os


time = datetime.datetime.now()
time_fmt = time.strftime("%d%m%y_%H%M%S")

co2 = []
times = []
program_run = True
while program_run:
    try:
        print("Parsing data file, please wait.")

        pdir = str(".")
        
        for filename in os.listdir(str(pdir)): 
            if filename.endswith(".json"):
                print("Writing data.json file to csv. Please wait!")
                with open(str(pdir) + "/" + str(filename), "r+") as data:
                    bme_data = json.load(data)

                    with open("parsed_data_" + str(time_fmt) + "_" + str(filename[0:-5]) + str(".csv"), "w+", newline="") as csvfile:
                        csvfile.write(str("timestamp") + "," + str("IAQ_Accuracy") + "," + str("IAQ") + "," + str("Gas") + "," + str("eCO2 ppm") + "," + str("bVOCe ppm") + "\n" )
                        for i in bme_data:
                            csvfile.write(str(i["timestamp"]) + "," + str(i["IAQ_Accuracy"]) + "," + str(i["IAQ"]) + "," + str(i["Gas"]) + "," + str(i["eCO2 ppm"]) + "," + str(i["bVOCe ppm"]) + "\n")
                            co2.append(i["eCO2 ppm"])            

                    data.close()
                    csvfile.close()
                    print("All done. Closing program.")
                    program_run = False
            else:
                pass

    except FileNotFoundError:
        
        enter_check = True
        while enter_check:
            enter = input("Please ensure you have the 'data.json' file in the same directory as this program. Please fix it and press Enter to try again.")

            if enter.lower() == "q" or enter.lower() == "quit" or enter.lower() == "exit":
                enter_check = False
                program_run == False

            else:
                enter_check = True
                program_run = True


