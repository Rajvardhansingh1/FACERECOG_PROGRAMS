import face_recognition as fr
import cv2
import os


known_faces_dir = 'E:/Pyhton_programs/new_known_faces/'
known_faces =[]

image_address = input("enter image path with its name and replace '/' with '//' or with '\' and kindly proceed ")
image_read = fr.load_image_file(image_address)
print('image adress collected')

face_classifier= cv2.CascadeClassifier('C:/Users/Lenovo/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image_read,cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
        cropped_face = image_read[y: y+h, x: x+w]
image_encode = fr.face_encodings(cropped_face)
'''cv2.imshow('gray',image_needed_storing)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

for name in os.listdir('E:/Pyhton_programs/new_known_faces'):
    image = fr.load_image_file(os.path.join(known_faces_dir, name))
    encoding = fr.face_encodings(image)[0]
    known_faces.append(encoding)
    
     
    for i in known_faces:
        results = fr.compare_faces(i, image_encode)
        #print(results)
    if results[0]:
        
        x = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        print('image successfully stored')
        break
    else:
        #print(' not found')
        pass