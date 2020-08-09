import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

def get_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def create_dataset(move):

    get_folder("dataset/" + str(move))
    counter = 1102

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        kernel = np.ones((3,3),np.uint8)

        r=frame[200:600, 500:900]
        cv2.rectangle(frame,(500,200),(900,600),(0,0,255),3)    
        
        hsv = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array([2, 50, 60]), np.array([25, 150, 255]))   

        if cv2.waitKey(1) & 0xFF == ord('n'):
            path = f'dataset/{move}/{counter}.png'
            cv2.imwrite(path, mask)

            print(f'move no: {counter}')
            counter = counter + 1

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', (800, 1200))
        cv2.imshow('mask', mask)
        cv2.imshow('frame', frame)
        cv2.moveWindow("mask", 20,20);
        cv2.moveWindow("frame", 500,0);

print("Create Dataset")
move = input("Enter move name: ")
create_dataset(move)

