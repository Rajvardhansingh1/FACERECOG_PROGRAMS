import face_recognition as fr
import os
import cv2

TOLERANCE = 0.6
k_unknown = fr.load_image_file('D:/Coding_Practice/Pyhton_programs/faces/user1.jpg')
uk_encode = fr.face_encodings(k_unknown)
'''print(k_unknown)
print(uk_encode)'''

for i in os.listdir('D:/Coding_Practice/Pyhton_programs/known_faces'):
    images = cv2.imread(os.path.join('D:/Coding_Practice/Pyhton_programs/new_known_faces/',i))
    #print(images)
    k_encode = fr.face_encodings(images)
    #print(k_encode)
    
    results = fr.compare_faces(uk_encode, k_encode,TOLERANCE)
    
    if True in results :
        x=images
        print("user found")
        break
    else:
        print('not found in our user database')
#print(x)
x_gray = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
print(x_gray)
cv2.imshow('gray',x_gray)
cv2.waitKey(1000)


