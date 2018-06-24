#runs the actual game itself

import numpy as np
import cv2
import backaudio
import kthread
from collections import deque
import argparse
import imutils
import time
import endPage
from random import randint
import beatdetection
import leaderboard

'''def compute_score(scores, increment, streak_length):
    if streak_length <= 0 or len(scores) <= 2 or len(scores) > 6 or streak_length <= 0:

        return increment 

    print(scores)

    output = int(0.1 * scores[len(scores) - 1] + compute_score(scores[0 : len(scores) - 2], increment, streak_length - 1)) + increment
    
    return output'''


def run(filename, mode):
    beatdetection.runBeatDetection(filename, mode)

    cam = cv2.VideoCapture(0)

    width = 1300
    height = 750


    totalScore = 0

    increment = 10
    hit = 0
    startTime = time.time()
    shown = ''
    kept = 0
    numTimes = 0

    ################code modified from https://pastebin.com/WVhfmphS#################
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video",
        help="path to the (optional) video file")
    ap.add_argument("-b", "--buffer", type=int, default=64,
        help="max buffer size")
    args = vars(ap.parse_args())
     
    # define the lower and upper boundaries of the colors in the HSV color space
    lower = {'red':(166, 84, 141),'blue':(97, 100, 117)}
    upper = {'red':(186,255,255), 'blue':(117,255,255)}
     
    # define standard colors for circle around the object
    colors = {'red':(0,0,255), 'blue':(255,0,0)}
    #############################################################################




    #maybe try to add sound effects everytime they get a note/miss
    def scoreboard(score, hit, shown, increment, kept):
        font = cv2.FONT_HERSHEY_SIMPLEX

        if shown == 'NICE':
            cv2.putText(img,shown,(int(width/2-125), int(height/2+150)), font, 2.5,(138, 247, 165),4,cv2.LINE_AA)
        else:
            cv2.putText(img,shown,(int(width/2-125), int(height/2+150)), font, 2.5,(0, 0, 0),4,cv2.LINE_AA)

        if time.time() - kept == 1.5:
            shown = ''

        if hit >= 3:
            cv2.putText(img, "Streak:  " + str(hit),(int(width/2-225), int(height/2+70)), font, 2.5,(255, 102, 153),4,cv2.LINE_AA)


        cv2.putText(img,str(score),(int(width/2-85), int(height/2+297)), font, 2.5,(255,255,255),4,cv2.LINE_AA)
        cv2.putText(img,str(score),(int(width/2-82), int(height/2+300)), font, 2.5,(255,215,144),4,cv2.LINE_AA)
        cv2.putText(img,'Press "e" to end the game',(int(width-470), int(height-35)), font, 1,(255,215,144),2,cv2.LINE_AA)



    class Circle():
        def __init__(self, x, y, color, thickness, radius=63, mark=False):
            self.x = x
            self.y = y
            self.color = color
            self.thickness = thickness
            self.radius = radius
            self.mark = mark

        def move(self):
            self.y -= 10

        def draw(self):
            cv2.circle(img,(self.x, self.y), self.radius, self.color, self.thickness)

        def collision(self, base, ballx, bally):
            if self.mark == False:
                if (base.x - self.x) ** 2 + (base.y - self.y) ** 2 <= self.radius ** 2 and (ballx - self.x) ** 2 + (bally - self.y) ** 2 <= self.radius ** 2:
                    self.mark = True
                    return True
            return False



    beatColors = {0:(0,0,255), 1:(255,0,255), 2:(0,255,255), 3:(255,255,0)}
    horiz = {0:int(width/5), 1:int(2*width/5), 2:int(3*width/5), 3:int(4*width/5)}


    base = []
    base.append(Circle(int(width/5), 70, (0,0,255), 5))
    base.append(Circle(int(2*width/5), 70, (255,0,255), 5))
    base.append(Circle(int(3*width/5), 70, (0,255,255), 5))
    base.append(Circle(int(4*width/5), 70, (255,255,0), 5))

    beats = []

    print(filename)
    w = kthread.KThread(target=backaudio.playAudio, args=(filename, ))
    w.start()


    while(1):

        _, img = cam.read()
        img = cv2.flip(img,1)
        img = cv2.resize(img, (width, height))

    ################code modified from https://pastebin.com/WVhfmphS#####################
        # blur it, and convert it to the HSV
        # color space
     
        blurred = cv2.GaussianBlur(img, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        #for each color in dictionary check object in img
        for key, value in upper.items():
            # construct a mask for the color from dictionary`1, then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            kernel = np.ones((9,9),np.uint8)
            mask = cv2.inRange(hsv, lower[key], upper[key])
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                   
            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None
           
            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((ballx, bally), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
           
                # only proceed if the radius meets a minimum size. Correct this value for your obect's size
                if radius > 0.5:
                    # draw the circle and centroid on the img,
                    # then update the list of tracked points
                    cv2.circle(img, (int(ballx), int(bally)), int(radius), colors[key], 2)


    #################################################################################


                    for beat in beats:
                        for circle in base:
                            if beat.collision(circle, ballx, bally):
                                shown = 'NICE'
                                totalScore += increment
                                hit += 1


        for circle in base:
            circle.draw()

        for beat in beats:
            beat.draw()
            beat.move()
            if beat.y <= 70:
                if not beat.mark:
                    hit = 0
                    increment = 10
                    shown = 'MISS'
                beats.remove(beat)

        songTime = float('%.2f' % (time.time() - startTime))
        # print(songTime)

        for btime in beatdetection.beatTime:
            if songTime-0.03<=btime<=songTime+0.03:
                ind = randint(0,3)
                newCirc = Circle(horiz[ind], height-63, beatColors[ind], -1)
                beats.insert(0, newCirc)
            if songTime > beatdetection.beatTime[len(beatdetection.beatTime)-1] + 3:
                endPage.drawEnd(totalScore, img)

        if hit%10 == 0 and hit > 0 and numTimes == 0:
            increment *= 1.3
            increment = int(increment)
            numTimes += 1
        elif hit%10 != 0:
            numTimes = 0



        scoreboard(totalScore, hit, shown, increment, kept)
        
        cv2.imshow('img', img)

        key = cv2.waitKey(1) & 0xFF
        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            cam.release()
            cv2.destroyAllWindows()

        if key == ord("e"):
            w.kill()
            beatdetection.beatTime = []
            if len(leaderboard.highScores) < 5 or totalScore > leaderboard.highScores[4]:
                font = cv2.FONT_HERSHEY_SIMPLEX
                print("HIGHSCORE")
                cv2.rectangle(img, (100, 100), (width-100,height-100), (145,159,242), -1)
                cv2.putText(img, 'HIGHSCORE!!!', (150, 250), font, 3,(0, 0, 0),2,cv2.LINE_AA)
                cv2.putText(img, 'Enter your name:', (150, 450), font, 1.5,(0, 0, 0),2,cv2.LINE_AA)
                cv2.imshow('img', img)
                time.sleep(1)
                name = input('Your Name:   ')
            endPage.drawEnd(totalScore, img, name)
     

    














