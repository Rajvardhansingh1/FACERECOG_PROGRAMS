import mysql.connector as s
import cv2


connector = s.connect(host="localhost",user="root",password="Thehero2004",database="images")
img = cv2.imread('D:/Coding_Practice/Pyhton_programs/new_known_faces/new_img6.jpg')
g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
mc = connector.cursor()

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
VALUES = (st,220911328,'Rajvardhan Singh',20, 'male')
mc.execute(sql, VALUES)
connector.commit()

print(mc.rowcount, "record inserted.")