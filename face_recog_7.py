import face_recognition as fr
import cv2
import os
import mysql.connector as s

known_faces_dir = 'E:/Pyhton_programs/new_known_faces/'
unknown_faces_dir = 'E:/Pyhton_programs/faces/'
tolerance = 0.6
MODEL = 'hog'
known_faces = []
c=0

print('loading unknown faces')
for i in os.listdir('E:/Pyhton_programs/faces/'):
    images = fr.load_image_file(os.path.join('E:/Pyhton_programs/faces/',i))
    encodings = fr.face_encodings(images)
    if encodings ==[]:
        print(encodings)
        pass
    else:
        e = encodings
        print('encoding transversing done!!! encodings stored ready to process')
        break


print('loading known faces')

for name in os.listdir('E:/Pyhton_programs/new_known_faces'):
    image = fr.load_image_file(os.path.join(known_faces_dir, name))
    encoding = fr.face_encodings(image)[0]
    known_faces.append(encoding)
         
    for i in known_faces:
        results = fr.compare_faces(i,e,tolerance)
        #print(results)
        
    if results[0]:      
        y = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #print('image successfully stored')
        
        break
    else:
        #print(' not found')
        pass
    

n=1
a = y[0]
b = y.shape[0]
l=[]
li=[]
for i in range(0,b):
    l.append(a[i])
for z in l:
    j=int(z)
    li.append(j)
    
st = str(li)
mydb = s.connect(host="localhost",user="root",password="thehero2003",database="images")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM images")

myresult = mycursor.fetchall()

for x in myresult:
    
    li = str(x[0])
    if li == st:
        print('Found')
        while n< len(x):
            print(x[n])
            n+=1
        break
    else:
        print('not matched')
    
cv2.imshow('img',y)
cv2.waitKey(0)
cv2.destroyAllWindows()
