def getNewPosition(xH, yH, direction, amount) :
    if direction == 'R':
        return xH, yH + amount
    elif direction == 'L':
        return xH, yH - amount
    elif direction == 'U':
        return xH + amount, yH
    elif direction == 'D':
        return xH - amount, yH
    return

def getNewStepPosition(xH, yH, direction) :
    if direction == 'R':
        return xH, yH + 1
    elif direction == 'L':
        return xH, yH - 1
    elif direction == 'U':
        return xH + 1, yH
    elif direction == 'D':
        return xH - 1, yH
    return

def pointsAreAdyacent(xH, yH, xT, yT):
    if xT == xH  and (yH == yT or yH == yT + 1 or yH == yT -1): # left or right adyacency
        return True
    elif yT == yH and (xH == xT or xH == xT + 1 or xH == xT -1): # up or down adyacency
        return True
    elif (xT == xH - 1 and yT == yH - 1): # top-right diagonal adyacency
        return True
    elif (xT == xH - 1 and yT == yH + 1): # top-left diagonal adyacency
        return True
    elif (xT == xH + 1 and yT == yH + 1): # bottom-left diagonal adyacency
        return True
    elif (xT == xH + 1 and yT == yH - 1): # bottom-right diagonal adyacency
        return True
    return False

def simulation(xH, yH, xT, yT, tailVisited):
    isAdyacent = pointsAreAdyacent(xH, yH, xT, yT)
    if not isAdyacent:

        xDifference = xH - xT
        yDifference = yH - yT

        if xDifference >= 1 and yDifference >= 1:
            minDiag = min(xDifference, yDifference)
            minDiag -= 1 if abs(xDifference) == abs(yDifference) else 0
            for i in range(minDiag):
                tailVisited.add((xT + i, yT + i))
            xT += minDiag
            yT += minDiag
            xDifference -= minDiag
            yDifference -= minDiag
        
        elif xDifference >= 1 and yDifference <= -1:
            minDiag = min(xDifference, abs(yDifference))
            minDiag -= 1 if abs(xDifference) == abs(yDifference) else 0
            for i in range(minDiag):
                tailVisited.add((xT + i, yT - i))
            xT += minDiag
            yT -= minDiag
            xDifference -= minDiag
            yDifference += minDiag
        
        elif xDifference <= -1 and yDifference <= -1:
            minDiag = min(abs(xDifference), abs(yDifference))
            minDiag -= 1 if abs(xDifference) == abs(yDifference) else 0
            for i in range(minDiag):
                tailVisited.add((xT - i, yT - i))
            xT -= minDiag
            yT -= minDiag
            xDifference += minDiag
            yDifference += minDiag
        
        elif xDifference <= -1 and yDifference >= 1:
            minDiag = min(abs(xDifference), yDifference)
            minDiag -= 1 if abs(xDifference) == abs(yDifference) else 0
            for i in range(minDiag):
                tailVisited.add((xT - i, yT + i))
            xT -= minDiag
            yT += minDiag
            xDifference += minDiag
            yDifference -= minDiag

        if xDifference == 0: # same row
            if yDifference > 1: # chase right
                for i in range(0, yDifference):
                    tailVisited.add((xT, yT + i))
                yT += yDifference - 1
            elif yDifference < -1: # chase left
                for i in range(0, abs(yDifference)):
                    tailVisited.add((xT, yT - i))
                yT -= abs(yDifference) - 1
        
        elif yDifference == 0: # same col
            if xDifference > 1: # chase up
                for i in range(0, xDifference):
                    tailVisited.add((xT + i, yT))
                xT += xDifference - 1
            elif xDifference < -1: # chase down
                for i in range(0, abs(xDifference)):
                    tailVisited.add((xT - i, yT))
                xT -= abs(xDifference) - 1

    return xT, yT, tailVisited

# Part 1
# with open('input9.txt') as openfileobject:
#     tailVisited = set()
#     xH = 0
#     yH = 0
#     xT = 0
#     yT = 0
#     for line in openfileobject:
#         lineSplit = line.split(' ')
#         direction = str(lineSplit[0])
#         amount = int(lineSplit[1])
#         xH, yH = getNewPosition(xH, yH, direction, amount)
#         xT, yT, tailVisited = simulation(xH, yH, xT, yT, tailVisited)
#     print('result 1: ', len(tailVisited))

# Part 2
# with open('input9.txt') as openfileobject:
#     tail9Visited = set()
#     xH = 0
#     yH = 0
#     xT = 0
#     yT = 0
#     tails = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)] # 9 tails
#     for line in openfileobject:
#         lineSplit = line.split(' ')
#         direction = str(lineSplit[0])
#         amount = int(lineSplit[1])
#         xH, yH = getNewPosition(xH, yH, direction, amount)
#         currentHeadX = xH
#         currentHeadY = yH
#         continueKnotSimulation = True
#         tailTraker = 0
#         while continueKnotSimulation:
#             if tailTraker > 0:
#                 currentHead = tails[tailTraker - 1]
#                 currentHeadX = currentHead[0]
#                 currentHeadY = currentHead[1]
#             currentTail = tails[tailTraker]
#             xT = currentTail[0]
#             yT = currentTail[1]
#             if tailTraker == 8:
#                 xT, yT, tail9Visited = simulation(currentHeadX, currentHeadY, xT, yT, tail9Visited)
#             else:
#                 xT, yT, tailVisited = simulation(currentHeadX, currentHeadY, xT, yT, set())
#             tails[tailTraker] = (xT, yT)
#             tailTraker += 1
#             if tailTraker == 9:
#                 continueKnotSimulation = False
#     print('tail 9:', sorted(tail9Visited))
#     print('result 2: ', len(tail9Visited))



























def moveHead(knots, direction, amount, tail9Visited):
    for i in range(amount):
        for j in range(len(knots)): # move un knot one time
            knot = knots[j]
            tailX, tailY = 0, 0
            if j == 0:  # head
                previousTailX, previousTailY = knot[0], knot[1]
                tailX, tailY = getNewStepPosition(previousTailX, previousTailY, direction)
                knots[0] = (tailX, tailY)
            else:
                head = knots[j - 1]
                if not pointsAreAdyacent(head[0], head[1], knot[0], knot[1]):
                    tailX, tailY = previousTailX, previousTailY
                    previousTailX, previousTailY = knot[0], knot[1]
                    knots[j] = (tailX, tailY)
                    if j == 9:
                        print(i,'tail 9 visits:', tailX, tailY)
                        tail9Visited.add((tailX, tailY))
                else:
                    print('break')
                    break
            print(knots)
    return knots, tail9Visited
            




# seguir la cola despues de cada movimiento
with open('input9.txt') as openfileobject:
    tail9Visited = set((0,0))
    xH = 0
    yH = 0
    xT = 0
    yT = 0
    knots = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)] # 1 head and 9 tails
    for line in openfileobject:
        lineSplit = line.split(' ')
        direction = str(lineSplit[0])
        amount = int(lineSplit[1])
        print(direction,amount)
        knots, tail9Visited = moveHead(knots, direction, amount, tail9Visited)
        
    # print('tail 9:', sorted(tail9Visited))
    print('result 2: ', len(tail9Visited))