import cv2 as cv

img = cv.imread('photos/Andrew and Kate 2.jpg')

cv.imshow('Andrew and Kate', img)

cv.waitKey(0)