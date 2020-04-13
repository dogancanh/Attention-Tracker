import cv2
import numpy as np
import os


class camera():

    def __init__(self, file, frame, res):
        self.filename = file
        self.frames_per_second = frame
        self.res = res

    # Set resolution for the video capture
    def change_res(cap, width, height):
        cap.set(3, width)
        cap.set(4, height)

    def get_dims(cap, res='1080p'):
        STD_DIMENSIONS = {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4k": (3840, 2160),
        }
        width, height = STD_DIMENSIONS["480p"]
        if res in STD_DIMENSIONS:
            width, height = STD_DIMENSIONS[res]
        ## change the current caputre device
        ## to the resulting resolution
        # change_res(cap, width, height)
        return cap.change_res(cap, width, height)

    def get_video_type(self,filename):
        VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID'),
         }
        filename, ext = os.path.splitext(filename)
        if ext in VIDEO_TYPE:
            return VIDEO_TYPE[ext]
        return VIDEO_TYPE['avi']

    def main(self):

        cap = cv2.VideoCapture(0)
        cap.set(3, int(self.res[0]))
        cap.set(4, int(self.res[1]))
        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        out = cv2.VideoWriter(self.filename, self.get_video_type(self.filename), self.frames_per_second,(int(w),int(h)))
        while True:
            ret, frame = cap.read()
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
