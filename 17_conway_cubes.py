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

    grid = dict()
    for x in range(len(rawGrid)):
        for y in range(len(rawGrid[0])):
            key = tuple([x, y] + [0]*(dimensions - 2))
            grid[key] = rawGrid[x][y]

    for cycle in range(cycles):
        # Create one more layer on grid
        for key in list(grid.keys()):
            for delta in moves:
                deltaKey = tuple(k+d for k, d in zip(key, delta))
                if deltaKey not in grid:
                    grid[deltaKey] = "."

        # Deepcopy grid
        newGrid = dict()
        for key, cube in grid.items():
            newGrid[key] = cube

        # Update grid
        for key in grid:
            neighbors = 0
            for delta in moves:
                deltaKey = tuple(k+d for k, d in zip(key, delta))
                if deltaKey in grid and grid[deltaKey] == "#":
                    neighbors += 1

            if grid[key] == "#" and neighbors not in [2, 3]:
                newGrid[key] = "."
            elif grid[key] == "." and neighbors == 3:
                newGrid[key] = "#"

        grid = newGrid

    return list(grid.values()).count("#")

################################

rawGrid = AOCUtils.loadInput(17)

print("Part 1: {}".format(conwayCubes(rawGrid, 3)))

print("Part 2: {}".format(conwayCubes(rawGrid, 4)))

AOCUtils.printTimeTaken()