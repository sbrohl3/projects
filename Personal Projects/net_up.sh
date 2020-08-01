#!/bin/bash

# A variable set to the status of the wwan0 interface

sleep 10
STATE=`ifconfig wwan0 | grep -o UP`

# if the interface is down turn it on, ask for an IP
if [ "$STATE" != "UP" ]; then
    ifconfig wwan0 up
    sleep 5s 
    echo 'AT+CGDC0NT=1,"IP","devapn.gdsp"' > /dev/ttyUSB2
    echo 'AT^NDISDUP=1,1,' > /dev/ttyUSB2
   # ifconfig wwan0 | grep -o UP > /home/ifdwn.txt 
    dhclient -v wwan0

elif [ "$STATE" == "UP" ]; then
    sleep 5s 	  
    echo 'AT+CGDC0NT=1,"IP","devapn.gdsp"' > /dev/ttyUSB2
    echo 'AT^NDISDUP=1,1,' > /dev/ttyUSB2
    #ifconfig wwan0 | grep -o UP > /home/ifup.txt
    dhclient -v wwan0

else
   echo "The interface is in an unknown state and the script has encountered an error. @: "  $(date) >> ~/net_up_error_log.txt
fi
