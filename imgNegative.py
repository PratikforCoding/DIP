import cv2
import numpy as np
def img_inv(img):
    grey1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey image',grey1)
    H,W,D=img.shape
    grey = np.zeros([H,W],dtype=np.uint8)
    for i in range(H):
        for j in range(W):
            grey[i,j]=int(255-grey1[i,j])
    cv2.imshow('negative image',grey)       

img=  cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/goMascot.webp')
cv2.imshow('input image',img) 
img_inv(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
