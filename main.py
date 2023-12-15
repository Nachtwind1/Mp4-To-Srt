import convert_to_ascii
import convert_to_png
import os
import argparse

parser = argparse.ArgumentParser(description="mp4 to srt")

# add expected arguments
parser.add_argument('--file', dest='file', required=True)
parser.add_argument('--collums', dest='collums', required=True)
parser.add_argument('--msoffset', dest='msoffset', required=False)
parser.add_argument('--submsoffset', dest='submsoffset', required=False)
parser.add_argument('--idoffset', dest='idoffset', required=False)

args = parser.parse_args()
if args.file != "":
    file = args.file
else:
    print("no file")
    exit()

#Janky Code

# Use given if it is Truthy, 0 if it is Falsey (empty string)
idoffset = int(args.idoffset or 0)
milisecondsoffset = int(args.msoffset or 0)

submilisecondoffset = int(args.submsoffset or 0)


if os.path.exists(file):
    ms_per_frame, total_frames, frames = convert_to_png.convert(file, milisecondsoffset, idoffset)
else:
    print("found no file at that location")
    exit()

srt = []
print('Generating Ascii art')
for x in range(total_frames):
    convert_to_png.print_progress_bar(x + 1, total_frames)

    srt.append(convert_to_ascii.convert(frames[x], x, ms_per_frame, args.collums, submilisecondoffset))

print()

#write to file
open("output/subtitles.srt","w").write("\n".join(srt))
