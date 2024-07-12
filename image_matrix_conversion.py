import cv2
from sklearn import preprocessing
import numpy as np


img = cv2.imread('E:/Pyhton_programs/new_known_faces/img1.jpg')
g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

a = np.array(g_img)
nor = preprocessing.minmax_scale(a, feature_range=(0, 1), axis=0, copy=True)
print(nor)
b = nor.shape

for i in b:
    c = i
for i in range(c):
    for j in range(c):
        if nor[i,j]>0.5:
            nor[i,j]=1
        else:
            nor[i,j]=0
            
