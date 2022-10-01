import sounddevice
from scipy.io.wavfile import write

fs = 44100

secend = int(input("enter the time duration in secend : "))


rec_voice = sounddevice.rec(int(secend * fs), samplerate= fs, channels = 2)

sounddevice.wait()

write("C:\\Users\\Administrator\\Desktop\\My code\\PYTHON\\simple project\\voice recorder\\this voice\\my_voice.wav", fs, rec_voice)


print("finished")
