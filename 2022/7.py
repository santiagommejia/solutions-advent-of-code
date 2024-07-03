# in this exercise a tree is being built, the solution to each part are in methods getSolutionPart1 and getSolutionPart2 of the node functions

class Node:
    def __init__(self, size, name, isDir):
        self.childs = [] # childs is an array of nodes
        self.isDirectory = isDir
        self.size = size
        self.name = name
        self.totalSize = 0
    
    def addChild(self, child):
        self.childs.append(child)

    def calculateTotalSize(self):
        totalSize = self.size
        for child in self.childs:
            totalSize += child.calculateTotalSize()
        self.totalSize = totalSize
        return totalSize


    def getSolutionPart1(self):
        result = 0
        if self.isDirectory:
            if self.totalSize <= 100000:
                result += self.totalSize
            for child in self.childs:
                result += child.getSolutionPart1()
        return result

    def getSolutionPart2(self, currentMin, neededSpace):
        if self.isDirectory:
            if self.totalSize >= neededSpace:
                if currentMin == None or self.totalSize < currentMin:
                    currentMin = self.totalSize
            for child in self.childs:
                currentMin = min(currentMin, child.getSolutionPart2(currentMin, neededSpace))
        return currentMin

with open('input7.txt') as openfileobject:
    nodeStack = []
    parentNode = None
    rootNode = None
    for line in openfileobject:
        inputSplit = line.split(' ')
        if inputSplit[0] == '$':
            if inputSplit[1] == 'cd':
                inputSplit[2] = inputSplit[2].replace('\n', '')
                if inputSplit[2] == '/':    # cd to /
                    if rootNode == None:
                        rootNode = Node(0, 'root', True)
                    parentNode = rootNode
                    nodeStack = [parentNode]
                elif inputSplit[2] == '..': # cd one level up
                    nodeStack.pop()
                    parentNode = nodeStack[len(nodeStack) - 1]
                else: # cd to targetDir
                    targetDir = inputSplit[2]
                    hasChild = False
                    for child in parentNode.childs:
                        if child.name == targetDir:
                            hasChild = True
                            parentNode = child
                            nodeStack.append(child)
                            break
                    if not hasChild:
                        node = Node(0, targetDir, True)
                        parentNode = node
                        nodeStack.append(node)
        else:   # is showing a list
            inputSplit[1] = inputSplit[1].replace('\n', '')
            if inputSplit[0] == 'dir': # there is a directory here
                dirName = inputSplit[1]
                hasChild = False
                for child in parentNode.childs:
                    if child.name == dirName:
                        hasChild = True
                        break
                if not hasChild:
                    node = Node(0, dirName, True)
                    parentNode.addChild(node)
            else: # file
                fileSize = int(inputSplit[0])
                fileName = inputSplit[1]
                hasChild = False
                for child in parentNode.childs:
                    if child.name == fileName:
                        hasChild = True
                        break
                if not hasChild:
                    node = Node(fileSize, fileName, False)
                    parentNode.addChild(node)
    rootNode.calculateTotalSize()
    
    resultPart1 = rootNode.getSolutionPart1()
    print('result part 1: ', resultPart1)

    freeSpace = 70000000 - rootNode.totalSize
    neededSpace = 30000000 - freeSpace
    resultPart2 = rootNode.getSolutionPart2(None, neededSpace)
    print('result part 2: ', resultPart2)
    
