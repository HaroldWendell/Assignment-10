# Assignment 10

# Contact Tracing App
# - A python program that will read QRCode using your webcam
# - All data read from QRCode will be stored in a text file including the date and time it was read

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

scanner = True
while scanner == True:
    _, frame = cap.read()
    Qr_info = pyzbar.decode(frame)
    for Check_profile in Qr_info:
        Person_data = Check_profile.data.decode('utf-8')
        Detect = np.array([Check_profile.polygon], np.int32)
        Detect = Detect.reshape((-1,1,2))
        cv2.polylines(frame,[Detect],True,(255,0,255),5)
        print(Person_data)
        scanner = False
    cv2.imshow('Scanner', frame)
    key = cv2.waitKey(1)