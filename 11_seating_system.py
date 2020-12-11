##################################
# --- Day 11: Seating System --- #
##################################

import AOCUtils

moves8 = [(0, 1), (1, 0), (0, -1), (-1, 0),
          (1, 1), (1, -1), (-1, 1), (-1, -1)]

##################################

originalSeats = [list(l) for l in AOCUtils.loadInput(11)]

seats = [l[:] for l in originalSeats]
h, w = len(seats), len(seats[0])

hasChanged = True
while hasChanged:
    newSeats = [l[:] for l in seats]
    hasChanged = False
    for a in range(h):
        for b in range(w):
            n = 0
            for da, db in moves8:
                if da == 0 and db == 0: continue
                
                if 0 <= a+da < h and 0 <= b+db < w:
                    if seats[a+da][b+db] == "#":
                        n += 1

            if seats[a][b] == "L" and n == 0:
                newSeats[a][b] = "#"
                hasChanged = True
            elif seats[a][b] == "#" and n >= 4:
                newSeats[a][b] = "L"
                hasChanged = True

    seats = newSeats

p1 = sum(l.count("#") for l in seats)
print("Part 1: {}".format(p1))

seats = [l[:] for l in originalSeats]
h, w = len(seats), len(seats[0])

hasChanged = True
while hasChanged:
    hasChanged = False
    newSeats = [l[:] for l in seats]
    for a in range(h):
        for b in range(w):
            n = 0
            for da, db in moves8:
                ca, cb = a, b
                while 0 <= ca+da < h and 0 <= cb+db < w:
                    ca += da
                    cb += db

                    if seats[ca][cb] == "#":
                        n += 1

                    if seats[ca][cb] != ".":
                        break

            if seats[a][b] == "L" and n == 0:
                newSeats[a][b] = "#"
                hasChanged = True
            elif seats[a][b] == "#" and n >= 5:
                newSeats[a][b] = "L"
                hasChanged = True

    seats = newSeats

p2 = sum(l.count("#") for l in seats)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()