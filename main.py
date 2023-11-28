import convert_to_ascii
import convert_to_png
import os
import argparse
#our subtitles string
srt = ""
parser = argparse.ArgumentParser(description="mp4 to srt")
# add expected arguments
parser.add_argument('--file', dest='file', required=True)
parser.add_argument('--inputfps', dest='fps', required=True)
parser.add_argument('--collums', dest='collums', required=True)
parser.add_argument('--msoffset', dest='msoffset', required=False)
parser.add_argument('--idoffset', dest='idoffset', required=False)
args = parser.parse_args()
if args.file != "":
    file = args.file
else:
    print("no file")
    exit()

if args.fps != "":
    if int(args.fps) % 30 == 0:
        fps = int(args.fps)#your fps (only works with 30 60 90 120...) output is always 30 fps
    else:
        print("you can only use 30, 60, 90, ... fps")
        exit()
else:
        print("you need to set an fps")
        exit()


fpsdiv = fps / 30
#Janky Code
files = 0
if os.path.exists(file):
    frames = convert_to_png.convert(file,fpsdiv)
else:
    print("found no file at that location")
    exit()

id = 0
if args.idoffset != "":
    idoffset = args.idoffset
else:
    idoffset = 0
if args.msoffset != "":
    milisecondsoffset = args.msoffset
else:
    milisecondsoffset = 0
frm = 1
print('Generating Ascii art')
for x in range(len(frames)):
    srt = srt + "\n" + convert_to_ascii.convert(frames[x],int(id+int(milisecondsoffset)),int(x + int(idoffset)),frm,args.collums) + "\n"
    frm += 1
    # 33.333333 milliseconds would be a frame so every third frame we make it 34 ms (33+33+34=100)
    if frm == 3:
        frm = 0
    if frm == 2:
        id += 34
    else:
        id += 33
#write to file
open("output/subtitles.srt","w").write(srt)





#remove all temporary files
id = 0
while(True):
    if (os.path.exists(f'temp/vids/{id}.png')):
        os.remove(f'temp/vids/{id}.png')
    else:
        break
    id += 1
