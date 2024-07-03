def scoreOfChar(char):
    if char.isupper():
        return ord(char) - 65 + 27
    else:
        return ord(char) - 96

# Part 1
with open('input3.txt') as openfileobject:
    totalScore = 0
    for line in openfileobject:
        line = line.strip()
        length = len(line)
        half = int(length / 2)
        rucksack1 = line[0:half]
        rucksack2 = line[half:length]
        set1 = set()
        for i in range(0, half):
            set1.add(rucksack1[i])
        for i in range(0, half):
            if rucksack2[i] in set1:
                score = scoreOfChar(rucksack2[i])
                totalScore += score
                break
    print(totalScore)

# Part 2
with open('input3.txt') as openfileobject:
    totalScore = 0
    groupCounter = 0
    setArray = [set(), set()]
    for line in openfileobject:     
        line = line.strip()
        length = len(line)
        for i in range(0, length):
            key = line[i]
            if groupCounter == 2:
                if key in setArray[0] and key in setArray[1]:
                    totalScore += scoreOfChar(key)
                    break
            else:
                setArray[groupCounter].add(key)
        groupCounter += 1           
        if groupCounter == 3:
            groupCounter = 0
            setArray = [set(), set()]
    print(totalScore)