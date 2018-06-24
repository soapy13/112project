#draws the mode selection page

from main import *
import cv2


def selectMode(img, filename):
    while True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img, (100, 100), (1200,650), (145,159,242), -1)

        cv2.putText(img,'MODES',(150, 150), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'Press "e" for easy',(150, 250), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'Press "m" for medium',(150, 300), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'Press "h" for hard',(150, 350), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        
        cv2.imshow('img', img)


        k = cv2.waitKey(1) & 0xFF
        if k == ord('e'):
            mode = 'e'
            run(filename, mode)
        elif k == ord('m'):
            mode = 'm'
            run(filename, mode)
        elif k == ord('h'):
            mode = 'h'
            run(filename, mode)