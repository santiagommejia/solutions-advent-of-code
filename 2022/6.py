# Part 1
with open('input6.txt') as openfileobject:
    for line in openfileobject:
        numberOfCharsToCheck = 4
        lineLength = len(line)
        for i in range(0, lineLength):
            marker = set()
            if i > numberOfCharsToCheck - 1:
                for j in range(numberOfCharsToCheck):
                    marker.add(line[i + j - numberOfCharsToCheck])
            if len(marker) == numberOfCharsToCheck:
                print(i)
                break


# Part 2
with open('input6.txt') as openfileobject:
    for line in openfileobject:
        numberOfCharsToCheck = 14
        lineLength = len(line)
        for i in range(0, lineLength):
            marker = set()
            if i > numberOfCharsToCheck - 1:
                for j in range(numberOfCharsToCheck):
                    marker.add(line[i + j - numberOfCharsToCheck])
            if len(marker) == numberOfCharsToCheck:
                print(i)
                break