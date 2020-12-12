#############################
# --- Day 12: Rain Risk --- #
#############################

import AOCUtils

moves = {"E": (1, 0),
         "N": (0, 1),
         "W": (-1, 0),
         "S": (0, -1)}

#############################

navigation = AOCUtils.loadInput(12)

pos = (0, 0)
facing = 0

for inst in navigation:
    action, n = inst[0], int(inst[1:])
   
    if action in moves:
        delta = moves[action]
        pos = (pos[0] + (delta[0] * n), pos[1] + (delta[1] * n))
    elif action == "L":
        facing = (facing + (n // 90)) % 4
    elif action == "R":
        facing = (facing - (n // 90)) % 4
    elif action == "F":
        delta = list(moves.values())[facing]
        pos = (pos[0] + (delta[0] * n), pos[1] + (delta[1] * n))

print("Part 1: {}".format(abs(pos[0]) + abs(pos[1])))

pos = (0, 0)
waypoint = (10, 1)

for inst in navigation:
    action, n = inst[0], int(inst[1:])

    if action in moves:
        delta = moves[action]
        waypoint = (waypoint[0] + (delta[0] * n), waypoint[1] + (delta[1] * n))
    elif action == "L":
        for _ in range((n // 90) % 4):
            waypoint = (-waypoint[1], waypoint[0])
    elif action == "R":
        for _ in range((n // 90) % 4):
            waypoint = (waypoint[1], -waypoint[0])
    elif action == "F":
        pos = (pos[0] + (waypoint[0] * n), pos[1] + (waypoint[1] * n))

print("Part 2: {}".format(abs(pos[0]) + abs(pos[1])))

AOCUtils.printTimeTaken()