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
    ingredientLists = possibleCauses[allergy]

    intersection = set(ingredientLists[0])
    for ingredientList in ingredientLists[1:]:
        intersection &= ingredientList

    possibleCauses[allergy] = intersection

mayCauseAllergy = set()
for ingredients in possibleCauses.values():
    mayCauseAllergy |= ingredients

cantCauseAllergy = set(allIngredients) - mayCauseAllergy

p1 = sum(ingredients in cantCauseAllergy for ingredients in allIngredients)
print("Part 1: {}".format(p1))

# Sort by ascending amount of possible causes
possibleCausesList = list(possibleCauses.items())
possibleCausesList.sort(key=lambda x: len(x[1]))

allergyCauses = {allergy: None for allergy in possibleCauses}

# Assume len(possibleCausesList[0]) == 1, and the correct answer
# can be found by cascading the correct answers from before
for i in range(len(possibleCausesList)):
    # Always get the ingredient with the smallest amount of possibilities
    if len(possibleCausesList[0][1]) != 1:
        possibleCausesList.sort(key=lambda x: len(x[1]))
    allergy, possible = possibleCausesList[0]

    # Found correct answer
    if len(possible) == 1:
        cause = possible.pop()

        allergyCauses[allergy] = cause

        # Remove determined cause from all other possibilities
        possibleCausesList.pop(0)
        for j in range(len(possibleCausesList)):
            possibleCausesList[j][1].discard(cause)

allergyCausesList = list(allergyCauses.items())
allergyCausesList.sort(key=lambda x: x[0])

p2 = ",".join(cause for _, cause in allergyCausesList)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()