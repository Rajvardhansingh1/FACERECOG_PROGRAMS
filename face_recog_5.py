# convereting Previous database images into gray
import os
import cv2


images=[]
list1 = []
count = 0
face_classifier= cv2.CascadeClassifier('D:/Anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

for i in os.listdir('D:/Coding_Practice/Pyhton_programs/known_faces'):
    img = cv2.imread(os.path.join('D:/Coding_Practice/Pyhton_programs/known_faces',i))
    
    if img is not None:
        images.append(img)
for i in images:
    gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        c_img = gray[y: y+h, x: x+w]
        list1.append(c_img)       
        
print(len(list1))
print(len(images))

for m in list1:
    count+=1
    f_name = 'D:/Coding_Practice/Pyhton_programs/new_known_faces/new_img' + str(count) + '.jpg'
    cv2.imwrite(f_name, m)
    cv2.putText(m,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
cv2.destroyAllWindows()   