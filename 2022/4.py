# Part 1
with open('input4.txt') as openfileobject:
    selfContainedSets = 0
    for line in openfileobject:
        first, second = line.split(',')
        a, b = map(int, first.split('-'))
        x, y = map(int, second.split('-'))
        if x >= a and x <= b and y >= a and y <= b:
            selfContainedSets += 1
        elif a >= x and a <= y and b >= x and b <= y:
            selfContainedSets += 1
    print(selfContainedSets)

# Part 2
with open('input4.txt') as openfileobject:
    overlaps = 0
    for line in openfileobject:
        first, second = line.split(',')
        a, b = map(int, first.split('-'))
        x, y = map(int, second.split('-'))
        if (x >= a and x <= b) or (y >= a and y <= b):
            overlaps += 1
        elif (a >= x and a <= y) or (b >= x and b <= y):
            overlaps += 1
    print(overlaps)