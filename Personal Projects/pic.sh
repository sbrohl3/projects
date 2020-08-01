$DATE = $(date +"%h%d%y-%H%M%S")

# Take picture on camera 1
ffmpeg -f v4l2 -s 1920x1080 -pix_fmt yuyv422 -deinterlace -i /dev/video0 -vframes 1 cam1_$DATE.jpg -hide_banner -y

# Take picture on camera 2
ffmpeg -f v4l2 -s 1920x1080 -pix_fmt yuyv422 -deinterlace -i /dev/video2 -vframes 1 cam2_$DATE.jpg -hide_banner -y
