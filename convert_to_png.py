# Importing all necessary libraries 
import cv2 
from PIL import Image

def print_progress_bar(iteration, total):
    percent = "{:.1f}".format(100 * (iteration / float(total)))
    progress = f"Progress: {iteration}/{total} - {percent}%"
    print(progress, end='\r', flush=True)

def convert(vidfile, startms):
    frames = []

    cam = cv2.VideoCapture(vidfile)
    fps = cam.get(cv2.CAP_PROP_FPS)
    total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))

    cam.set(cv2.CAP_PROP_POS_MSEC, startms)

    print('Extracting Frames...')
    while True:
        frame_num = int(cam.get(cv2.CAP_PROP_POS_FRAMES))
        print_progress_bar(frame_num, total_frames)

        ret, frame = cam.read()
        if not ret: break
        frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))

    cam.release()

    return fps, total_frames, frames