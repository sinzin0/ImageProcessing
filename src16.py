# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 14:14:33 2025

@author: jyshin
"""

import cv2 as cv

img=cv.imread('soccer.jpg')
patch=img[280:380,220:320,:]

img=cv.rectangle(img,(220,280),(320,380),(255,0,0),3)
patch1=cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_NEAREST)
patch2=cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_LINEAR)
patch3=cv.resize(patch,dsize=(0,0),fx=5,fy=5,interpolation=cv.INTER_CUBIC)

cv.imshow('Original',img)
cv.imshow('Resize nearest',patch1)
cv.imshow('Resize bilinear',patch2)
cv.imshow('Resize bicubic',patch3)

cv.waitKey()
cv.destroyAllWindows()
