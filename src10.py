# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 13:05:11 2025

@author: jyshin
"""

import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg')
h=cv.calcHist([img], [2], None, [256], [0,256])
plt.plot(h,color='r',linewidth=1)