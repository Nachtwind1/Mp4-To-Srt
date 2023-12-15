# Mp4-To-Srt
A Python Programm That Converts Mp4 files to Srt files

# How to use

## Requirements

python3, opencv and numpy

### How to install

#### [Python](https://www.python.org/downloads/)

if you have python setup do

#### pip install opencv-python
#### pip install  numpy
#### pip install Pillow

## Example

#### python3 main.py --file "./Bad Apple.mp4" --collums 40 --msoffset 0 --idoffset 0

## What do The Arguments mean

|Argument|Rquired|Description|
|----|-----|-------|
|--file|Yes|Your input mp4 file|
|--collums|Yes|How many characters Per Row|
|--msoffset|No|After How many milliseconds should the animation start|
|--idoffset|No|At which subtitle id should it start|
|--submsoffset|No|at which milisecond the subtitles start|
