from pydub import AudioSegment
from pydub.playback import play
from fx import pitch
from alg import mergeSort

cut = AudioSegment.from_file("sounds/perc-g.wav", format="wav")

cut = cut[:200]
res = cut

for ix in range(10):
    res = res.append(pitch(cut, ix+1), crossfade=0)
for ix in range(10, 0, -1):
    res = res.append(pitch(cut, ix / 4.0), crossfade=1)
for ix in range(18):
    res = res.append(pitch(cut, ix / 4.0), crossfade=1)
for ix in range(16):
    res = res.append(pitch(cut, (16 - ix) / 2.0), crossfade=1)

res = res.overlay(pitch(res, 1.2, .2), 100)

play(res)

#cut.export("cut.wav", format="wav")
