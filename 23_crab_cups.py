#############################
# --- Day 23: Crab Cups --- #
#############################

import AOCUtils

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def crabCups(cups, moves):
    nodes = [Node(k) for k in cups]
    for i in range(len(cups)-1):
        nodes[i].next = nodes[i+1]
    nodes[len(cups)-1].next = nodes[0]

    nodeLookup = {node.data: node for node in nodes}

    cur = nodes[0].data
    for _ in range(moves):
        p = nodeLookup[cur]

        a = nodeLookup[cur].next
        b = nodeLookup[cur].next.next
        c = nodeLookup[cur].next.next.next

        nodeLookup[cur].next = c.next

        dest = cur
        while True:
            dest -= 1

            if dest < 1:
                dest = len(cups)

            if dest not in [a.data, b.data, c.data]:
                break

        c.next = nodeLookup[dest].next
        nodeLookup[dest].next = a
        nodeLookup[dest].next.next = b
        nodeLookup[dest].next.next.next = c

        cur = nodeLookup[cur].next.data

    return nodeLookup[1].next

#############################

rawCups = AOCUtils.loadInput(23)

cups1 = [int(i) for i in str(rawCups)]
p = crabCups(cups1, 100)

p1 = []
for _ in range(8):
    p1.append(str(p.data))
    p = p.next

print("Part 1: {}".format("".join(p1)))

cups2 = cups1 + list(range(len(cups1)+1, 1000000+1))
p = crabCups(cups2, 10000000)

print("Part 2: {}".format(p.data * p.next.data))

AOCUtils.printTimeTaken()