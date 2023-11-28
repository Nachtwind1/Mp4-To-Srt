# Importing all necessary libraries 
import cv2 
from PIL import Image

# function to print an in-place progress bar (doesn't spam terminal and looks very clean)
def print_progress_bar(iteration, total):
    percent = "{:.1f}".format(100 * (iteration / float(total)))
    progress = f"Progress: {iteration}/{total} - {percent}%"
    print(progress, end='\r', flush=True)

def convert(vidfile, startms, idoffset):
    frames = []

    cam = cv2.VideoCapture(vidfile)
    fps = cam.get(cv2.CAP_PROP_FPS)
    ms_per_frame = 1000 / fps

    cam.set(cv2.CAP_PROP_POS_MSEC, startms + idoffset * ms_per_frame)

    pos_after_offset = int(cam.get(cv2.CAP_PROP_POS_FRAMES))
    total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) - pos_after_offset

    print('Extracting Frames...')
    while True:
        frame_num = int(cam.get(cv2.CAP_PROP_POS_FRAMES)) - pos_after_offset
        print_progress_bar(frame_num, total_frames)

        ret, frame = cam.read()
        if not ret: break
        frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
    print()

    cam.release()

    return ms_per_frame, len(frames), frames