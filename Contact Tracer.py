# Assignment 10

# Contact Tracing App
# - A python program that will read QRCode using your webcam
# - All data read from QRCode will be stored in a text file including the date and time it was read.

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from datetime import datetime

# Access the webcam of the pc.
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# This part will serve as the scanner and decoder of the data in the QR code.
scanner = True
while scanner == True:
    _, frame = cap.read()
    Qr_info = pyzbar.decode(frame)
    for Check_profile in Qr_info:
        Person_data = Check_profile.data.decode('utf-8')
        Detect = np.array([Check_profile.polygon], np.int32)
        Detect = Detect.reshape((-1,1,2))
        cv2.polylines(frame,[Detect],True,(255,0,255),5)
        scanner = False
    cv2.imshow('Scanner', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

# Stores the decode data in the QR code in a text file including the date and time it was scanned/read.
DT = datetime.now()
date_time = DT.strftime("Date Visited: %B %d, %Y\nTime Visited: %I:%M:%S")
linesep = '--------------------------------------------------'
txtfile = open('Trace Record.txt', 'a')
txtfile.write(Person_data + '\n' )
txtfile.write(date_time + '\n')
txtfile.write(linesep + '\n')
