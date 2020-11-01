## 11/01/2020 - Turtle Audio Plotter - Pink
import turtle
import sys
import os
import librosa as lib
import numpy as np

## A class to open MP3 Audio with Librosa
class librosaOpen():

    ''' A class for librosa methods '''

    def __init__(self, fn=""):
        
        ''' A init method for librosa methods '''
        
        self.filename = fn

    def openAudio(self):
        
        ''' A method for opening audio for plotting '''

        print("DRAWING - " + str(self.filename))
        sr = lib.get_samplerate(self.filename)
        audio = lib.load(str(self.filename), sr=int(sr), mono=False, offset=0.0, duration=None, dtype=np.float32)
        ch1 = np.ndarray.tolist(audio[0][0])
        ch2 = np.ndarray.tolist(audio[0][1])
        td = turtleDraw()
        td.ch1 = ch1
        td.ch2 = ch2
        td.draw()

## A class to draw opened MP3 files with Turtle
class turtleDraw():

    def __init__(self, ch1=[], ch2=[]):
    
        ''' A init method for turtleDraw methods '''
    
        self.ch1 = ch1
        self.ch2 = ch2

    def draw(self):
        t = turtle.Turtle()
        turtle.bgcolor("black")
        t.speed(99999999999999999999999999999999999)

        for n in self.ch1:
            for v in self.ch2:

                t.pencolor("magenta")
                t.forward(n*000000)
                t.right(n*1000000)
                t.forward(n*1000000)
                t.left(n*1000000)
                t.forward(n*1000000)
                t.right(n*1000000)
                t.penup()
                t.setposition(0, 0)
                t.pendown()
                t.right(n*1000000)

                t.pencolor("blue")
                t.forward(v*1000000)
                t.right(v*1000000)
                t.forward(v*1000000)
                t.left(v*1000000)
                t.forward(v*1000000)
                t.right(v*1000000)
                t.penup()
                t.setposition(0, 0)
                t.pendown()
                t.right(v*1000000)

        turtle.done()

ro = librosaOpen()

## Walk each directory looking for MP3 files and attempt to plot them
for r, d, f in os.walk(".", topdown=False):
    for i in f:
        if i.endswith(".mp3"):
            fn = os.path.join(r, i)
            try:
                ro.filename = fn
                ro.openAudio()

            except:
                pass


