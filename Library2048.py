from random import randint

def numZeroes(grid):
    ctr = 0
    for row in grid:
        for el in row:
            if el == 0:
                ctr += 1
    return ctr

def genValue(grid):
    tile = randint(1, numZeroes(grid))
    ctr = 0
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                ctr += 1
            if ctr == tile:
                x = randint(1, 10)
                if x == 10:
                    grid[row][col] = 4
                else:
                    grid[row][col] = 2
                return

def printGrid(grid):
    for row in grid:
        print(row)

def copyFourByFour(grid):
    copiedGrid = [([0] * 4) for i in range(4)]
    for row in range(4):
        for col in range(4):
            copiedGrid[row][col] = grid[row][col]
    return copiedGrid

def gridsEqual(grid1, grid2):
    for row in range(4):
        for col in range(4):
            if grid1[row][col] != grid2[row][col]:
                return False
    return True

def shiftLeft(grid):
    newGrid = [([0] * 4) for i in range(4)]
    for row in range(4):
        currentCol = 0
        lastNonZero = -1
        for col in range(4):
            if grid[row][col] != 0:
                if lastNonZero == grid[row][col]:
                    newGrid[row][currentCol-1] *= 2
                    lastNonZero = -1
                else:
                    newGrid[row][currentCol] = grid[row][col]
                    lastNonZero = grid[row][col]
                    currentCol += 1
    return newGrid

def rotateClockwise(grid, times):
    newGrid = copyFourByFour(grid)
    for i in range(times):
        tempGrid = copyFourByFour(newGrid)
        for row in range(4):
            for col in range(4):
                newGrid[col][3-row] = tempGrid[row][col]
    return newGrid

def shiftDown(grid):
    return rotateClockwise(shiftLeft(rotateClockwise(grid, 1)), 3)

def shiftRight(grid):
    return rotateClockwise(shiftLeft(rotateClockwise(grid, 2)), 2)

def shiftUp(grid):
    return rotateClockwise(shiftLeft(rotateClockwise(grid, 3)), 1)

def hasMoves(grid):
    return not (gridsEqual(grid, shiftLeft(grid)) and gridsEqual(grid, shiftRight(grid)) and gridsEqual(grid, shiftUp(grid)) and gridsEqual(grid, shiftDown(grid)))

def getMaxTile(grid):
    maxNum = 0
    for row in grid:
        for el in row:
            if el > maxNum:
                maxNum = el
    return maxNum
