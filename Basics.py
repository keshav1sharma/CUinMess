import cv2
import numpy as np
import os
import face_recognition


while True:
  cap = cv2.VideoCapture(0)  # enabling webcam
  # cap.set(3, 640)
  # cap.set(4, 480)

  myData = "Aadarsh.jpg"
  imgCurr = cap.read()
  imgTest = os.path.join('KnownFaces/', myData)  # image to compare with


  facesCurFrame = face_recognition.face_locations(imgCurr)
  encodeCurFrame = face_recognition.face_encodings(imgCurr, facesCurFrame)
  encodeTest = face_recognition.face_encodings(imgTest)[0]

  result = face_recognition.compare_faces(encodeTest, encodeCurFrame, 0.45)
  # cv2.imshow()
  # cv2.waitKey(1)
  print(result)
