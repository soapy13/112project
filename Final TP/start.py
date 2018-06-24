#runs the homescreen and starts the game

#structure influenced by code from https://people.csail.mit.edu/hubert/pyaudio/docs/

import kthread
import pyaudio
import wave 
import cv2
import time
import helpPage
import songSelection


cam = cv2.VideoCapture(0)

width = 1300
height = 750

click = []
count = 0

def startScreenAudio():
    time.sleep(1.5)

    #define stream chunk   
    chunk = 1024  

    #open a wav format music  
    f = wave.open(r"Disfigure-Blank.wav","rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)
        


    #stop stream
    stream.stop_stream()  
    stream.close()

    #close PyAudio  
    p.terminate()  
####################################################################

sa = kthread.KThread(target=startScreenAudio, args=())
sa.start()

while(1):
    _, img = cam.read()
    img = cv2.flip(img,1)
    img = cv2.resize(img, (width, height))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'HANDS HANDS',(int(width/2-429), int(height/2-84)), font, 4,(0,0,0),4,cv2.LINE_AA)
    cv2.putText(img,'HANDS HANDS',(int(width/2-425), int(height/2-80)), font, 4,(255,255,255),4,cv2.LINE_AA)
    cv2.putText(img,'HANDS HANDS',(int(width/2-421), int(height/2-76)), font, 4,(255,215,144),4,cv2.LINE_AA)
    cv2.putText(img,'REVOLUTION',(int(width/2-354), int(height/2+16)), font, 4,(0,0,0),4,cv2.LINE_AA)
    cv2.putText(img,'REVOLUTION',(int(width/2-350), int(height/2+20)), font, 4,(255,255,255),4,cv2.LINE_AA)
    cv2.putText(img,'REVOLUTION',(int(width/2-346), int(height/2+24)), font, 4,(255,215,144),4,cv2.LINE_AA)

    cv2.putText(img,'Press "h" for help',(width-350,110), font, 1,(145,159,242), 2,cv2.LINE_AA)

    cv2.putText(img,'https://www.youtube.com/user/DisfigureMusic',(int(width-430), int(height-60)), font, 0.5,(255,215,144),1,cv2.LINE_AA)
    cv2.putText(img,'https://www.youtube.com/watch?v=p7ZsBPK656s',(int(width-430), int(height-35)), font, 0.5,(255,215,144),1,cv2.LINE_AA)
    cv2.putText(img,'Disfigure - Blank [NCS Release]',(int(width-430), int(height-10)), font, 0.5,(255,215,144),1,cv2.LINE_AA)

    if count//10 % 2 == 0:
        cv2.putText(img,'Press "s" to',(int(width/2-150), int(height/2+110)), font, 1.5,(138, 247, 165),4,cv2.LINE_AA)
        cv2.putText(img,'START',(int(width/2-125), int(height/2+200)), font, 2.5,(247, 192, 138),4,cv2.LINE_AA)
    else:
        cv2.putText(img,'Press "s" to',(int(width/2-150), int(height/2+110)), font, 1.5,(247, 192, 138),4,cv2.LINE_AA)
        cv2.putText(img,'START',(int(width/2-125), int(height/2+200)), font, 2.5,(138, 247, 165),4,cv2.LINE_AA)

    
    count += 1

    cv2.imshow('img', img)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('h'):
        helpPage.drawHelp(img)

    if k == ord('s'):
        #music wont stop playing when main page starts
        sa.kill()
        songSelection.drawSongSelection(img)

    if k == ord('q') or k == 27:
        sa.kill()
        break

cam.release()
cv2.destroyAllWindows() 
        
 
















