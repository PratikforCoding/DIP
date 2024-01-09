import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
def his(img):
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey',grey)
    H,W=grey.shape
    new = np.zeros([256],dtype=np.uint8)
    for i in range(H):
        for j in range(W):
            ind = grey[i,j]
            new[ind]+= 1
    plt.bar(np.arange(len(new)),new)
    plt.show()
img=  cv2.imread('/Users/pratikkotal/Documents/dipAssignment/test/goMascot.webp')
cv2.imshow('img',img)
his(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
