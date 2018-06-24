#returns a list of numbers that represents the beats int he song

#https://github.com/aubio/aubio/blob/master/python/demos/demo_tempo.py
#! /usr/bin/env python
from main import *
import sys
from aubio import tempo, source
import time, copy

beatTime = []

def runBeatDetection(filename, mode):
    win_s = 512                 # fft size
    hop_s = win_s // 2          # hop size


    samplerate = 44100


    s = source(filename, samplerate, hop_s)
    samplerate = s.samplerate
    o = tempo("default", win_s, hop_s, samplerate)

    # tempo detection delay, in samples
    # default to 4 blocks delay to catch up with
    delay = 4. * hop_s

    # list of beats, in samples
    totalbeats = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            this_beat = int(total_frames - delay + is_beat[0] * hop_s)
            timeOfBeat = "%.2f" % (this_beat / float(samplerate))
            print(timeOfBeat)
            totalbeats.append(float(timeOfBeat))
        total_frames += read
        if read < hop_s: break


    for i in range(len(totalbeats)):
        if mode == 'e':
            if i % 3 == 0:
                beatTime.append(totalbeats[i])
        elif mode == 'm':
            if i % 2 == 0:
                beatTime.append(totalbeats[i])
        elif mode == 'h':
            if i % 1 == 0:
                beatTime.append(totalbeats[i])









