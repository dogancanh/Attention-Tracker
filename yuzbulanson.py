import sys
import threading
from cv2 import cv2 as cv
import time
import queue
import time
import mysql.connector
import datetime
from datetime import timedelta


mydb=mysql.connector.connect(host='94.130.57.82',user="appsplat_semih",passwd="semihsemih123",database="appsplat_semih")
mycursor =mydb.cursor()


idnum=sys.argv[1]
course=sys.argv[2]

def att(q):


    sqlform = "Insert into attentionstudent(sessionID,userID,min,attentionP) values(%s,%s,NOW(),%s)"

    value = q.get()
    print('Average attention:',value)
    #formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    #print(formatted_date)
    dt = datetime.datetime.now()


    #x = dt.strftime("%Y-%m-%d %H:%M:%S")

    students=[(course,idnum,value)]

    mycursor.executemany(sqlform, students)
    mydb.commit()

    return q


def th():
    for _ in range(50):
        thread1 = threading.Thread(target=att, args=(q,))
        thread1.start()
        time.sleep(1)



if __name__ == '__main__':
    attention = 100
    cap = cv.VideoCapture(0)
    """q = queue.LifoQueue()
    Timer.Timer(10, att,[q]).start()"""
    #manager = multiprocessing.Manager()
    q = queue.LifoQueue()
    #p = Timer.Timer(10, att, [q])
    #p.start()
    #thread = threading.Thread(target=att, args=(q,))
    #thread.start()
    thread = threading.Thread(target=th)
    thread.start()
    while True:
        ret, frame = cap.read()
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        # -- Detect faces
        face_cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")
        eyes_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
        faces = face_cascade.detectMultiScale(frame_gray)
        if any(map(len, faces)):
            if attention < 96:
                attention += 5
        else:
            if attention > 9:
                attention -= 10
        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
            faceROI = frame_gray[y:y + h, x:x + w]
            # -- In each face, detect eyes
            eyes = eyes_cascade.detectMultiScale(faceROI)

            if any(map(len, eyes)):
                if attention < 98:
                    attention += 3
            else:
                if attention > 6:
                    attention -= 7

            for (x2, y2, w2, h2) in eyes:
                eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
                radius = int(round((w2 + h2) * 0.25))
                frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)

            q.put(attention)
        cv.imshow('Capture - Face detection', frame)

        if cv.waitKey(10) == 27:
            break
