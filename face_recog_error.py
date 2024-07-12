import cv2
import os

i=0
known_faces_dir = 'E:/Pyhton_programs/know_faces/'

while i<3:
    pw = input('enter system user password if you want to insert a user into the database: ')
    if pw=='letmein':
        cap=cv2.VideoCapture(0)
        check,frame = cap.read()
        cv2.imshow('img',frame)
        cap.release()
        cv2.waitKey()
        cv2.destroyAllWindows()
        break
    else:
        i+=1
        print('incorrect password try again',' ','You have',' ' ,3-i,' ','changes left')
else:
    print('all the tries are done retry later')

img_name = input('enter the user name for the image')

file_name = 'E:/Pyhton_programs/know_faces/' +str(img_name)+ 'jpg'
cv2.imwrite(file_name,frame)

print('the new image has been insterted!!!!!!!')
