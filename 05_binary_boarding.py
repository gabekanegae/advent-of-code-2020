##################################
# --- Day 5: Binary Boarding --- #
##################################

import AOCUtils

##################################

boardingPasses = AOCUtils.loadInput(5)

seatIDs = []
for boardingPass in boardingPasses:
    lo, hi = 0, 127
    for c in boardingPass[:7]:
        mid = (lo + hi) // 2
        if c == "F":
            hi = mid
        elif c == "B":
            lo = mid

    row = hi

    lo, hi = 0, 7
    for c in boardingPass[7:]:
        mid = (lo + hi) // 2
        if c == "L":
            hi = mid
        elif c == "R":
            lo = mid

    col = hi

    seatID = 8 * row + col
    seatIDs.append(seatID)

print("Part 1: {}".format(max(seatIDs)))

allSeats = set(range(min(seatIDs), max(seatIDs)+1))
missingSeats = allSeats - set(seatIDs) # Assume len(missingSeats) == 1

print("Part 2: {}".format(missingSeats.pop()))

AOCUtils.printTimeTaken()