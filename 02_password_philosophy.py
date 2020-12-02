######################################
# --- Day 2: Password Philosophy --- #
######################################

import AOCUtils

######################################

rawPasswords = AOCUtils.loadInput(2)

p1 = 0
p2 = 0
for rawPassword in rawPasswords:
    counts, c, password = rawPassword.split()
    a, b = [int(i) for i in counts.split("-")]
    c = c[0]

    if a <= password.count(c) <= b:
        p1 += 1
    if (password[a-1] == c) ^ (password[b-1] == c):
        p2 += 1

print("Part 1: {}".format(p1))

print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()