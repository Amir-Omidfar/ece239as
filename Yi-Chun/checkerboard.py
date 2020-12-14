import numpy as np
import cv2 as cv
import glob
import matplotlib.pyplot as plt
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((8*6,3), np.float32)
objp[:,:2] = np.mgrid[0:8,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('../data/checker_board/piCam/piCam11.jpg') #webcam 13, picam 11
for fname in images:
    print(fname)
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (8, 6), None)
    # If found, add object points, image points (after refining them)
    print(ret)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (8,6), corners2, ret)

        plt.figure(1)
        plt.imshow(img)
        #cv.waitKey(500)

        h, w = img.shape[:2]
        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
        print(newcameramtx)
        mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)

        for i in range(10):
            img_hand = cv.imread("../data/dataSet-12-6/right-1/picam{}.jpg".format(i))
            dst = cv.remap(img_hand, mapx, mapy, cv.INTER_LINEAR)
            dst = cv.resize(dst, (int(1.3*dst.shape[1]), int(1.3*dst.shape[0])))
            plt.imsave("../data/dataSet-12-6/right-1/undistort/picam{}.jpg".format(i), dst)
        #plt.figure(2)
        #plt.imshow(dst)
        #plt.show()
