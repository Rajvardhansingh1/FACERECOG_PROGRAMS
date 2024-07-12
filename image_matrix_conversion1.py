import cv2
import numpy as np

img = cv2.imread('E:/Pyhton_programs/new_known_faces/img3.jpg')
g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
a = g_img[0]
l=[]
b = g_img.shape[0]

for i in range(0,b):
    l.append(a[i])
li=[]
#st=str(l)
for z in l:
    j=int(z)
    li.append(bin(j))
    
st = str(li)
