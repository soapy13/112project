#plays background audio
#structure influenced by code from https://people.csail.mit.edu/hubert/pyaudio/docs/
import time
import pyaudio
import wave 


def playAudio(filename):
    time.sleep(1.5)

    #define stream chunk   
    chunk = 1024  

    #open a wav format music  
    f = wave.open(filename,"rb")  
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
              
    #stop stream  .
    stream.stop_stream()  
    stream.close()

    #close PyAudio  
    p.terminate()  
