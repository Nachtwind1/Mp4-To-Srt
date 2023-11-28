# Importing all necessary libraries 
import cv2 
from PIL import Image

def convert(vidfile, fpsdiv):
    # Read the video from specified path 
    cam = cv2.VideoCapture(vidfile) 

    # Get the total number of frames in the video
    total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))

    # frame 
    currentframe = 0

    frames = []

    while currentframe < total_frames: 
        # Set the frame position
        cam.set(cv2.CAP_PROP_POS_FRAMES, currentframe)

        # reading from frame 
        ret, frame = cam.read() 

        if ret: 
            frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))

            # increasing counter so that it will 
            # show how many frames are created 
            currentframe += fpsdiv

        else: 
            break
    # Release all space and windows once done 
    cam.release() 
    cv2.destroyAllWindows() 

    return frames
