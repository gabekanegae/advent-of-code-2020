#######################################
# --- Day 21: Allergen Assessment --- #
#######################################

import AOCUtils

#######################################

rawFoods = AOCUtils.loadInput(21)

foods = []
for rawFood in rawFoods:
    rawIngredients, rawAllergies = rawFood.split(" (contains ")
    rawAllergies = rawAllergies[:-1].split(", ")
    rawIngredients = rawIngredients.split()

    allergies = set(rawAllergies)
    ingredients = set(rawIngredients)

    foods.append((ingredients, allergies))

allIngredients = []
for ingredients, _ in foods:
    allIngredients += ingredients

# Make a list of list of ingredients that make a recipe with each allergy
possibleCauses = dict()
for ingredients, allergies in foods:
    for allergy in allergies:
        if allergy not in possibleCauses:
            possibleCauses[allergy] = []
        possibleCauses[allergy].append(ingredients)

# Narrow down the possibilities by taking intersections
# of ingredients of recipes that cause each allergy
for allergy in possibleCauses:
    possibleCauses[allergy] = set.intersection(*possibleCauses[allergy])

mayCauseAllergy = set.union(*possibleCauses.values())
cantCauseAllergy = set(allIngredients) - mayCauseAllergy

p1 = sum(ingredients in cantCauseAllergy for ingredients in allIngredients)
print("Part 1: {}".format(p1))

possibleCausesList = list(possibleCauses.items())

# Assume the correct answer can be found by cascading
# the correct answers from before
allergyCauses = dict()
for i in range(len(possibleCausesList)):
    # Always get the ingredient with the smallest amount of possibilities
    # i.e. sort by descending set length (so it can be later popped in O(1))
    if len(possibleCausesList[-1][1]) != 1:
        possibleCausesList.sort(key=lambda x: len(x[1]), reverse=True)

    # Assume len(possible) == 1, i.e. there's only one answer
    allergy, possible = possibleCausesList[-1]
    cause = possible.pop()

    allergyCauses[allergy] = cause

    possibleCausesList.pop() # Remove allergy that had its cause identified

    # Remove determined cause from all other possibilities
    for j in range(len(possibleCausesList)):
        possibleCausesList[j][1].discard(cause)

allergyCausesList = list(allergyCauses.items())
allergyCausesList.sort(key=lambda x: x[0])

p2 = ",".join(cause for _, cause in allergyCausesList)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()