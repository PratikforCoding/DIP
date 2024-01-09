import cv2
import numpy as np

def apply_prewitt(image):
    height, width = image.shape
    result_image = np.zeros((height, width), dtype=np.uint8)

    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])

    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            gx = np.sum(kernel_x * image[i-1:i+2, j-1:j+2])
            gy = np.sum(kernel_y * image[i-1:i+2, j-1:j+2])

            gradient_magnitude = int(np.sqrt(gx**2 + gy**2))

            result_image[i, j] = max(0, min(255, gradient_magnitude))

    return result_image

input_image = cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/mascot2.jpeg')

gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

edge_result = apply_prewitt(gray_image)

cv2.imshow('Original Image', gray_image)
cv2.imshow('Prewitt Edge Detection', edge_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
