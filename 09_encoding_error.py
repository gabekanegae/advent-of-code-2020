#################################
# --- Day 9: Encoding Error --- #
#################################

import AOCUtils
from itertools import combinations

#################################

data = AOCUtils.loadInput(9)

for i in range(25, len(data)):
    if data[i] not in [sum(l) for l in combinations(data[i-25:i], 2)]:
        p1 = data[i]
        break

print("Part 1: {}".format(p1))

i = 0
j = 1
cumSum = data[i]
while i < len(data):
    cumSum += data[j] # cumSum == sum(data[i:j+1])

    if cumSum == p1:
        p2 = min(data[i:j+1]) + max(data[i:j+1])
        break

    if cumSum > p1 or j == len(data) - 1:
        i += 1
        j = i
        cumSum = data[i]

    j += 1

print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()