import math
file = open("C:/Exercises/AdvOfCode2023/ProbFile4.txt","r")
totalPoints = 0
allCards = (file.readlines())
for card in allCards:
    card = card.split()[2:]
    for i in range (len(card)):
        if card [i] == "|":
            winnings = card[:i]
            actual = card[i+1:]
            break
    winnings = set(winnings)
    actual = set(actual)
    luckyNums = (winnings.intersection(actual))
    points = math.floor(2 ** (luckyNums.__len__()-1))
    totalPoints += points
print(totalPoints)
