import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def con(img):
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey',grey)
    H,W=grey.shape
    new=np.zeros([H,W],dtype=np.uint8)
    Max=np.max(grey)
    Min=np.min(grey)
    print("Before contrast stretching the min and max value of img is:=",Min,"&",Max)
    outs=int(input("enter the output start: "))
    oute=int(input("enter the output end: "))
    for i in range(H):
         for j in range(W):
            r = grey[i,j]
            new[i,j]=((r-Min)/(Max-Min)*(oute-outs))+(outs)
    Max1=np.max(new)
    Min1=np.min(new)
    print("After contrast stretching the min and max value of img is:=",Min1,"&",Max1)
    cv2.imshow("contast",new)
    return new
    

img=cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/mascot2.jpeg')
cv2.imshow('img',img)
con(img)
cv2.waitKey(0)
cv2.destroyAllWindows()	
