# # Part 1
# with open('input5.txt') as openfileobject:
#     seeds = []
#     mappedSeeds = []
#     for line in openfileobject:
#         line = line.strip()
#         if line.startswith('seeds'):
#             seeds = line.split(':')[1].strip().split(' ')
#             seeds = list(map(int, seeds))
#         if line == '':
#             mappedSeeds = [False for i in range(len(seeds))]
#         elif line != '' and line[0].isnumeric(): # is searching in map
#             end, start, srange = map(int, line.split(' '))
#             for i in range(len(seeds)):
#                 seed = seeds[i]
#                 if seed >= start and seed<= start + srange:
#                     seeds[i] = seeds[i] if mappedSeeds[i] else end + (seed - start)
#                     mappedSeeds[i] = True
#     print('Part 1: ', min(seeds))

def getIntersections(topBlock, bottomBlock): # devuelve un solo block
    print('* GET INTERSECTION *', topBlock, bottomBlock)
    A1, A2 = topBlock[0], topBlock[1]
    B1, B2 = bottomBlock[0], bottomBlock[1]
    if A1 > B2 or B1 > A2: # case 1 and 5
        return (), [(A1, A2)]
    elif B1 <= A1 and A1 <= B2 and B2 <= A2: # case 2
        leftovers = [] if B2 == A2 else [(B2, A2 - 1)] 
        return (A1, B2), leftovers
    elif B1 >= A1 and B2 <= A2: # case 3
        leftovers = []
        leftovers += [(A1, B1 - 1)] if B1 > A1 else []
        leftovers += [(B2, A2 - 1)] if A2 > B2 else []
        return (A1, B2), leftovers
    elif A1 <= B1 and B1 <= A2 and B2 > A2: # case 4
        leftovers = [(A1, B1 -1)] if B1 > A1 else  []
        return (B1, A2), leftovers 
    elif B1 < A1 and A2 < B2:
        return (A1, A2), []
    return (), []


# Part 2
with open('input5.txt') as openfileobject:
    seeds = []
    leftBehindMap = []
    currentMap = []
    count = 0
    for line in openfileobject:
        line = line.strip()
        currentLeftovers = []
        
        if line.startswith('seeds'):
            seeds = line.split(':')[1].strip().split(' ')
            seeds = list(map(int, seeds))

            topBlocks = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
            topBlocks = [topBlocks[0]] # quitar eta lienas
            print('setting topBlocks', topBlocks)
            allIntersected = topBlocks

        if line == '':
            # if len(currentLeftovers) > 0:
                # leftBehindMap += currentLeftovers
            topBlocksSet = set(topBlocks)
            print('allIntersected:', allIntersected)
            for x in allIntersected:
                if x not in topBlocksSet:
                    topBlocks += [x]
            # topBlocks += [x if x not in topBlocksSet else () for x in allIntersected]
            allIntersected = []
            currentLeftovers = []
            print('----------------------- LINE -----------------------')
            # count += 1
            # if count == 5:
            #     break

        elif line != '' and line[0].isnumeric(): # is searching in map
            print('----------- ANALIZING NEW RANGE ------------')
            sourceBlockStart, destinationBlockStart, width = map(int, line.split(' '))
            sourceBlock = (sourceBlockStart, sourceBlockStart + width)
            destinationBlock = (destinationBlockStart, destinationBlockStart + width)
            diff = destinationBlockStart - sourceBlockStart

            print('sourceBlock:', sourceBlock)
            print('destinationBlock:', destinationBlock)
            print('TOP BLOCKS: ', topBlocks)
            # obtener intersecciones del topblock con el sourceBlock =>  [ I1 ]
            sourceIntersections = []
            for topBlock in topBlocks:
                print('analizing topBlock: ', topBlock)
                sourceIntersection, leftovers = getIntersections(topBlock, sourceBlock)
                print('sourceIntersection: ', sourceIntersection)
                currentLeftovers += leftovers
                print('leftovers: ', leftovers)
                if len(sourceIntersection) > 0:
                    sourceIntersections.append(sourceIntersection)
            
                print("DEL TOP AL SOURCE FINISHED")
            
            destinationBlocks = []
            # obtener intersecciones del sourceIntersection con el destinationBlock =>  [ I1 ]
            for sourceBlock in sourceIntersections:
                print('analizing sourceBlock before: ', sourceBlock)
                diff = destinationBlockStart - sourceBlockStart
                print('diff:', diff)
                destinationBlock = (sourceBlock[0] + diff, sourceBlock[1] + diff)
                destinationBlocks.append(destinationBlock)
                print("DEL SOURCE AL DESTINATION FINISHED")
            
            print('destinationBlocks:', destinationBlocks)
            print('currentLeftovers:', currentLeftovers)
            allIntersected += destinationBlocks
            topBlocks = currentLeftovers

    print('topBlocks: ', topBlocks)        
    # print('leftBehindMap: ', leftBehindMap)        
    # finalMapping = topBlocks + leftBehindMap
    # for finalMap in finalMapping:
        # encontrar el menor de lo que sea que sea esto jaja una lista de tuplas

    # print('Part 1: ', min(seeds))
