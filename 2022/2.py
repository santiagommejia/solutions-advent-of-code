# A = rock
# B = paper
# C = scissors

WIN = 6
DRAW = 3
LOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

# X = rock
# Y = paper
# Z = scissors

def roundScore(a, b):
    score = 0
    if b == 'X':
        score += ROCK 
        if a == 'A':
            score +=  DRAW
        elif a == 'C':
            score += WIN
    elif b == 'Y':
        score += PAPER
        if a == 'A':
            score += WIN
        elif a == 'B':
            score += DRAW
    else:
        score += SCISSORS
        if a == 'B':
            score += WIN
        elif a == 'C':
            score += DRAW
    return score

# X = need to lose
# Y = need to draw
# Z = need to win

def decryptedRoundScore(a, b):
    score = 0
    if b == 'X': 
        score += LOSE
        if a == 'A':
            score +=  SCISSORS
        elif a == 'B':
            score += ROCK
        else:
            score += PAPER
    elif b == 'Y':
        score += DRAW
        if a == 'A':
            score += ROCK
        elif a == 'B':
            score += PAPER
        else:
            score += SCISSORS
    else:
        score += WIN
        if a == 'A':
            score += PAPER
        elif a == 'B':
            score += SCISSORS
        else:
            score += ROCK
    return score
        

# Part 1
with open('input2.txt') as openfileobject:
    totalScore = 0
    for line in openfileobject:
        line = line.strip()
        a, b = line.split(' ')
        totalScore += roundScore(a, b)
    print(totalScore)

# Part 2
with open('input2.txt') as openfileobject:
    totalScore = 0
    for line in openfileobject:
        line = line.strip()
        a, b = line.split(' ')
        totalScore += decryptedRoundScore(a, b)
    print(totalScore)
