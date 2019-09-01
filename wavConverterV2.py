import wave

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()

dacSize = int(input("Dac size in bits:"))
samplingRate = int(input("Target sampling rate (probably 11025):"))
size = int(input("How much of the song do you want (if you want 1/10 type 10 if you want want 1/5 type 5 etc) :"))


song = wave.open(filename)


comp = song.getcomptype()
framerate = song.getframerate()
bytedepth = song.getsampwidth()
length = song.getnframes()

print(framerate)

if(bytedepth != 2):
    raise Exception("Bit depth is not 16")

rateScale = framerate // samplingRate
bitScale = (2**(bytedepth * 8) // (2**(dacSize)))

if(bitScale < 1):
    raise Exception("Dac")

dataArray = []

for x in range(0,length // rateScale // size):
    frame = song.readframes(1)

    value = int.from_bytes(frame[0:bytedepth], byteorder='little', signed=True)
    print(value)

    smallestVal = (2 ** (bytedepth * 8)) // 2
    value = value + smallestVal
    dataArray.append(value // bitScale)

    if(rateScale > 1):
        song.readframes(rateScale - 1)






dir =  filename.split("/")
del(dir[-1])

dir= "/".join(dir)
print(dir)

id = filename.split("/")[-1].split(".")[0]
name = "/Converted" + id + ".txt"
name = dir + name
print(name)

with open(name, 'w') as f:
    f.write("const uint8_t "+ id +"["+str(len(dataArray)) + "] = {")
    for item in dataArray:
        f.write("%s ," % item)
    f.write("};")

