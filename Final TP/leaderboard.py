#displays the leaderboard
import cv2
import songSelection

cam = cv2.VideoCapture(0)

highScores = []
highScoreName = []

def drawLeaderboard(highScores, highScoreName, count, img):
    while True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img, (100, 100), (1200,650), (145,159,242), -1)

        cv2.putText(img, 'Top 5 Scores: ', (150, 200), font, 3,(0, 0, 0),2,cv2.LINE_AA)
        cv2.putText(img, 'Press "b" to go back ', (150, 600), font, 1,(0, 0, 0),2,cv2.LINE_AA)

        for i in range(len(highScores)):
            cv2.putText(img, highScoreName[i], (150, 300+50*i), font, 1.5,(0, 0, 0),2,cv2.LINE_AA)
            cv2.putText(img, str(highScores[i]), (950, 300+50*i), font, 1.5,(0, 0, 0),2,cv2.LINE_AA)



        cv2.imshow('img', img)

        k = cv2.waitKey(1) & 0xFF

        if k == ord('h'):
            helpPage.drawHelp(img)

        if k == ord('r'):
            songSelection.drawSongSelection(img)

        if k == ord("b"):
            break 


    
print('leaderboard')
cam.release()
cv2.destroyAllWindows() 
