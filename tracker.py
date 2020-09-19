from os import listdir
import glob
import json

def load_track(filename:str):
    with open(filename) as f:
        operations = json.load(f)
        track = Tracker(filename)
        track.operations = operations
        return track

class Tracker:

    def __init__(self, name:str, sounds_dir:str = "sounds/*.wav", mode:str = "pitch"):
        self.name = name
        self.state = {}
        self.operations = []
        self.sounds = glob.glob(sounds_dir)
        self.sound_index = 0
        self.mode = mode

    def add(self, op: str, value, category: str=None):
        if not op in self.state:
            self.state[op] = {"octave": 1, "pos": 1000, "dur": 50, "value": value, "sound": self.sounds[self.sound_index]}
            self.sound_index += 1
            if self.sound_index >= len(self.sounds):
                self.sound_index = 0
        if self.mode == "pitch":
            if self.state[op]["value"] < value:
                self.state[op]["octave"] = self.state[op]["octave"] + .2
            elif self.state[op]["value"] > value:
                self.state[op]["octave"] = self.state[op]["octave"] - .2
            operation = {"type": self.mode, "octave": self.state[op]["octave"], "sound": self.state[op]["sound"]}
        elif self.mode == "slice":
            if self.state[op]["value"] < value:
                self.state[op]["pos"] = self.state[op]["pos"] - 2000
                self.state[op]["dur"] = self.state[op]["dur"] - 10
            elif self.state[op]["value"] > value:
                self.state[op]["pos"] = self.state[op]["pos"] + 2000
                self.state[op]["dur"] = self.state[op]["dur"] + 10
            else:
                self.state[op]["pos"] = self.state[op]["pos"] + 500
                self.state[op]["dur"] = self.state[op]["dur"] + 5
            operation = {"type": self.mode, "start": self.state[op]["pos"], 
                        "end": self.state[op]["pos"] + self.state[op]["dur"], "sound": self.state[op]["sound"]}
        self.state[op]["value"] = value
        self.operations.append(operation)

    def list(self):
        return self.operations

    def save(self, filename:str):
        with open(filename, 'w') as outfile:
            json.dump(self.operations, outfile, indent=2)
