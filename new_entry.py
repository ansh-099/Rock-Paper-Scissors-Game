import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


capture = cv2.VideoCapture(0)

def get_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def new_entry(move):

    get_folder("dataset/" + str(move))
    counter = 1102

    while True:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)

        kernel = np.ones((3,3),np.uint8)

        r=frame[200:600, 500:900]
        cv2.rectangle(frame,(500,200),(900,600),(0,0,255),3)    
        
        hsv = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
        threshold = cv2.inRange(hsv, np.array([2, 50, 60]), np.array([25, 150, 255]))   
        

        key = cv2.waitKey(1)
        if key & 0xFF == ord('n'):
            path = f'dataset/{move}/{counter}.png'
            cv2.imwrite(path, threshold)

            print(f'move: {counter}')
            counter = counter + 1
        elif key & 0xFF == ord('q'):
            break

        cv2.namedWindow('Image ("n" to add move, "q" to exit)', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Image ("n" to add move, "q" to exit)', (800, 1200))
        cv2.imshow('Threshold', threshold)
        cv2.imshow('Image ("n" to add move, "q" to exit)', frame)
        cv2.moveWindow('Threshold', 20,20);
        cv2.moveWindow('Image ("n" to add move, "q" to exit)', 500,0);

print("Create Dataset")
move = input("Enter move name: ")
new_entry(move)
capture.release()
cv2.destroyAllWindows()
