# Importing all necessary libraries 
import cv2 
import os 
import threading
import time

def convert(vidfile, fpsdiv):
    # Read the video from specified path 
    cam = cv2.VideoCapture(vidfile) 

    # Get the total number of frames in the video
    total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))

    # frame 
    currentframe = 0

    while currentframe < total_frames: 
        # Set the frame position
        cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)

        # reading from frame 
        ret, frame = cam.read() 

        if ret: 
            # if video is still left continue creating images 
            name = './temp/vids/' + str(int(currentframe/fpsdiv)) + '.png'#converts 60 fps to 30 fps
            print('Creating...' + name) 

            # writing the extracted images 
            cv2.imwrite(name,frame)

            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += fpsdiv

        else: 
            break
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows() 
