from picamera import PiCamera
from time import sleep





camera = PiCamera()
camera.framerate = 13
camera.resolution = (640,480)
count = 30


for i in range(count,count+10):
    sleep(0.2)
    camera.capture('images/piCam%s.jpg' % i)
