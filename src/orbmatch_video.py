'''
Created on Saturday, 3rd October 2020 8:13::01 pm
@author: mtc-20
 Coded on VS Code 2019
------
Overview:
 
------
Last Modified: Sat Oct 03 2020
'''
import cv2
import numpy as np

def display(frame):
    cv2.imshow("check", frame)
    cv2.waitKey(0)
    if cv2.waitKey(1):
        cv2.destroyAllWindows()


# Load ORB, BF and model objects
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING2, crossCheck = True)
model = cv2.imread('./../index0_s.jpg')


# Detect and compute keypoints 
kp_model, des_model = orb.detectAndCompute(model, None)

try:
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Result', cv2.WINDOW_NORMAL)        
    cv2.resizeWindow('Result', 640,480)

    while True:
        ret, frame = cap.read()
        # frame = cv2.flip(frame, 1)
        kp_frame, des_frame = orb.detectAndCompute(frame, None)
        matches = bf.match(des_model,des_frame)
        good = []
        for index, m in enumerate(matches):
            if index < len(matches) - 1 and m.distance < 0.75 * matches[index+1].distance:
                good.append(m)
        if len(good) < 5:
    #        print(len(good))
            cv2.imshow("Result", frame)
            k = cv2.waitKey(1)
        else:
            out = cv2.drawMatches(model, kp_model, frame, kp_frame, good[:], 0, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            cv2.imshow("Result", out)
            k = cv2.waitKey(1)
        if k%256 ==27:
            print("[INFO] User induced exit...")
            break
        
        
    cap.release()
    cv2.destroyAllWindows()


except Exception as e:
    print("[ERR] ", e)
    print("[INFO] Closing...")
    cap.release()
    cv2.destroyAllWindows()