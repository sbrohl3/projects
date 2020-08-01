#!/bin/bash

# cd to video dir
cd ~/videos

# Create date variable to append to filename
DATE=$(date +"%h%d%y-%H%M%S")

# ffmpeg create video 
ffmpeg -f v4l2 -input_format mjpeg -i /dev/video0 -c:v copy cam1_$DATE.mkv -hide_banner -y | ffmpeg -f v4l2 -input_format mjpeg -i /dev/video2 -c:v copy cam2_$DATE.mkv -hide_banner -y 

# copy recorded videos to Flash drive
cp ~/videos/* /media/usb


