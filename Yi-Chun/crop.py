import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

picam = plt.imread("../data/dataSet-12-6/right-1/undistort/picam2.jpg")
    #imgR = cv2.imread('depth2.jpg')
webcam = plt.imread("../data/dataSet-12-6/right-1/undistort/webcam2.jpg")


plt.figure(1)
plt.imshow(picam)
plt.figure(2)
plt.imshow(webcam)
plt.show()

x= 100
y= 50
picam_center = np.array([239, 602])
webcam_center = np.array([161, 576])
picam_start = [picam_center[0]-x, picam_center[1]-y-100]
picam_end = [picam_center[0]+x+100, picam_center[1]+y]
webcam_start = [webcam_center[0]-x, webcam_center[1]-y-100]
webcam_end = [webcam_center[0]+x+100, webcam_center[1]+y]

imgL = picam[picam_start[0]:picam_end[0], picam_start[1]:picam_end[1]]
imgR = webcam[webcam_start[0]:webcam_end[0], webcam_start[1]:webcam_end[1]]
imgL=cv.cvtColor(imgL, cv.COLOR_BGR2GRAY)
imgR=cv.cvtColor(imgR, cv.COLOR_BGR2GRAY)

#plt.subplot(211)
#plt.imshow(imgL, cmap='gray')
#plt.subplot(212)
#plt.imshow(imgR, cmap='gray')
#plt.show()
stereo = cv.StereoSGBM_create(minDisparity=0 , numDisparities=48, blockSize=5, speckleWindowSize = 6, speckleRange = 40, disp12MaxDiff=2)
disparity = stereo.compute(imgR,imgL) / 16.0
disparity = disparity - np.min(disparity)
disparity = disparity / np.max(disparity)
plt.subplot(311)
plt.imshow(imgL, cmap='gray')
plt.subplot(312)
plt.imshow(imgR, cmap='gray')
plt.subplot(313)
plt.imshow(disparity,'gray')
plt.show()

plt.imsave("../result/exp10_right2/imgL_crop.jpg", imgL, cmap='gray')
plt.imsave("../result/exp10_right2/imgR_crop.jpg", imgR, cmap='gray')
plt.imsave("../result/exp10_right2/disparity.jpg", disparity[:, 50:], cmap='gray')
'''
plt.subplot(211)
plt.imshow(picam[picam_start[0]:picam_end[0], picam_start[1]:picam_end[1]])
plt.subplot(212)
plt.imshow(webcam[webcam_start[0]:webcam_end[0], webcam_start[1]:webcam_end[1]])
plt.show()
'''
