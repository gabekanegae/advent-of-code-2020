######################################
# --- Day 16: Ticket Translation --- #
######################################

import AOCUtils

######################################

rawInput = AOCUtils.loadInput(16)

rawFields, rawMyTicket, rawNearbyTickets = "\n".join(rawInput).split("\n\n")
rawFields = rawFields.strip().split("\n")
rawMyTicket = rawMyTicket.strip().split("\n")
rawNearbyTickets = rawNearbyTickets.strip().split("\n")

fields = dict()
for rawField in rawFields:
    field, rawRanges = rawField.split(": ")

    a, b = rawRanges.split(" or ")
    a = [int(i) for i in a.split("-")]
    b = [int(i) for i in b.split("-")]

    fields[field] = [a, b]

myTicket = [int(i) for i in rawMyTicket[1].split(",")]

nearbyTickets = [[int(i) for i in ticket.split(",")] for ticket in rawNearbyTickets[1:]]

errorRate = 0
validNearbyTickets = []
for ticket in nearbyTickets:
    isValidTicket = True
    for value in ticket:
        isValidValue = False
        for ranges in fields.values():
            (sa, ea), (sb, eb) = ranges
            if sa <= value <= ea or sb <= value <= eb:
                isValidValue = True
                break

        if not isValidValue:
           errorRate += value
           isValidTicket = False
    
    if isValidTicket:
        validNearbyTickets.append(ticket)

print("Part 1: {}".format(errorRate))

fieldsPossibleIndexes = dict()  
for field, ranges in fields.items():
    fieldsPossibleIndexes[field] = set()

    (sa, ea), (sb, eb) = ranges
    for i in range(len(fields)):
        possible = True
        for ticket in validNearbyTickets:
            if not (sa <= ticket[i] <= ea or sb <= ticket[i] <= eb):
                possible = False
                break

        if possible:
            fieldsPossibleIndexes[field].add(i)

# Sort by ascending amount of possible indexes
fieldsPossibleIndexes = list(fieldsPossibleIndexes.items())
fieldsPossibleIndexes.sort(key=lambda x: len(x[1]))

fieldIndexes = {field: None for field in fields}

# Assume len(fieldsPossibleIndexes[0]) == 1, and each fieldPossibleIndexes
# is a superset of the one before, with one more element
for i in range(len(fieldsPossibleIndexes)):
    field, possibleIndexes = fieldsPossibleIndexes[i]
    if len(possibleIndexes) == 1:
        index = possibleIndexes.pop()

        fieldIndexes[field] = index

        # Remove determined index from all other possibilities
        for j in range(i+1, len(fieldsPossibleIndexes)):
            fieldsPossibleIndexes[j][1].discard(index)

departureHash = 1
for field, index in fieldIndexes.items():
    if field.startswith("departure"):
        departureHash *= myTicket[index]

print("Part 2: {}".format(departureHash))

AOCUtils.printTimeTaken()