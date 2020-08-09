import os
import numpy as np
import cv2
import keras
from keras.preprocessing import image
from keras.models import load_model

def get_result(user):
    computer = np.random.randint(0, 3)
    if user == 0 and computer == 1:
        return 'User Win', computer
    elif user == 0 and computer == 2:
        return 'Computer Win', computer
    elif user == 1 and computer == 2:
        return 'User Win', computer
    elif user == 1 and computer == 0:
        return 'Computer Win', computer
    elif user == 2 and computer == 0:
        return 'User Win', computer
    elif user ==2 and computer == 1:
        return 'Computer Win', computer
    elif user == computer:
        return "Draw", computer
    else:
        return "Try Again", computer

def print_result(num):
    if num == 0:
        return("Paper")
    elif num == 1:
        return("Rock")
    elif num == 2:
        return("Scissors")
    else:
        return("Please Try Again")

model = load_model('model.h5')
capture = cv2.VideoCapture(0)
user_choice = ""
computer_choice = ""
text_result = "" 

while(True):

    ret, frame = capture.read()
    frame=cv2.flip(frame,1)
    r=frame[200:600, 500:900]
    cv2.rectangle(frame,(500,200),(900,600),(0,0,255),3)   
    
    kernel = np.ones((3,3),np.uint8)
    hsv = cv2.cvtColor(r, cv2.COLOR_BGR2HSV)
    threshold = cv2.inRange(hsv, np.array([2, 50, 60]), np.array([25, 150, 255]))

    key = cv2.waitKey(1)
    if key & 0xFF == ord('n'):
        out = cv2.imwrite('playing.png', threshold)
        print('Turn played')
        image_path = 'playing.png'
        img = image.load_img(image_path, target_size=(50,50), color_mode='grayscale')

        user_img = image.img_to_array(img)
        user_img = np.expand_dims(user_img, axis=0)
        predict = model.predict_classes(user_img)[0]

        text_result, computer_choice = get_result(predict)
        user_choice = print_result(predict)
        computer_choice = print_result(computer_choice)
        print(text_result)

    elif key & 0xFF == ord('q'):
        break
    

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Click "n" to make next move, "q" to Quit',(0,50), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.putText(frame,"User: ",(0,100), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.putText(frame, user_choice,(90,100), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.putText(frame,"Computer: ",(0,150), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.putText(frame, computer_choice,(170,150), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.putText(frame,"Result: ",(0,200), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.putText(frame, text_result, (110,200), font, 1, (0,255,0), 2, cv2.LINE_AA)
    cv2.namedWindow('Game: Place your move in box and press "n". To quit press "q"', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Game: Place your move in box and press "n". To quit press "q"', (800, 1200))
    cv2.imshow('Threshold', threshold)
    cv2.imshow('Game: Place your move in box and press "n". To quit press "q"', frame)
    cv2.moveWindow('Threshold', 20,20);
    cv2.moveWindow('Game: Place your move in box and press "n". To quit press "q"', 500,0);
    
# Finished playing
capture.release()
cv2.destroyAllWindows()