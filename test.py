# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:13:05 2021

@author: vinay
"""

from grip import GripPipeline
import cv2
import requests

vid = cv2.VideoCapture('rtsp://admin:admin@10.186.57.228:8554/live')
#vid = cv2.VideoCapture(0)

pipeline = GripPipeline()

num_contours = 0

while True:
    ret, img = vid.read()
        
    #img = cv2.imread('download.jpg')
    
    pipeline.process(img)
    
    contours = pipeline.filter_contours_output

    num_contours = len(contours)  

    for contour in contours:
        for i in range(len(contour) - 1):
            img = cv2.line(img, tuple(contour[i][0]), tuple(contour[i + 1][0]), (0, 0, 255), 2)
        img = cv2.line(img, tuple(contour[len(contour) - 1][0]), tuple(contour[0][0]), (0, 0, 255), 2)
  
    requests.get("http://127.0.0.1:5000/input/" + str(num_contours))  
  
    cv2.imshow("img", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

'''
import cv2
  
# define a video capture object
vid = cv2.VideoCapture(1)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
'''
