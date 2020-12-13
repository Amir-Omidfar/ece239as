import time 
import os 


count = 10

for i in range(count,count+10):
    os.system('fswebcam -r 640x480 -d /dev/video1 --no-banner --jpeg 200 --save /fsImages/f%s.jpg' %i)

