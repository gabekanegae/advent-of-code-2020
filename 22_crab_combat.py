###############################
# --- Day 22: Crab Combat --- #
###############################

import AOCUtils
from collections import deque

def getScore(deck):
    return sum((i+1) * card for i, card in zip(range(len(deck)), reversed(deck)))

def playGame1(rawPlayer1, rawPlayer2):
    player1 = deque(rawPlayer1)
    player2 = deque(rawPlayer2)

    while player1 and player2:
        top1 = player1.popleft()
        top2 = player2.popleft()

        p1Wins = (top1 > top2)

        if p1Wins:
            player1.append(top1)
            player1.append(top2)
        else:
            player2.append(top2)
            player2.append(top1)

    return getScore(player1), getScore(player2)

def playGame2(rawPlayer1, rawPlayer2):
    player1 = deque(rawPlayer1)
    player2 = deque(rawPlayer2)

    seen = set()
    while player1 and player2:
        top1 = player1.popleft()
        top2 = player2.popleft()

        state = (tuple(player1), tuple(player2))

        if state in seen:
            p1Wins = True
        else:
            seen.add(state)

            if len(player1) >= top1 and len(player2) >= top2:
                recursiveCopy1 = list(player1)[:top1]
                recursiveCopy2 = list(player2)[:top2]

                score1, score2 = playGame2(recursiveCopy1, recursiveCopy2)

                p1Wins = (score1 > score2)
            else:
                p1Wins = (top1 > top2)

        if p1Wins:
            player1.append(top1)
            player1.append(top2)
        else:
            player2.append(top2)
            player2.append(top1)

    return getScore(player1), getScore(player2)

###############################

rawDecks = AOCUtils.loadInput(22)

rawPlayer1, rawPlayer2 = "\n".join(rawDecks).split("\n\n")
rawPlayer1 = [int(i) for i in rawPlayer1.split("\n")[1:]]
rawPlayer2 = [int(i) for i in rawPlayer2.split("\n")[1:]]

print("Part 1: {}".format(max(playGame1(rawPlayer1, rawPlayer2))))

print("Part 2: {}".format(max(playGame2(rawPlayer1, rawPlayer2))))

AOCUtils.printTimeTaken()