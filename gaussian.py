import cv2
import numpy as np
import random
   
img=cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/mascot3.webp')
cv2.imshow('input img',img)
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
x=int(input("enter the noise resolution [0<High]: "))
noise = np.random.normal(0,x,grey.shape)

cv2.imshow('grey img',grey)
img_noise=grey+noise
img_noise=np.clip(img_noise,0,255).astype(np.uint8)
cv2.imshow('output img',img_noise)

cv2.waitKey(0)
cv2.destroyAllWindows()
