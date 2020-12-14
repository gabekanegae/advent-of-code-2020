################################
# --- Day 14: Docking Data --- #
################################

import AOCUtils

################################

program = AOCUtils.loadInput(14)

mem = dict()
mask = None

for instruction in program:
    var, data = instruction.split(" = ")
    if var == "mask":
        mask = data
    elif var.startswith("mem"):
        idx = var[4:-1]

        data = list(bin(int(data))[2:].zfill(36))
        for i, c in enumerate(mask):
            if c != "X":
                data[i] = c
        data = int("".join(data), 2)

        mem[idx] = data

print("Part 1: {}".format(sum(mem.values())))

mem = dict()
mask = None

for instruction in program:
    var, data = instruction.split(" = ")
    if var == "mask":
        mask = data
    elif var.startswith("mem"):
        idx = var[4:-1]

        idx = list(bin(int(idx))[2:].zfill(36))
        for i, c in enumerate(mask):
            if c == "1":
                idx[i] = c

        n = mask.count("X")
        for bits in range(2**n):
            bits = bin(bits)[2:].zfill(n)

            newIdx = idx[:]
            b = 0
            for i, c in enumerate(mask):
                if c == "X":
                    newIdx[i] = bits[b]
                    b += 1

            newIdx = int("".join(newIdx), 2)
            mem[newIdx] = int(data)

print("Part 2: {}".format(sum(mem.values())))

AOCUtils.printTimeTaken()