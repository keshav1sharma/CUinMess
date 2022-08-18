import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)  # enabling webcam
cap.set(3, 640)
cap.set(4, 480)

with open('Auth_Data_values.txt') as f:
  myDataList = f.read().splitlines()
print(myDataList)


# def markAttendance(name):
#   with open('Attendance.csv','r+') as f:
#     myDataList = f.readlines()
#     nameList = []
#     for line in myDataList:
#       entry = line.split(',')
#       nameList.append(entry[0])
#     if name not in nameList:
#       now = datetime.now()
#       dtString = now.strftime('%H:%M:%S')
#       f.writelines(f'\n{name},{dtString}')






while True:

  success, img = cap.read()
  for barcode in decode(img):
    myData = barcode.data.decode('utf-8')  # converting data into string
    print(myData)

    if myData in myDataList:
      myOutput = "Authorized"
      myColor = (0,255,0)
    else:
      myOutput = "Un-Authorized"
      myColor = (0,0,255)
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape(-1, 1, 2)
    cv2.polylines(img, [pts], True,myColor, 5)  # drawing polygon around qr code
    pts2 = barcode.rect
    cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)

  cv2.imshow('Result', img)
  cv2.waitKey(1)


  imgTest = os.path.join('KnownFaces/', myData) #image to compare with
  imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
  # realtime image size has been divided by 4 using 0.25
  imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

  facesCurFrame = face_recognition.face_locations(imgS)
  encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
  encodeTest = face_recognition.face_encodings(imgTest)[0]

  result = face_recognition.compare_faces(encodeTest,encodeCurFrame,0.45)
  print(result)
