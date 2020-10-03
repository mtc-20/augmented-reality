# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:05:32 2019

@author: Wolf/mtc-20
"""

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def display(frame):
    cv2.imshow("check", frame)
    cv2.waitKey(0)
    if cv2.waitKey(1):
        cv2.destroyAllWindows()


# Load ORB, BF and model objects
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING2, crossCheck = True)
model = cv2.imread('./../index0_s.jpg')


# Load image
frame = cv2.imread('./../3.jpg',0)
frame = cv2.flip(frame, 1)
#display(frame)

# Detect and compute keypoints 
kp_model, des_model = orb.detectAndCompute(model, None)
kp_frame, des_frame = orb.detectAndCompute(frame, None)

# Apply BF matching
matches = bf.match(des_model,des_frame)
#print(type(matches), matches)
#matches_sorted = sorted(matches, key=lambda x: x.distance)

# Filter out 75% 
good = []        
for i, m in enumerate(matches):
    if i < len(matches) - 1 and m.distance < 0.75 * matches[i+1].distance:
        good.append(m)

print(len(good))

# Draw the matching keypoints between model and image
out = cv2.drawMatches(model, kp_model, frame, kp_frame, good[:], 0, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
display(out)
#plt.imshow(frame),plt.show()



drawkp_model = cv2.drawKeypoints(model,kp_model,0)
#plt.imshow(frame_model),plt.show()
display(drawkp_model)

drawkp_frame = cv2.drawKeypoints(frame, kp_frame, frame)
display(drawkp_frame)
# cv2.imshow("output", frame_model)
