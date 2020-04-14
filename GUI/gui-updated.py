import PySimpleGUI as sg
import cv2
from camera import camera
from cam2 import camera2

# define the window layout
layout = [
            [sg.Text('Name', size=(10, 1)), sg.InputText()],
            [sg.Text('Surname', size=(10, 1)), sg.InputText()],
            [sg.Text('Lecture', size=(10, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()],
            [sg.SimpleButton('480', size=(8,1)),
             sg.SimpleButton('720', size=(8, 1)),
             sg.SimpleButton('1080', size=(8, 1)),
             sg.SimpleButton('Extract',size=(8,1)),
             ],
        ]
window = sg.Window('Demo Application-Opencv Integration', layout, location=(800, 400))

while True:
    event, values = window.Read()      # get events for the window with 20ms max wait
    if event == '480':
        a = camera('video480.avi', 10.0, (640, 480))
        a.main()
        break

    if event == '720':
        a = camera('video720.avi', 10.0, (1280, 720))
        a.main()
        break
    if event == '1080':
        a = camera('video1080.avi', 10.0, (1920, 1080))
        a.main()
        break
    if event =='Extract':
        a = camera2()
        a.main()
        print('files are saved')
        break

window.read()


