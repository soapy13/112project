#draws the help page
import cv2
needHelp = True
cam = cv2.VideoCapture(0)

def drawHelp(img):
    while True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img, (100, 100), (1200,650), (145,159,242), -1)

        cv2.putText(img,'Welcome to HANDS HANDS REVOLUTION!',(150, 150), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'This is a game where you hit the ',(150, 250), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'beats to the beat of the music.',(150, 300), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'Hold a red ball in one hand and a blue',(150, 350), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'ball in the other. Try to hit ',(150, 400), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'the beats when they reach the base.',(150, 450), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)
        cv2.putText(img,'Press "h" to go back',(150, 550), font, 1.5,(0, 0, 0),1,cv2.LINE_AA)

        cv2.imshow('img', img)

        k = cv2.waitKey(1) & 0xFF

        if k == ord('h'):
            break

        if k == 27:
            break

    

print('import drawHelp')
cam.release()
cv2.destroyAllWindows() 
