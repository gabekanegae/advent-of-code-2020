##################################
# --- Day 5: Binary Boarding --- #
##################################

import AOCUtils

##################################

rawAnswers = AOCUtils.loadInput(6)

for i in range(len(rawAnswers)):
    if rawAnswers[i] == "": rawAnswers[i] = "\n"

rawGroups = " ".join(rawAnswers).split("\n")

groups = [[set(answer) for answer in rawGroup.split()] for rawGroup in rawGroups]

p1 = sum(len(set.union(*group)) for group in groups)
print("Part 1: {}".format(p1))

p2 = sum(len(set.intersection(*group)) for group in groups)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()