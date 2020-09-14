from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("cut.wav", format="wav")
#cut = sound[:2*1000]
#cut.export("cut.wav", format="wav")
play(sound)
