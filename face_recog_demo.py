import face_recognition as fr

tolerance = 0.6
images = fr.load_image_file('E:/Pyhton_programs/known_faces/horan-niall-image.jpg')
i = fr.face_encodings(images)[0]

images1 = fr.load_image_file('E:/Pyhton_programs/new_known_faces/img16.jpg')
e = fr.face_encodings(images1)[0]

results = fr.compare_faces([i],e,tolerance)
print(results)