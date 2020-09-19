from tracker import Tracker
from pydub import AudioSegment
from pydub.playback import play
import fx
import alg

song = Tracker("bingo", "sounds3/*.wav", "slice")

# song.add("cat", 1)
# song.add("cat", 2)
# song.add("cat", 1)

# song.add("cat", 1)
# song.add("cat", 1)
# song.add("bill", 1)
# song.add("cat", 0)

# song.add("cat", 1)
# song.add("cat", 1)
# song.add("bill", 1)
# song.add("cat", 0)

# song.add("cat", 0)
# song.add("bill", 1)
# song.add("cat", 1)
# song.add("dog", 0)
# song.add("cat", 1)
# song.add("bill", 1)


# song.add("cat", -1)
# song.add("cat", -1)
# song.add("bill", -1)
# song.add("cat", 0)

# song.add("cat", 1)
# song.add("cat", 1)
# song.add("bill", 1)
# song.add("cat", 0)
#print(song.list())

#track = fx.get_track(song.operations)

arr = [12, 11, 13, 5, 6, 7, 55, 1, 19, 2, 4334, 12, 11, 13, 5, 6, 7, 55, 1, 19, 2, 4334, 12, 11, 13, 5, 6, 7, 55, 1, 19, 2, 4334] 
n = len(arr) 
alg.mergeSort(arr,0,n-1, song) 
#alg.bubbleSort(arr, song)
song.save("tracks/t4.track")
track = fx.get_track(song.operations)
play(track)
