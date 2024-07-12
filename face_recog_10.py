import face_recognition as fr
import cv2
import os
import mysql.connector as s

known_faces_dir = 'D:/Coding_Practice/Pyhton_programs/new_known_faces/'
known_faces =[]
tolerance =0.5

image_address = input("enter image path with its name and replace '/' with '//' or with '\' and kindly proceed ")
image_read = fr.load_image_file(image_address)
print('image adress collected')

face_classifier= cv2.CascadeClassifier('D:/Anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image_read,cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cropped_face = image_read[y: y+h, x: x+w]
    image_encode = fr.face_encodings(cropped_face)
    
for name in os.listdir('D:/Coding_Practice/Pyhton_programs/new_known_faces'):
    image = fr.load_image_file(os.path.join(known_faces_dir, name))
    encoding = fr.face_encodings(image)[0]
    known_faces.append(encoding)
    for i in known_faces:
        results = fr.compare_faces(i, image_encode,tolerance)
        #print(results)
    if results[0]:
        
        y = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        print('image successfully stored')
        break
    else:
        #print(' not found')
        pass

a = y[0]
b = y.shape[0]
l=[]
li=[]
n=1
for i in range(0,b):
    l.append(a[i])
for z in l:
    j=int(z)
    li.append(j)
st = str(li)
mydb = s.connect(host="localhost",user="root",password="Thehero2004",database="images")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM images")
myresult = mycursor.fetchall()
for x in myresult:
    li = str(x[0])
    if li == st:
        print('User found')
        while n< len(x):
            print(x[n])
            n+=1
        break
    else:
        print('not matched')

cv2.imshow('img',y)
cv2.waitKey(0)
cv2.destroyAllWindows()
