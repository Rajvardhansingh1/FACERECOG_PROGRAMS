import cv2
img = cv2.imread('E:/Pyhton_programs/new_known_faces/img3.jpg')
g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
a = g_img[0]
b = g_img.shape[0]
l=[]
li=[]
for i in range(0,b):
    l.append(a[i])
for z in l:
    j=int(z)
    li.append(j)
    
st = str(li)