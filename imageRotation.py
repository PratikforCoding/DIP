import cv2
import numpy as np 
def rot(img):
    grey1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    cv2.imshow('grey image',grey1)
    H,W=grey1.shape
    grey = np.zeros([W,H],dtype=np.uint8) 
    for i in range(H):
        for j in range(W): 
            grey[j,i] = grey1[i,j]
    cv2.imshow('rotate image',grey)
img= cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/goMascot.webp') 
rot(img)
cv2.waitKey(0)
cv2.destroyAllWindows()