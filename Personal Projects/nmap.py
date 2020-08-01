#!/usr/python/bin/env python

import nmap3

nm = nmap3.Nmap()

class Nmap:

    ''' A simple class to run Nmap in Python '''

    def __init__(self, ip=""):

        ''' A simple constructor to init variables used in the Nmap Class ''' 

        self.ip = ip

    def portScan(self):

        ''' A simple method to scan open ports in the given IP range defined by the user '''
        
        print("Starting Nmap Port Scan.\nPlease wait...")

        results = nm.nmap_version_detection(self.ip)

        return results


## Note: 
########
## This method needs to validate user input
## Create a validator module! 
## 04/20/2020 - Steven
osType = ""
## Take in user input for IP and PORT number
n = Nmap()
n.ip = str(input("What is the IP range you want to scan: "))

try:

    for item in n.portScan():
        if item["service"]["ostype"]:
            print("Open Ports: ", item["port"], " - ", item["protocol"], "\nOS Type: ")
            osType = item["service"]["ostype"]


        else:
            pass
except:
    for item in n.portScan():
        print("Open Ports: ", item["port"], " - ", item["protocol"])

if osType:
    print(osType)

else:
    pass

print("Done.")