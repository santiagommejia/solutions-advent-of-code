# Part 1
def isSurroundedBySimbol(matrix, startCol, endCol, row):
    result = False
    rows = len(matrix)
    cols = len(matrix[row])
    gear = '*'
    gears = []
    if row > 0: # check the upper row
        line = ''.join(matrix[row - 1])
        segment = line[max(0, startCol - 1) : min(cols - 1, endCol + 1)]
        hasSymbol = any(not char.isdigit() and char != '.' for char in segment)
        gearPositions = [pos for pos, char in enumerate(segment) if char == gear]
        for gearPos in gearPositions:
            gears.append((row - 1, gearPos + max(0, startCol - 1)))
        if hasSymbol:
            result = True
    if row < rows - 1: # check the lower row
        line = ''.join(matrix[row + 1])
        segment = line[max(0, startCol - 1) : min(cols - 1, endCol + 1)]
        hasSymbol = any(not char.isdigit() and char != '.' for char in segment) 
        gearPositions = [pos for pos, char in enumerate(segment) if char == gear]
        for gearPos in gearPositions:
            gears.append((row + 1, gearPos + max(0, startCol - 1)))
        if hasSymbol:
            result = True
    if startCol > 0:
        char = matrix[row][startCol - 1]
        hasSymbol =  char != '.' and not char.isdigit()
        if char == gear:
            gears.append((row, startCol - 1))
        if hasSymbol:
            result = True
    if endCol < cols - 1:
        char = matrix[row][endCol]
        hasSymbol =  char != '.' and not char.isdigit()
        if char == gear:
            gears.append((row, endCol))
        if hasSymbol:
            result = True
    return result, gears
gearDict = {}

def addToGearDict(gears, number):
    for gear in gears:
        numbers = []
        if gear in gearDict:
            numbers = gearDict[gear]
        numbers.append(int(number))
        gearDict[gear] = numbers

def getGearRatiosSum():
    totalSum = 0
    for gear in gearDict:
        numbers = gearDict[gear]
        if len(numbers) == 2:
            totalSum += numbers[0] * numbers[1]
    return totalSum

with open('input3.txt') as openfileobject:
    matrix = []
    totalSum = 0
    for line in openfileobject:
        lineVector = []
        for char in line:
            if char != '\n':
                lineVector.append(char)
        matrix.append(lineVector)
    rows = len(matrix)
    for row in range(rows):
        line = ''.join(matrix[row])
        cols = len(line)
        isCountingNumber = False
        startCol = 0
        for col in range(cols):
            char = matrix[row][col]
            if char.isnumeric():
                if not isCountingNumber:
                    startCol = col
                isCountingNumber = True
            else:
                if isCountingNumber:
                    isSurroundedBySimbolx, gears = isSurroundedBySimbol(matrix, startCol, col, row)
                    foundNumberStr = line[startCol : col]
                    addToGearDict(gears, foundNumberStr)
                    if isSurroundedBySimbolx:
                        totalSum += int(foundNumberStr)
                    isCountingNumber = False
        if isCountingNumber:
            isSurroundedBySimbolx, gears = isSurroundedBySimbol(matrix, startCol, cols, row)
            foundNumberStr = line[startCol : cols]
            addToGearDict(gears, foundNumberStr)
            if isSurroundedBySimbolx:
                totalSum += int(foundNumberStr)
            isCountingNumber = False
    print('sum: ', totalSum)
    print('gears: ', getGearRatiosSum())
