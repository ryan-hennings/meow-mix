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

    def __init__(self, name):
        self.name = name
        self.state = {}
        self.operations = []
        self.sounds = glob.glob("sounds2/*.wav")
        self.sound_index = 0

    def add(self, op: str, value, category: str=None):
        if not op in self.state:
            self.state[op] = {"octave": 1, "value": value, "sound": self.sounds[self.sound_index]}
            self.sound_index += 1
            if self.sound_index >= len(self.sounds):
                self.sound_index = 0
        if self.state[op]["value"] < value:
            self.state[op]["octave"] = self.state[op]["octave"] + .2 * 100
        elif self.state[op]["value"] > value:
            self.state[op]["octave"] = self.state[op]["octave"] - .2 * 100
        self.state[op]["value"] = value
        #operation = {"type": "pitch", "octave": self.state[op]["octave"], "sound": self.state[op]["sound"]}
        operation = {"type": "slice", "start": self.state[op]["octave"]*100, "end": self.state[op]["octave"]*1000, "sound": self.state[op]["sound"]}
        self.operations.append(operation)

    def list(self):
        return self.operations

    def save(self, filename:str):
        with open(filename, 'w') as outfile:
            json.dump(self.operations, outfile, indent=2)
