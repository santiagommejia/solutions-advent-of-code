def countVisible(matrix, rows, cols):
    visible = 0
    for i in range(rows):
        for j in range(cols):
            visible += 1 if matrix[i][j] else 0
    return visible

def getScenicScore(value, xPos, yPos, row, col):
    toLeft = 0
    for i in range(yPos, 0, -1):
        toLeft += 1
        if row[i -1] >= value:
            break
    toRight = 0
    for i in range(yPos, len(row) - 1):
        toRight += 1
        if row[i + 1] >= value:
            toRight += 1
            break
    toTop = 0
    for i in range(xPos, 0, -1):
        toTop += 1
        if col[i - 1] >= value:
            break
    toBottom = 0
    for i in range(xPos, len(col) - 1):
        toBottom += 1
        if col[i + 1] >= value:
            break
    return toLeft * toRight * toTop * toBottom


# Part 1    
with open('input8.txt') as openfileobject:
    matrix = []
    for line in openfileobject:
        splitLine = list(map(int, line.replace('\n', '').strip()))
        matrix.append(splitLine)
    cols = len(matrix[0])
    rows = len(matrix)
    visibleMatrix = [[False for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        rowMaxSoFarFromLeft = matrix[i][0]
        rowMaxSoFarFromRight = matrix[i][cols - 1]
        for j in range(cols):
            if i == 0 or i == rows - 1: # this should mark first and last row as true
                visibleMatrix[i][j] = True
            if matrix[i][j] > rowMaxSoFarFromLeft:
                visibleMatrix[i][j] = True
                rowMaxSoFarFromLeft = matrix[i][j]
            if matrix[i][cols - j - 1] > rowMaxSoFarFromRight:
                visibleMatrix[i][cols - j - 1] = True
                rowMaxSoFarFromRight = matrix[i][cols - j - 1]
    
    for i in range(cols):
        colMaxSoFarFromTop = matrix[0][i]
        colMaxSoFarFromBottom = matrix[rows - 1][i]
        for j in range(rows):
            if i == 0 or i == cols - 1: # this should mark first and last col as true
                visibleMatrix[j][i] = True
            if matrix[j][i] > colMaxSoFarFromTop:
                visibleMatrix[j][i] = True
                colMaxSoFarFromTop = matrix[j][i]
            if matrix[rows - j - 1][i] > colMaxSoFarFromBottom:
                visibleMatrix[rows - j - 1][i] = True
                colMaxSoFarFromBottom = matrix[rows - j - 1][i]
    print(countVisible(visibleMatrix,rows,cols))

# Part 2
with open('input8.txt') as openfileobject:
    matrix = []
    for line in openfileobject:
        splitLine = list(map(int, line.replace('\n', '').strip()))
        matrix.append(splitLine)
    cols = len(matrix[0])
    rows = len(matrix)
    visibleMatrix = [[False for _ in range(cols)] for _ in range(rows)]
    maxScore = 0
    columns = list(zip(*matrix))
    for i in range(rows):
        if i == 0 or i == rows -1:
            continue
        for j in range(cols):
            if j == 0 or j == cols - 1:
                continue
            score = getScenicScore(matrix[i][j], i, j, matrix[i], list(columns[j]))
            if score > maxScore:
                maxScore = score
    print(maxScore)





