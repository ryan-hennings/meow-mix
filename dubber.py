from pydub import AudioSegment
from pydub.playback import play

def pitch(sound, octaves):
    sample_rate = int(sound.frame_rate * (2.0 ** octaves))
    sound = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
    return sound.set_frame_rate(44100)

cut = AudioSegment.from_file("sounds/perc-g.wav", format="wav")

cut = cut[:200]

res = cut
for ix in range(10):
    res = res.append(pitch(cut, ix+1), crossfade=0)
for ix in range(8):
    res = res.append(pitch(cut, ix / 4.0), crossfade=1)
for ix in range(16):
    res = res.append(pitch(cut, (16 - ix) / 2.0), crossfade=1)

play(res)

#cut.export("cut.wav", format="wav")
