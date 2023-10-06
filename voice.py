import sounddevice as sound

from scipy.io.wavfile import write


freq = 44100

duration = 12

recording = sound.rec(int(duration*freq), samplerate = freq, channels = 2)

sound.wait()

write("my_wav.wav", freq, recording)


