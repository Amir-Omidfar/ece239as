import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 13
camera.start_recording('videos/vid10.h264')
camera.wait_recording(10)
camera.stop_recording()
