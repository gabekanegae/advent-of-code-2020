######################################
# --- Day 3: Toboggan Trajectory --- #
######################################

import AOCUtils

def countTrees(forest, deltaW, deltaH):
    h, w = len(forest), len(forest[0])

    trees = 0

    curH, curW = 0, 0
    for curH in range(0, h, deltaH):
        trees += int(forest[curH][curW] == "#")

        curW = (curW + deltaW) % w

    return trees

######################################

forest = AOCUtils.loadInput(3)

p1 = countTrees(forest, 3, 1)

print("Part 1: {}".format(p1))

p2 = countTrees(forest, 1, 1)
p2 *= countTrees(forest, 3, 1)
p2 *= countTrees(forest, 5, 1)
p2 *= countTrees(forest, 7, 1)
p2 *= countTrees(forest, 1, 2)

print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()