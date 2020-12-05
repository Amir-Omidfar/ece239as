import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

imgL = cv.imread("../data/twoCamImages/piCam0.jpg")
imgR = cv.imread("../data/twoCamImages/webCam0.jpg")
imgL_gray = cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)
imgR_gray = cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)
#print(imgL_gray.shape, imgR_gray.shape)
stereo = cv.StereoBM_create(numDisparities=16,blockSize=21)
disparity = stereo.compute(imgL_gray, imgR_gray)
plt.imshow(disparity,'gray')
plt.show()
