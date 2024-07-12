import face_recognition as fr
import os
import cv2


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
        file_name='E:/Pyhton_programs/faces/user'+ str(count)+'.jpg'
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

# compaaring faces


known_faces_dir = 'D:/Coding_Practice/Pyhton_programs/new_known_faces/'
unknown_faces_dir = 'D:/Coding_Practice/Pyhton_programs/faces/'
tolerance = 0.6
MODEL = 'hog'
known_faces = []

print('loading unknown faces')
for i in os.listdir('D:/Coding_Practice/Pyhton_programs/faces/'):
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

for name in os.listdir('D:/Coding_Practice/Pyhton_programs/new_known_faces'):
    image = fr.load_image_file(os.path.join(known_faces_dir, name))
    encoding = fr.face_encodings(image)
    known_faces.append(encoding)
         
    for i in known_faces:
        results = fr.compare_faces(i, e)
        print(results)
    if results[0]:      
        x = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        print('image successfully stored')
        break
    else:
        #print(' not found')
        pass
    
cv2.imshow('img',x)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('img',x)
cv2.waitKey(0)          
