from time import time
import os

_startTime = None

def loadInput(day):
    global _startTime

    day = str(day)
    filename = "input" + day.zfill(2) + ".txt"
    filepath = os.path.join("inputs", filename)

    with open(filepath) as f:
        content = [l.rstrip("\n") for l in f.readlines()]

    _startTime = time()

    if len(content) == 1:
        try:
            return int(content[0])
        except:
            try:
                return [int(i) for i in content[0].split()]
            except:
                return content[0]
    else:
        try:
            return [int(i) for i in content]
        except:
            return content

def printTimeTaken():
    global _startTime
    _endTime = time()
    
    print("Time: {:.3f}s".format(_endTime - _startTime))