import PySimpleGUI as sg
import cv2
import os
#ecvdekal


def pypy480():
    os.system('python record-video-480.py')

def pypy720():
    os.system('python record-video-720.py')

def pypy1080():
    os.system('python record-video-1080.py')

# define the window layout
layout = [
           [sg.SimpleButton('480', size=(8,1)),
          sg.SimpleButton('720', size=(8, 1)),
          sg.SimpleButton('1080', size=(8, 1))],
          ]
window = sg.Window('Demo Application-Opencv Integration', layout, location=(800, 400))

while True:
    event, values = window.Read()      # get events for the window with 20ms max wait
    if event=='480':
        pypy480()
    if event=='720':
        pypy720()
    if event=='1080':
        pypy1080()

window.read()
