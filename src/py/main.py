import os.path
import wave
import random
from pydub import AudioSegment

path = input("Enter your file Path (You can drag & drop your file): ")
if path.startswith('"'):
    path = path[1:]
if path.endswith('"'):
    path = path[:-1]

spacer = int(input("Enter the Number of Seconds you would like to hear the Sound on average in: "))

importedTrack = wave.open(path, "rb")                 # reads the Track that should be imported

nchannels = importedTrack.getnchannels()  # output section for params
sampwidth = importedTrack.getsampwidth()
framerate = importedTrack.getframerate()
nframes = importedTrack.getnframes()
params = importedTrack.getparams()
frames = importedTrack.readframes(-1)

importedTrack.close()


silence = wave.open("silence.wav", "rb")

silentframes = silence.readframes(-1)


exportedTrack = wave.open("temp.wav", "wb")               # sets up binary writings for output file

exportedTrack.setnchannels(nchannels)
exportedTrack.setsampwidth(sampwidth)
exportedTrack.setframerate(framerate)

while exportedTrack.getnframes()<(3600 * framerate):

    exportedTrack.writeframes(frames)
    looper=0
    while looper<random.randint(0, 140 * spacer):
        exportedTrack.writeframes(silentframes)
        looper+=1

exportedTrack.close()

outputpath=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/output.mp3')

AudioSegment.from_wav("temp.wav").export(outputpath,format="mp3")

os.remove("temp.wav")