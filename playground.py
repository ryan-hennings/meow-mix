from tracker import Tracker
from pydub import AudioSegment
from pydub.playback import play
import fx

song = Tracker("bingo")

# song.add("cat", 1)
# song.add("cat", 2)
# song.add("cat", 1)

song.add("cat", 1)
song.add("cat", 1)
song.add("bill", 1)
song.add("cat", 0)

song.add("cat", 1)
song.add("cat", 1)
song.add("bill", 1)
song.add("cat", 0)

song.add("cat", 0)
song.add("bill", 1)
song.add("cat", 1)
song.add("dog", 0)
song.add("cat", 1)
song.add("bill", 1)


# song.add("cat", -1)
# song.add("cat", -1)
# song.add("bill", -1)
# song.add("cat", 0)

# song.add("cat", 1)
# song.add("cat", 1)
# song.add("bill", 1)
# song.add("cat", 0)
print(song.list())

track = fx.get_track(song.operations)
play(track)
