###################################
# --- Day 20: Jurassic Jigsaw --- #
###################################

import AOCUtils
from collections import deque

class Tile:
    def __init__(self, tileID, image):
        self.tileID = tileID
        self.image = [list(l) for l in image]

    @property
    def imageWithoutBorders(self):
        return [row[1:-1] for row in self.image[1:-1]]
    
    @property
    def sides(self):
        up = self.image[0]
        down = self.image[-1]
        left = [self.image[i][0] for i in range(len(self.image[0]))]
        right = [self.image[i][-1] for i in range(len(self.image[0]))]

        return {"U": up, "D": down, "L": left, "R": right}

def rot90CW(matrix):
    return [list(l) for l in zip(*matrix[::-1])]

def flipH(matrix):
    return [row[::-1] for row in matrix]

###################################

# Loooots of assumptions made for this one to work. Should be
# good for all test cases, but it's very likely they were
# VERY carefully picked for a bunch of reasons.

rawTiles = AOCUtils.loadInput(20)

rawTiles = "\n".join(rawTiles).split("\n\n")

tiles = dict()
for rawTile in rawTiles:
    rawTile = rawTile.split("\n")

    tileID = int(rawTile[0].split()[1][:-1])
    tile = [l for l in rawTile[1:] if l] # Input has one extra newline at the end

    tiles[tileID] = Tile(tileID, tile)

# Assume tiles have equal sizes and are all squares,
# get size of one of them (doesn't matter which one)
tileSize = len(tiles[list(tiles.keys())[0]].image)

# Build tiles adjacency matrix
tileConnections = dict()
for tile1ID, tile1 in tiles.items():
    for tile2ID, tile2 in tiles.items():
        if tile1ID == tile2ID: continue

        for side1Direction, side1 in tile1.sides.items():
            for side2Direction, side2 in tile2.sides.items():
                if side1 in [side2, side2[::-1]]:
                    if tile1ID not in tileConnections:
                        tileConnections[tile1ID] = dict()
                    tileConnections[tile1ID][side1Direction] = tile2ID

# Assume there will be only one possible match/choice/placement for each tile
cornerTiles = [tileID for tileID, conns in tileConnections.items() if len(conns) == 2]

p1 = 1
for tileID in cornerTiles:
    p1 *= tileID

print("Part 1: {}".format(p1))

mov4 = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

dirsOpposite = {"D": "U", "U": "D", "L": "R", "R": "L"}
dirsRot90CW = {"D": "L", "U": "R", "L": "U", "R": "D"}
dirsFlipH = {k: (v if k in "LR" else dirsOpposite[v]) for k, v in dirsOpposite.items()}

# Figure out the correct tile placement (after tiles are
# rotated/flipped), building a `grid` matrix made of tile IDs.
# Assume grid is square (i.e. `len(tiles)` is a perfect square)
gridSize = int(len(tiles) ** 0.5)
grid = [[None for _ in range(gridSize)] for _ in range(gridSize)]

# Pick any corner tile (doesn't matter which, as long
# as `startPos` is set based on their neighbors)
startTile = cornerTiles[0]
if all(c in tileConnections[startTile] for c in "DR"): # Top-left
    startPos = (0, 0)
elif all(c in tileConnections[startTile] for c in "DL"): # Top-right
    startPos = (0, len(grid)-1)
elif all(c in tileConnections[startTile] for c in "UR"): # Bottom-left
    startPos = (len(grid)-1, 0)
elif all(c in tileConnections[startTile] for c in "UL"): # Bottom-right
    startPos = (len(grid)-1, len(grid)-1)

# BFS starting from the picked corner until the grid is filled
queue = deque([(startPos, startTile)])
tilesPlaced = set()
while queue:
    pos, tile = queue.popleft()

    if tile in tilesPlaced: continue
    tilesPlaced.add(tile)

    grid[pos[0]][pos[1]] = tile

    for direction, adjTile in tileConnections[tile].items():
        # Loop through all possible rotations/flips until the matching one is found
        # Performing these actions yields all possible versions after each one:
        #   nothing, rot90CW, rot90CW, rot90CW, flipH, rot90CW, rot90CW, rot90CW 
        # TODO: Can be found directly instead of looping through all 8
        tries = 0
        while tiles[adjTile].sides[dirsOpposite[direction]] != tiles[tile].sides[direction]:
            if tries == 3:
                tiles[adjTile].image = flipH(tiles[adjTile].image)
                tileConnections[adjTile] = {dirsFlipH[k]: v for k, v in tileConnections[adjTile].items()}
            else:
                tiles[adjTile].image = rot90CW(tiles[adjTile].image)
                tileConnections[adjTile] = {dirsRot90CW[k]: v for k, v in tileConnections[adjTile].items()}
            tries += 1

        delta = mov4[direction]
        nxtPos = (pos[0]+delta[0], pos[1]+delta[1])
        queue.append((nxtPos, adjTile))

# Merge the tiles row by row
image = []
tileSizeWithoutBorder = tileSize - 2
for rowIndex in range(gridSize * tileSizeWithoutBorder):
    gridColumn = rowIndex // tileSizeWithoutBorder
    tileRow = rowIndex % tileSizeWithoutBorder

    row = []
    for i in range(gridSize):
        row += tiles[grid[gridColumn][i]].imageWithoutBorders[tileRow]
    image.append(row)

# Print matrix of tile IDs
# for i in range(len(grid)): print(grid[i])

# Print final image
# print("\n".join("".join(row) for row in image))

# Print image but pretty (with borders, tile IDs and separators)
# for rowIndex in range(gridSize * tileSize):
#     gridColumn = rowIndex // tileSize
#     tileRow = rowIndex % tileSize
#     if tileRow == 0:
#         print("-" * gridSize * (tileSize+1))
#         tileIDs = [grid[gridColumn][i] for i in range(gridSize)]
#         print("   " + "       ".join([str(s) for s in tileIDs]))
#     print("|".join("".join(tiles[grid[gridColumn][i]].image[tileRow]) for i in range(gridSize)))

monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]
monsterRoughness = sum(row.count("#") for row in monster)

# Assume the correct rotation/flip will be the only one with any monsters
monsters = 0
tries = 0
# Loop through all possible rotations/flips until a monster is found
while monsters == 0:
    for i in range(len(image) - len(monster) + 1):
        for j in range(len(image[0]) - len(monster[0]) + 1):
            roughness = 0
            # Assume a # can be part of more than one monster (although
            # I'm pretty sure this is not the case in any of the actual inputs)
            for mi in range(len(monster)):
                for mj in range(len(monster[0])):
                    if monster[mi][mj] == "#" and image[i+mi][j+mj] == "#":
                        roughness += 1

            monsters += int(roughness == monsterRoughness)

    # Performing these actions yields all possible versions after each one:
    #   nothing, rot90CW, rot90CW, rot90CW, flipH, rot90CW, rot90CW, rot90CW 
    if tries == 3:
        image = flipH(image)
    else:
        image = rot90CW(image)
    tries += 1

totalRoughness = sum(row.count("#") for row in image)
p2 = totalRoughness - (monsters * monsterRoughness)

print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()