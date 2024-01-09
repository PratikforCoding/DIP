import cv2
import numpy as np

img1 =  cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/baracktocat.jpg')
H,W,D = img1.shape

greyone=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.imshow('greyone',greyone)
img2 =  cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/mascot3.webp')
h,w,d=img2.shape
greytwo=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('greytwo',greytwo)
new = np.zeros([H,W],dtype=np.uint8)
for i in range(H):
        for j in range(W):
                new[i,j]=int(greyone[i,j]/2+greytwo[i,j]/2)
                
cv2.imshow('adding image',new)

cv2.waitKey(0)
cv2.destroyAllWindows()

