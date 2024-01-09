import cv2
import numpy as np

def threshold_segmentation(image, threshold_value):
   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey Image', gray_image)

    ret,binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

image = cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/king.jpeg')

threshold_value =80

segmented_image = threshold_segmentation(image, threshold_value)

cv2.imshow('Original Image', image)
cv2.imshow('Threshold Segmentation', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
