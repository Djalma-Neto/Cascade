import cv2
import numpy as np

def getDots(event, C, L, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(L, ' ', C)
        cv2.putText(img, ("{0} : {1}".format(L,C)), (C,L), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 1)
        cv2.imshow('image', img)

img = cv2.imread('1.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', getDots)

cv2.waitKey(0)
cv2.destroyAllWindows()