# WIP

from Library2048 import *
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

grid = [([0] * 4) for i in range(4)]
tempGrid = copyFourByFour(grid)
    
genValue(grid)

running = True
while running:
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
    running = hasMoves(grid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
