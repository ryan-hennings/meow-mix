from pydub import AudioSegment
from pydub.playback import play
from fx import pitch
from alg import mergeSort

cut = AudioSegment.from_file("sounds/aaron.wav")
play(cut)