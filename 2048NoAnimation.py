from Library2048 import *

grid = [([0] * 4) for i in range(4)]
tempGrid = copyFourByFour(grid)
    
genValue(grid)
while hasMoves(grid):
    if not gridsEqual(grid, tempGrid):
        genValue(grid)
    tempGrid = copyFourByFour(grid)
    printGrid(grid)
    move = input("Enter your move: ")
    if move == "a":
        grid = shiftLeft(grid)
    elif move == "s":
        grid = shiftDown(grid)
    elif move == "d":
        grid = shiftRight(grid)
    elif move == "w":
        grid = shiftUp(grid)

    print("HIGHEST TILE: " + str(getMaxTile(grid)))
