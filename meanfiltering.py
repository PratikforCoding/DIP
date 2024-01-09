import cv2
import numpy as np

def mean_filtering(image, kernel_size):
    
    pad = kernel_size // 2  
    padded_image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)

    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size**2)

    filtered_image = np.zeros_like(image)
    for i in range(pad, image.shape[0] + pad):
        for j in range(pad, image.shape[1] + pad):
            roi = padded_image[i - pad:i + pad + 1, j - pad:j + pad + 1]
            
            filtered_image[i - pad, j - pad] = np.sum(roi * kernel)

    return filtered_image

image = cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/king.jpeg', cv2.IMREAD_GRAYSCALE)
filtered_image = mean_filtering(image, 3) 

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
