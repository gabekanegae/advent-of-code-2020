##################################
# --- Day 13: Shuttle Search --- #
##################################

import AOCUtils

# Modular inverse of n (assumes mod is prime, uses Euler's Theorem)
def modinv(n, mod):
    return pow(n, mod-2, mod)

# Get smallest x (i.e. unique in mod N) that satisfies a list
# of linear congruences (assumes all elements in mods are coprime)
def chineseRemainderTheorem(mods, remainders):
    # Given linear congruences x%3 = 2, x%5 = 3, x%7 = 2,
    # x = chineseRemainderTheorem([3, 5, 7], [2, 3, 2])

    N = 1
    for m in mods:
        N *= m

    x = sum(r * N//m * modinv(N//m, m) for m, r in zip(mods, remainders))
    return x % N

##################################

notes = AOCUtils.loadInput(13)

arrivedAtBusStop = int(notes[0])
schedule = notes[1].split(",")

nextArrivals = []
for i, busID in enumerate(schedule):
    if busID == "x": continue
    busInterval = int(busID)

    sinceLastArrival = arrivedAtBusStop % busInterval
    untilNextArrival = busInterval - sinceLastArrival

    nextArrivals.append((untilNextArrival, busInterval))

nextArrivals.sort()
nextArrival = nextArrivals[0]

print("Part 1: {}".format(nextArrival[0] * nextArrival[1]))

# Builds a list of linear congruences as x%mod = remainder
#   Example with schedule=[67,7,x,59,61]:
#       (t+0) % 67 = 0   ->   t % 67 = (67-0)%67   ->   t % 67 =  0 
#       (t+1) %  7 = 0   ->   t %  7 =   (7-1)%7   ->   t %  7 =  6
#       (t+3) % 59 = 0   ->   t % 59 = (59-3)%59   ->   t % 59 = 56 
#       (t+4) % 61 = 0   ->   t % 61 = (61-4)%61   ->   t % 61 = 57
#     mods = [67, 7, 59, 61]
#     remainders = [0, 6, 56, 57]

mods = []
remainders = []
for i, busID in enumerate(schedule):
    if busID == "x": continue
    busInterval = int(busID)

    mod = busInterval
    remainder = (busInterval - i) % busInterval

    mods.append(mod)
    remainders.append(remainder)

print("Part 2: {}".format(chineseRemainderTheorem(mods, remainders)))

AOCUtils.printTimeTaken()