from pydub import AudioSegment
from pydub.playback import play

def pitch(sound, octaves, multiplier=1.0):
    sample_rate = int(sound.frame_rate * (2.0 ** octaves) * multiplier)
    
    sound = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
    return sound.set_frame_rate(44100)

def get_track(operations):
    sounds = {}
    res = AudioSegment.silent(duration=10)
    for op in operations:
        if not op["sound"] in sounds:
            sounds[op["sound"]] = AudioSegment.from_file(op["sound"], format="wav")
        if op["type"] == "pitch":
            res = res.append(pitch(sounds[op["sound"]], op["octave"]), crossfade=0)
        if op["type"] == "slice":
            l = len(sounds[op["sound"]])
            start = op["start"] % l
            end = op["end"] % l
            if start > end:
                end = start + 50 % l
            sz = sounds[op["sound"]][start:end]
            res = res.append(sz, crossfade=0)

    return res
