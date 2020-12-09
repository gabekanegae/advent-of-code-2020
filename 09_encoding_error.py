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
while i < len(data):
    total = sum(data[i:j])

    if total == p1:
        p2 = min(data[i:j]) + max(data[i:j])
        break

    if j == len(data) - 1 or total > p1:
        i += 1
        j = i

    j += 1

print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()