#################################
# --- Day 25: Combo Breaker --- #
#################################

import AOCUtils

def brutePrivate(public, e, n):
    # (e ^ private) % n = public
    
    private = 1
    genPublic = 1
    while True:
        genPublic = (genPublic * e) % n
        if genPublic == public:
            return private
        private += 1
    
    return private

#################################

cardPublic, doorPublic = AOCUtils.loadInput(25)

n = 20201227
e = 7

doorPrivate = brutePrivate(doorPublic, e, n)
doorKey = pow(cardPublic, doorPrivate, n)

cardPrivate = brutePrivate(cardPublic, e, n)
cardKey = pow(doorPublic, cardPrivate, n)

if doorKey == cardKey:
    print("Part 1: {}".format(doorKey))

AOCUtils.printTimeTaken()