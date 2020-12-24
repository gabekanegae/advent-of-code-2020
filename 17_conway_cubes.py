################################
# --- Day 17: Conway Cubes --- #
################################

import AOCUtils
from itertools import combinations

# Assume dimensions >= 2
def conwayCubes(rawGrid, dimensions, cycles=6):
    allMoves = set(list(combinations([-1, 0, 1]*dimensions, dimensions)))
    nullMove = set([tuple([0]*dimensions)])
    moves = list(allMoves - nullMove)

    active = set()
    for x in range(len(rawGrid)):
        for y in range(len(rawGrid[0])):
            if rawGrid[x][y] == "#":
                pos = tuple([x, y] + [0]*(dimensions - 2))
                active.add(pos)

    for cycle in range(cycles):
        toBeUpdated = set(active)
        for pos in active:
            for delta in moves:
                neighbor = tuple(k+d for k, d in zip(pos, delta))
                toBeUpdated.add(neighbor)

        newActive = set(active)
        for pos in toBeUpdated:
            neighbors = 0
            for delta in moves:
                neighbor = tuple(k+d for k, d in zip(pos, delta))
                neighbors += int(neighbor in active)

            if pos in active and neighbors not in [2, 3]:
                newActive.remove(pos)
            elif pos not in active and neighbors == 3:
                newActive.add(pos)

        active = newActive

    return len(active)

################################

rawGrid = AOCUtils.loadInput(17)

print("Part 1: {}".format(conwayCubes(rawGrid, 3)))

print("Part 2: {}".format(conwayCubes(rawGrid, 4)))

AOCUtils.printTimeTaken()