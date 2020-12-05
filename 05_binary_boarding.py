##################################
# --- Day 5: Binary Boarding --- #
##################################

import AOCUtils

##################################

boardingPasses = AOCUtils.loadInput(5)

seatIDs = []
for boardingPass in boardingPasses:
    lo, hi = 0, (2 ** len(boardingPass)) - 1
    for c in boardingPass:
        mid = (lo + hi) // 2
        if c in "FL":
            hi = mid
        elif c in "BR":
            lo = mid

    seatID = hi
    seatIDs.append(seatID)

print("Part 1: {}".format(max(seatIDs)))

allSeats = set(range(min(seatIDs), max(seatIDs) + 1))
missingSeats = allSeats - set(seatIDs) # Assume len(missingSeats) == 1

print("Part 2: {}".format(missingSeats.pop()))

AOCUtils.printTimeTaken()