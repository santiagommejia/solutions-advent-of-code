# Part 1
with open('input5.txt') as openfileobject:
    stacks = []
    hasReversedStacks = False
    for line in openfileobject:
        lineLength = len(line)
        isNewLine = True
        stackCounter = 0
        isInstruction = line[0:4] == 'move'
        if not isInstruction:
            for i in range(0, lineLength, 4):
                crate = line[i:i+4]
                crate = crate.strip()
                if crate.isnumeric():
                    break
                if isNewLine:
                    stackCounter = 0
                if len(stacks) <= stackCounter:
                    stacks.append([])
                if not crate == '':
                    stacks[stackCounter].append(str(crate[1]))
                stackCounter += 1
                isNewLine = False
        
        else:
            if not hasReversedStacks:
                hasReversedStacks = True
                for stack in stacks:
                    stack.reverse()
            x, move, y, fromStack, z, toStack = line.split(' ')
            move = int(move)
            fromStack = int(fromStack) - 1
            toStack = int(toStack) - 1
            for i in range(0, move):
                moving = stacks[fromStack].pop()
                stacks[toStack].append(moving) 
    result = ''
    for stack in stacks:
        stackSize = len(stack)
        if stackSize > 0:
            result += stack[stackSize - 1]
    print(result)


# Part 2
with open('input5.txt') as openfileobject:
    stacks = []
    hasReversedStacks = False
    for line in openfileobject:
        lineLength = len(line)
        isNewLine = True
        stackCounter = 0
        isInstruction = line[0:4] == 'move'
        if not isInstruction:
            for i in range(0, lineLength, 4):
                crate = line[i:i+4]
                crate = crate.strip()
                if crate.isnumeric():
                    break
                if isNewLine:
                    stackCounter = 0
                if len(stacks) <= stackCounter:
                    stacks.append([])
                if not crate == '':
                    stacks[stackCounter].append(str(crate[1]))
                stackCounter += 1
                isNewLine = False
        
        else:
            if not hasReversedStacks:
                hasReversedStacks = True
                for stack in stacks:
                    stack.reverse()
            x, move, y, fromStack, z, toStack = line.split(' ')
            move = int(move)
            fromStack = int(fromStack) - 1
            toStack = int(toStack) - 1
            toMove = []
            for i in range(0, move):
                moving = stacks[fromStack].pop()
                toMove.append(moving)
            toMove.reverse()
            for item in toMove:
                stacks[toStack].append(item) 
    result = ''
    for stack in stacks:
        stackSize = len(stack)
        if stackSize > 0:
            result += stack[stackSize - 1]
    print(result)
            