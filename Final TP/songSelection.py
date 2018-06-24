#draws the song selection page

import cv2
import modeSelection
cam = cv2.VideoCapture(0)

width = 1300
height = 750

filename = ""

def drawSongSelection(img):
    while True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img, (100, 100), (1200,650), (145,159,242), -1)

        cv2.putText(img,'Song Selection',(150, 200), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'Press number to choose:',(150, 250), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)

        cv2.putText(img,'#1 Pretty Girl (Cheat CodesxCADE Remix) - Maggie Lindemann',(150, 350), font, 1,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'#2 You Should Talk - Fletcher',(150, 400), font, 1,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'#3 Input My Own Song!!!',(150, 450), font, 1,(0, 0, 0),1,cv2.LINE_AA)


        cv2.imshow('img', img)

        k = cv2.waitKey(1) & 0xFF

        if k == ord('1'):
            filename = "Pretty-Girl-_Cheat-Codes-x-Cade-Remix_.wav"
            modeSelection.selectMode(img, filename)

        if k == ord('2'):
            filename = "You-Should-Talk-Fletcher.wav"
            modeSelection.selectMode(img, filename)

        if k == ord('3'):
            try:
                filename = input("Name of the file (include the .wav at the end):   ")
                modeSelection.selectMode(img, filename)
            except:
                print('THIS SONG CAN NOT BE PLAYED!!!!')
                break

        if k == 27:
            break


    
print('import songSelection')

