import cv2
import face_recognition as fr
import os
import mysql.connector as s

face_classifier= cv2.CascadeClassifier('D:/Anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is ():
        return None
    for (x,y,w,h) in faces:
        cropped_face = img[y: y+h, x: x+w]
    
    return cropped_face

cap =cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        file_name='D:/Coding_Practice/Pyhton_programs/teacher_unknown_face/user'+ str(count)+'.jpg'
        cv2.imwrite(file_name,face)
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow(' face cropper',face)
    else:
        print(" Face not found")
        pass
    if cv2.waitKey(1)==13 or count==10:
        break
cap.release()
cv2.destroyAllWindows()
print(" Collecting samples complete!!!")
known_faces_dir = 'D:/Coding_Practice/Pyhton_programs/teacher_known_face'
unknown_faces_dir = 'D:/Coding_Practice/Pyhton_programs/teacher_unknown_face/'
tolerance = 0.8
MODEL = 'hog'
known_faces = []
print('loading unknown faces')
for i in os.listdir(unknown_faces_dir):
    images = fr.load_image_file(os.path.join('D:/Coding_Practice/Pyhton_programs/teacher_unknown_face/',i))
    encodings = fr.face_encodings(images)
    if encodings ==[]:
        print(encodings)
        pass
    else:
        e = encodings
        print('encoding transversing done!!! encodings stored ready to process')
        break
print('loading known faces')
for name in os.listdir(known_faces_dir):
    image = fr.load_image_file(os.path.join(known_faces_dir, name))
    encoding = fr.face_encodings(image)[0]
    known_faces.append(encoding)
    for i in known_faces:
        results = fr.compare_faces(i, e, tolerance)
        #print(results)
    if results[0]:
        y = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        print('image successfully stored')
        break
    else:
        #print(' not found')
        pass
   
#finding image in database
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
mycursor.execute("SELECT * FROM teacher_images")
myresult = mycursor.fetchall()
for x in myresult:
    li = str(x[0])
    if li == st:
        print('user found')
        while n< len(x):
            print(x[n])
            n+=1
        break
    else:
        print('not matched')
cv2.imshow('img',y)
cv2.waitKey(0)
cv2.destroyAllWindows()             

