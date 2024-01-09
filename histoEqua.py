import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def histogram_equalization(image):
    height, width = image.shape
    total_pixels = height * width

    histogram = [0] * 256
    for i in range(height):
        for j in range(width):
            histogram[image[i, j]] += 1

    cdf = [sum(histogram[:i+1]) for i in range(256)]

    equalized_image = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            equalized_image[i, j] = int((cdf[image[i, j]] / total_pixels) * 255)

    return equalized_image

input_image = cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/mascot3.webp')

gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

equalized_image = histogram_equalization(gray_image)

cv2.imshow('input Image', input_image)
cv2.imshow('Original Image', gray_image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
