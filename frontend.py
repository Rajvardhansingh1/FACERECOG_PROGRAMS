# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:02:57 2024

@author: Aditya
"""
import datetime
import subprocess
import tkinter as tk
from PIL import Image,ImageTk
#import util
import cv2
import face_recognition as fr
import os
import mysql.connector as s
from tkinter import messagebox

def get_button(window,text,color,command,fg='white'):
    button = tk.Button(
                        window,
                        text=text,
                        activebackground="black",
                        activeforeground="white",
                        fg=fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,
                        font=('Helvetica bold',20)
                        )
    return button

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0,column=0)
    return label

def get_text_label(window,text):
    label = tk.Label(window,text=text)
    label.config(font=("sans-serif",21),justify="left")
    return label

def get_entry_text(window):
    inputtxt = tk.Text(window,
                       height=2,
                       width=15,font=("Arial",32))
    return inputtxt

def msg_box(title,description):
    messagebox.showinfo(title,description)

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")
        
        self.login_button_main_window = get_button(self.main_window,'login','green',self.login)
        self.login_button_main_window.place(x=500,y=100)
        
        self.register_new_user_button_main_window = get_button(self.main_window,'register new user','green',
                                                                    self.register_new_user,fg='black')
        self.register_new_user_button_main_window.place(x=500,y=250)
       
        
        self.db_dir = 'D:/Coding_Practice/Pyhton_programs/new_known_faces'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
            
        self.log_path = './.log.txt'
            
       
        
        
    def login(self):
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
                msg_box("Image Found",'image has been found')
                break
            else:
                print('not found')
                pass
        msg_box("Success login", "You have successfully login now you can view your image and the information")
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
                    msg_box("Information", (x[n]))
                    n+=1
                break
            else:
                print("No information found")
        if str(x[1]):
            reg_no = str(x[1])
            mycursor.execute("SELECT * FROM course WHERE student_id = " + "'" + reg_no + "'")
            myresult = mycursor.fetchall()
            msg_box("Course info",(myresult))
            mycursor.execute("SELECT * FROM medicalrecord WHERE Sid = " + "'" + reg_no + "'")
            myresult = mycursor.fetchall()
            msg_box("medical info",(myresult))
            cv2.imshow('img',y)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def register_new_user(self):
        self.register_new_user_window = tk.Tk()
        #self.register_new_user_window = tk.TopLevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")
        
        name = input("Enter your name : ")
        reg_no = int(input("Enter registration number : "))
        age = int(input("Enter your age : "))
        gender = input("Enter your gender : ")
        cid = int(input("Enter course id"))
        coursename = input("enter course name")
        teachername = input("Enter teacher name")

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
                file_name='D:/Coding_Practice/Pyhton_programs/new_known_faces/' + name +'.jpg'
                cv2.imwrite(file_name,face)
                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                cv2.imshow(' face cropper',face)
            else:
                print(" Face not found")
                pass
            if cv2.waitKey(1)==13 or count==1:
                break
        cap.release()
        cv2.destroyAllWindows()
        print(" Collecting samples complete!!!")

        connector = s.connect(host="localhost",user="root",password="Thehero2004",database="images")
        mc = connector.cursor()
        img = cv2.imread('D:/Coding_Practice/Pyhton_programs/new_known_faces/' + name + '.jpg')
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

        sql = "INSERT INTO images (id,student_id,name,Age,Gender) VALUES (%s,%s,%s,%s,%s)"
        VALUES = (st,reg_no,name,age,gender)
        mc.execute(sql, VALUES)
        
        sql = "INSERT INTO course (student_id, Cid,Course_name,Teacher_name) VALUES (%s,%s,%s,%s)"
        VALUES = (reg_no, cid, coursename,teachername)
        mc.execute(sql, VALUES)
        connector.commit()
        print('signin complete')
        
        # self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window,'Accept','green',self.accept_register_new_user)
        # self.accept_button_register_new_user_window.place(x=750,y=300)
        
        # self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window,'Try Again','red',self.accept_register_new_user)
        # self.try_again_button_register_new_user_window.place(x=750,y=400)
        
        # self.capture_label = util.get_img_label(self.register_new_user_window)
        # self.capture_label.place(x=10,y=0,width=700,height=500)
        
        # self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        # self.entry_text_register_new_user.place(x=750,y=150)
        
        # self.text_label_register_new_user = util.get_text_label(self.register_new_user_window,'Please input username:')
        # self.text_label_register_new_user.place(x=750,y=70)
        
    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()
        
    def add_img_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        
        self.register_new_user_capture = self.most_recent_capture_arr.copy()
        
        
    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0,"end-1.c")
        
        
        util.msg_box('Success!','User registered successfully!')
        
        self.register_new_user_window.destroy()
    
    def start(self):
        self.main_window.mainloop()
    
if __name__=="__main__":
    app = App()
    app.start()