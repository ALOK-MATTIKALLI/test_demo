import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture('test_vedio.mp4')
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def nothing(a):
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',600,250)
cv2.createTrackbar('Huemin', 'Trackbars', 0,180, nothing)
cv2.createTrackbar('Huemax', 'Trackbars', 180,180, nothing)
cv2.createTrackbar('Satmin', 'Trackbars', 0,255, nothing)
cv2.createTrackbar('Satmax', 'Trackbars', 255,255, nothing)
cv2.createTrackbar('Valmin', 'Trackbars', 0,255, nothing)
cv2.createTrackbar('Valmax', 'Trackbars', 255,255, nothing)

frameCounter = 0

while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0
    
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos('Huemin','Trackbars')
    hmax = cv2.getTrackbarPos('Huemax','Trackbars')
    smin = cv2.getTrackbarPos('Satmin','Trackbars')
    smax = cv2.getTrackbarPos('Satmax','Trackbars')
    vmin = cv2.getTrackbarPos('Valmin','Trackbars')
    vmax = cv2.getTrackbarPos('Valmax','Trackbars')
    # print(hmin,hmax,smin,smax,vmin,vmax)

    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img,mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])
    cv2.imshow('Horizontal Stacking', hstack)
    # cv2.imshow('mask', mask)
    cv2.imshow('img', img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        # cv2.waitKey(0)
        break
    
cv2.release()
cv2.destroyAllWindow()