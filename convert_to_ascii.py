# Python code to convert an image to ASCII image.
import sys, random, argparse
import numpy as np
import math

from PIL import Image





# 10 levels of grey
gscale2 = '$8obdpq0Lun1+"`'
def id_to_time_format(id):
    # Calculate hours, minutes, seconds, and milliseconds
    hours = id // 3600000  # 1 hour = 3600 seconds * 1000 milliseconds
    id %= 3600000
    minutes = id // 60000  # 1 minute = 60 seconds * 1000 milliseconds
    id %= 60000
    seconds = id // 1000
    milliseconds = id % 1000

    # Format the time components as strings with leading zeros
    time_format = f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

    return time_format





def getAverageL(image):

	"""
	Given PIL Image, return average value of grayscale value
	"""
	# get image as numpy array
	im = np.array(image)

	# get shape
	w,h = im.shape

	# get average
	return np.average(im.reshape(w*h))

def getEqualWidthScale(scale, width):
    equal_width_scale = ""
    for char in scale:
        equal_width_scale += char + " " * (width - 1)
    return equal_width_scale

def convertImageToAscii(frame, cols, scale):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images 
    """
    # declare globals
    global gscale1, gscale2

    # open image and convert to grayscale
    image = frame.convert('L')

    # store dimensions
    W, H = image.size[0], image.size[1]
    #print("input image dims: %d x %d" % (W, H))

    # compute width of tile
    w = W / cols

    # compute tile height based on aspect ratio and scale
    h = w / scale

    # compute number of rows
    rows = int(H / h)

    #print("cols: %d, rows: %d" % (cols, rows))
    #print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    # ascii image is a list of character strings
    aimg = []

    # generate list of dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)

        # correct last tile
        if j == rows - 1:
            y2 = H

        # append an empty string
        aimg.append("")

        for i in range(cols):

            # crop image to tile
            x1 = int(i * w)
            x2 = int((i + 1) * w)

            # correct last tile
            if i == cols - 1:
                x2 = W

            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            # get average luminance
            avg = int(getAverageL(img))

            # look up ascii char
            gsval = gscale2[int(((255-avg) * 14) / 255)]
            if gsval == '"':
                gsval = '" '
            elif gsval == "`":
                gsval = "` "   
            # append ascii char to string
            aimg[j] += gsval

    # return txt image
    return aimg


# main() function
def convert(frame, frm,id,tfrm,clms):
	rtn = ""

	# set scale default as 0.43 which suits
	# a Courier font
	scale = 0.43

	# set cols
	#cols = 40 # 3:30 vids (Bad apple) if you upload your srt file and the subtitle doesn't appear its because the file is too big (5.5 i think is the max)
	#cols = 56 # 2:00 vids so use less columms if your file is too big
    #cols = 64 #max res
	if clms:
		cols = int(clms)
	else:
		print("ERROR"*1000)

	# convert image to ascii txt
	aimg = convertImageToAscii(frame, cols, scale)

	
	i = 0

	if tfrm == 2:
		frm = frm - 1
		efrm = frm + 34
	else:
		efrm = frm + 33
	rtn = f'{id+1}\n{id_to_time_format(frm)} --> {id_to_time_format(efrm)}'
	for row in aimg:
		rtn = rtn + "\n" +  row

	
	return rtn
