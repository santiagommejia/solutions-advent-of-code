# Part 1
# with open('input2.txt') as openfileobject:
#     totalSum = 0
#     maxRed = 12
#     maxGreen = 13
#     maxBlue = 14
#     for line in openfileobject:
#         gameIsValid = True
#         gameNumber = int(line.split(':')[0].replace('Game ',''))
#         gameSets = line.split(':')[1].split(';')
#         for gameSet in gameSets:
#             colors = gameSet.split(',')
#             for color in colors:
#                 colorCount = color.strip().split(' ')
#                 if (colorCount[1] == 'red' and int(colorCount[0]) > maxRed) or (colorCount[1] == 'green' and int(colorCount[0]) > maxGreen) or (colorCount[1] == 'blue' and int(colorCount[0]) > maxBlue):
#                    gameIsValid = False
#                    break
#         if gameIsValid:
#             totalSum += gameNumber
#     print(totalSum)

# Part 1
with open('input2.txt') as openfileobject:
    totalSum = 0
    for line in openfileobject:
        maxRed = 1
        maxGreen = 1
        maxBlue = 1
        gameSets = line.split(':')[1].split(';')
        for gameSet in gameSets:
            colors = gameSet.split(',')
            for color in colors:
                colorCount = color.strip().split(' ')
                if (colorCount[1] == 'red' and int(colorCount[0]) > maxRed):
                    maxRed = int(colorCount[0])
                if (colorCount[1] == 'green' and int(colorCount[0]) > maxGreen):
                    maxGreen = int(colorCount[0])
                if (colorCount[1] == 'blue' and int(colorCount[0]) > maxBlue):
                    maxBlue = int(colorCount[0])
        power = maxRed * maxGreen * maxBlue
        totalSum += power
    print(totalSum)
