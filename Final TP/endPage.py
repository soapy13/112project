#draws the end page
import cv2
import songSelection, leaderboard
needHelp = True
cam = cv2.VideoCapture(0)

width = 1300
height = 750




def drawEnd(score, img, name):
    count = 0
    done = 0

    while True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(img, (100, 100), (width-100,height-100), (145,159,242), -1)

        cv2.putText(img, 'HIGHSCORE!!!', (150, 250), font, 3,(0, 0, 0),2,cv2.LINE_AA)
        cv2.putText(img, 'Enter your name:', (150, 450), font, 1.5,(0, 0, 0),2,cv2.LINE_AA)

        
        if len(leaderboard.highScores) < 5 and done == 0:
            for hscore in leaderboard.highScores:
                if hscore >= score:
                    count+=1
            done += 1
            leaderboard.highScores.insert(count, score)
            leaderboard.highScoreName.insert(count, name)
        elif len(leaderboard.highScores) < 5 and done == 0:
            if score > leaderboard.highScores[4] and done == 0:
                leaderboard.highscore = leaderboard.highScores[:4]
                for hscore in leaderboard.highScores:
                    if hscore >= score:
                        count+=1
                done += 1
                leaderboard.highScores.insert(count, score)
                leaderboard.highScoreName.insert(count, name)


        cv2.imshow('img', img)

        k = cv2.waitKey(1) & 0xFF

        if k == ord('h'):
            helpPage.drawHelp(img)

        if k == ord('c'):
            leaderboard.drawLeaderboard(leaderboard.highScores, leaderboard.highScoreName, count, img)

        if k == ord('r'):
            songSelection.drawSongSelection(img)

        if k == 27:
            cv2.destroyAllWindows() 


    
print('endPage')
cam.release()
cv2.destroyAllWindows() 
