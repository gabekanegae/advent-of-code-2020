################################
# --- Day 24: Lobby Layout --- #
################################

import AOCUtils

def splitTokens(s, tokens):
    tokens = set(tokens)
    
    i = 0
    j = 0
    out = []
    while j < len(s):
        if s[i:j] in tokens:
            out.append(s[i:j])
            i = j
        j += 1
    out.append(s[i:])
    
    return out

# Y axis rotated 30 deg (L/R is W/E)
directions = {"nw": (1, -1), "w": (0, -1), "ne": (1, 0),
              "sw": (-1, 0), "e": (0, 1),  "se": (-1, 1)}

################################

paths = AOCUtils.loadInput(24)

blackTiles = set()
for path in paths:
    cur = (0, 0)
    for direction in splitTokens(path, directions.keys()):
        delta = directions[direction]
        cur = (cur[0]+delta[0], cur[1]+delta[1])

    if cur not in blackTiles:
        blackTiles.add(cur)
    else:
        blackTiles.remove(cur)

print("Part 1: {}".format(len(blackTiles)))

for _ in range(100):
    toBeUpdated = set(blackTiles)
    for tile in blackTiles:
        for delta in directions.values():
            neighbor = (tile[0]+delta[0], tile[1]+delta[1])
            toBeUpdated.add(neighbor)

    newBlackTiles = set(blackTiles)
    for tile in toBeUpdated:
        blackNeighbors = 0
        for delta in directions.values():
            neighbor = (tile[0]+delta[0], tile[1]+delta[1])
            blackNeighbors += int(neighbor in blackTiles)

        if tile in blackTiles and (blackNeighbors == 0 or blackNeighbors > 2):
            newBlackTiles.remove(tile)
        elif tile not in blackTiles and blackNeighbors == 2:
            newBlackTiles.add(tile)

    blackTiles = newBlackTiles

print("Part 2: {}".format(len(blackTiles)))

AOCUtils.printTimeTaken()