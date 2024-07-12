from tkinter import *
import cv2
import face_recognition as fr
import os
import mysql.connector as s

root =Tk()
root.geometry("355x70")

def cam():
   
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
            file_name='D:/Coding_Practice/Pyhton_programs/faces/user'+ str(count)+'.jpg'
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
    known_faces_dir = 'D:/Coding_Practice/Pyhton_programs/new_known_faces'
    unknown_faces_dir = 'D:/Coding_Practice/Pyhton_programs/faces/'
    tolerance = 0.5
    MODEL = 'hog'
    known_faces = []
    print('loading unknown faces')
    for i in os.listdir(unknown_faces_dir):
        images = fr.load_image_file(os.path.join('D:/Coding_Practice/Pyhton_programs/faces/',i))
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
    mycursor.execute("SELECT * FROM images")
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

def name():
    known_faces_dir = 'D:/Coding_Practice/Pyhton_programs/new_known_faces/'
    tolerance = 0.5
    known_faces =[]
    image_address = input("enter image path with its name and replace '/' with '\\' or with '\' and kindly proceed ")
    image_read = fr.load_image_file(image_address)
    print('image adress collected')
    face_classifier= cv2.CascadeClassifier('D:/Anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image_read,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cropped_face = image_read[y: y+h, x: x+w]
    image_encode = fr.face_encodings(cropped_face)
    for name in os.listdir(known_faces_dir):
        image = fr.load_image_file(os.path.join(known_faces_dir, name))
        encoding = fr.face_encodings(image)[0]
        known_faces.append(encoding)
        for i in known_faces:
            results = fr.compare_faces(i, image_encode, tolerance)
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
            print()
    cv2.imshow('img',y)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

frame = Frame(root, borderwidth=23, bg="black", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Search by Image", command=cam)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Search by address", command=name)
b2.pack(side=LEFT, padx=23)
root.mainloop()
