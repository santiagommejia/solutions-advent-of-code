# Part 1
with open('input1.txt') as openfileobject:
    currentSum = 0
    maxSoFar = 0
    for line in openfileobject:
        line = line.strip()
        if line != '':
            currentSum += int(line)
        else:
            if currentSum > maxSoFar:
                maxSoFar = currentSum
            currentSum = 0
    print(maxSoFar)

# Part 2
with open('input1.txt') as openfileobject:
    currentSum = 0
    maxSoFar = 0
    caloriesCount = []
    for line in openfileobject:
        line = line.strip()
        if line != '':
            currentSum += int(line)
        else:
            caloriesCount.append(currentSum)
            currentSum = 0
    caloriesCount.append(currentSum)
    caloriesCount.sort()
    elvesCount = len(caloriesCount)
    result = caloriesCount[elvesCount - 1] + caloriesCount[elvesCount - 2] + caloriesCount[elvesCount - 3]
    print(result)