# Mp4-To-Srt
A Python Programm That Converts Mp4 files to Srt files

# How to use

## Requirements

python3, opencv and numpy

### How to install

#### [Python](https://www.python.org/downloads/)

if you have python setup do

#### pip install opencv, numpy

## Example

#### python3 main.py --file "./Bad Apple.mp4" --inputfps 30 --collums 40 --msoffset 0 --idoffset 0

## What do The Arguments mean

|Argument|Rquired|Description|
|----|-----|-------|
|--file|Yes|Your input mp4 file|
|--inputfps|Yes|The fps of your input Video (it only works for 30, 60, 90...)|
|--collums|Yes|How many characters Per Row|
|--msoffset|No|After How many milliseconds should the animation start|
|--idoffset|No|At which subtitle id should it start|
