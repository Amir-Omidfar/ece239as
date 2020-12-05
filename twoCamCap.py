from picamera import PiCamera
from time import sleep
import os




camera = PiCamera()
camera.framerate = 13
camera.resolution = (480,640)
count = 0


for i in range(count,count+16):
    os.system('fswebcam -r 480x640 -d /dev/video0 --rotate -90 --no-banner --jpeg 200 --save twoCamImages/webCam%s.jpg' %i)
    sleep(0.01)
    camera.capture('twoCamImages/piCam%s.jpg' % i)
    sleep(0.5)
