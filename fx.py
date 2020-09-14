from pydub import AudioSegment
from pydub.playback import play

def pitch(sound, octaves, multiplier=1.0):
    sample_rate = int(sound.frame_rate * (2.0 ** octaves) * multiplier)
    
    sound = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_rate})
    return sound.set_frame_rate(44100)
