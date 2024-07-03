def cardPoints(line):
    line = line.split(':')[1].strip()
    winningLine = line.split('|')[0].strip()
    myNumbersLine = line.split('|')[1].strip()
    winningSet = set()
    matchingCards = 0
    for num in winningLine.split(' '):
        if num.strip() != '':
            winningSet.add(num.strip())
    for num in myNumbersLine.split(' '):
        if num.strip() != '':
            matchingCards += 1 if num in winningSet else 0
    return matchingCards

# Part 1
with open('input4.txt') as openfileobject:
    totalSum = 0
    for line in openfileobject:
        powers = cardPoints(line)
        if powers > 0:
            totalSum += 2**(powers - 1)        
    print('Part 1: ', totalSum)

# Part 2
with open('input4.txt') as openfileobject:
    totalSum = 0
    copies = {}
    currentCard = 0
    for line in openfileobject:
        currentCard += 1
        matchingCards = cardPoints(line)        
        copies[currentCard] = copies[currentCard] + 1 if currentCard in copies else 1
        for i in range(matchingCards):
            nextCard = currentCard + i + 1
            copies[nextCard] = copies[nextCard] + copies[currentCard] if nextCard in copies else copies[currentCard]
    for copy in copies:
        totalSum += copies[copy]
    print('Part 2: ', totalSum)


