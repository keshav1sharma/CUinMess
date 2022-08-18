import cv2
import numpy as np
import face_recognition
import  os

# Asking program to import and find encodings for the known images

path = 'KnownFaces'
images = []
classNames = []
myList = os.listdir(path) # garbbing list of images int the folder
print(myList)

#importing images 1 by 1
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])# removing extension name from names in  list

print(classNames)
 # creating function for finding encodings for imported images and returning encoded list

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
print("encoding complete")


#initialising webcam

cap = cv2.VideoCapture(0)

#While loop to get each frame 1 by 1
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)  #REDUCING SIZE OF IMAGE BY 1/4
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB) # converting into RGB

  # Finding encoding from webcam
    facesCurFrame = face_recognition.face_encodings(imgS)
    encodesCurFrame = face_recognition.face_locations(imgS, facesCurFrame)

  # Finding match
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
         matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
         faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
         print(faceDis)





