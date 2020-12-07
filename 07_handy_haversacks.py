###################################
# --- Day 7: Handy Haversacks --- #
###################################

import AOCUtils

def containsBag(bags, outerBag, goal):
    return outerBag == goal or any(containsBag(bags, bag, goal) for bag in bags[outerBag])

def countBagsInside(bags, outerBag):
    return sum(n * (countBagsInside(bags, bag) + 1) for bag, n in bags[outerBag].items())

###################################

rawBags = AOCUtils.loadInput(7)

bags = dict()
for rawBag in rawBags:
    color, rawContents = rawBag.split(" contain ")
    rawContents = rawContents.rstrip(".").split(", ")

    color = color.replace("bags", "bag")

    contents = dict()
    if rawContents[0] != "no other bags":
        for rawContent in rawContents:
            rawContent = rawContent.split()

            contentAmount = int(rawContent[0])
            contentColor = " ".join(rawContent[1:])

            contentColor = contentColor.replace("bags", "bag")
            contents[contentColor] = contentAmount

    bags[color] = contents

target = "shiny gold bag"

p1 = sum(containsBag(bags, bag, target) for bag in bags) - 1
print("Part 1: {}".format(p1))

p2 = countBagsInside(bags, target)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()