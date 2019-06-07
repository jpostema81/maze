#!/usr/bin/python

import sys
from graphics import (GraphWin, Rectangle, Point)
import time
import random

def main():
    # start and finis location
    startPosX = 1
    startPosY = 0

    # maze dimensions
    mazeWidth = 10
    mazeHeight = 10
    blockDim = 25

    window = GraphWin("My Maze", blockDim*2+mazeWidth*blockDim, blockDim*2+mazeHeight*blockDim)
    maze = createDynamicMaze(mazeWidth, mazeHeight)
    drawMaze(window, maze, blockDim)
    visitNextPosition(startPosX, startPosY, maze, mazeWidth, mazeHeight, window, blockDim)
    window.getMouse() # Pause to view result
    window.close()

#create hard-coded maze
def createStaticMaze(mazeWidth, mazeHeight):
    # the maze
    # w = wall
    # g = gate
    # s = start
    # f = finish
    # v = visited
    return [['w','s','w','w','w','w','w','w','w','w'], 
        ['w','g','w','w','g','g','g','g','g','w'],
        ['w','g','w','w','g','w','w','w','g','w'],
        ['w','g','w','w','w','w','g','g','g','w'],
        ['w','g','g','g','g','g','w','w','g','w'],
        ['w','g','w','g','w','w','w','w','g','w'],
        ['w','g','w','g','w','g','g','g','g','w'],
        ['w','g','w','g','w','g','w','w','g','w'],
        ['w','g','w','g','g','g','g','w','g','f'],
        ['w','w','w','w','w','w','w','w','w','w']]

#create dynamic generated maze
def createDynamicMaze(mazeWidth, mazeHeight):
    maze = [['w' for x in range(mazeWidth)] for y in range(mazeHeight)]

    createNextGate(1, 0, 2, maze, mazeWidth, mazeHeight)

    # for y in range(mazeHeight):
    #     maze[y][1] = 'g'

    # maze[mazeHeight-1][1] = 'f'
    return maze

# direction:
# 1 = up
# 2 = down
# 3 = left
# 4 = right
def createNextGate(x, y, direction, maze, mazeWidth, mazeHeight):
    maze[y][x] = 'g'
    print("add gate at position: %s, %s" % (x, y))
    print("current direction: %s" % direction)

    # decide to split track or keep current direction or both, 10% chance
    doSplit = random.randint(1, 10)

    if doSplit == 1:
        direction = random.choice(range(4).pop(direction))
        print("split track to direction: %s" % direction)

    if direction == 1:
        if y > 0:
            createNextGate(x, y-1, direction, maze, mazeWidth, mazeHeight)
        else:
            return False
    if direction == 2:
        if y < mazeHeight-1:
            createNextGate(x, y+1, direction, maze, mazeWidth, mazeHeight)
        else:
            direction = (direction + 1) % 4
            print("split track to direction: %s" % direction)
            return False
    if direction == 3:
        if x > 0:
            createNextGate(x-1, y, direction, maze, mazeWidth, mazeHeight)
        else:
            return False
    if direction == 4:
        if x > mazeWidth-1:
            createNextGate(x+1, y, direction, maze, mazeWidth, mazeHeight)
        else:
            return False

    return False

def drawMaze(window, maze, blockDim):
    for y in range(len(maze)):
        for x in range(len(maze[y])):            
            if maze[y][x] == 'w':
                drawBlock(window, x, y, 'black', blockDim)
            elif maze[y][x] == 'g':
                drawBlock(window, x, y, 'white', blockDim)
            elif maze[y][x] == 's':
                drawBlock(window, x, y, 'blue', blockDim)
            elif maze[y][x] == 'f':
                drawBlock(window, x, y, 'green', blockDim)

def drawBlock(window, x, y, color, blockDim):
    xPos = (x + 1) * blockDim
    yPos = (y + 1) * blockDim
    rect = Rectangle(Point(xPos, yPos), Point(xPos+blockDim, yPos+blockDim))
    rect.setFill(color)
    rect.draw(window)

# function to visit all neighbouring (left, right, top, bottom) visitable positions
def visitNextPosition(x, y, maze, mazeWidth, mazeHeight, window, blockDim):
    maze[y][x] = 'v'

    if maze[y][x] == 'f':
        return

    drawBlock(window, x, y, 'yellow', blockDim)
    time.sleep(.3)

    if isVisitable(x-1, y, maze, mazeWidth, mazeHeight):
        visitNextPosition(x-1, y, maze, mazeWidth, mazeHeight, window, blockDim)

    if isVisitable(x+1, y, maze, mazeWidth, mazeHeight):
        visitNextPosition(x+1, y, maze, mazeWidth, mazeHeight, window, blockDim)

    if isVisitable(x, y-1, maze, mazeWidth, mazeHeight):
        visitNextPosition(x, y-1, maze, mazeWidth, mazeHeight, window, blockDim)

    if isVisitable(x, y+1, maze, mazeWidth, mazeHeight):
        visitNextPosition(x, y+1, maze, mazeWidth, mazeHeight, window, blockDim)

    return

def isVisitable(x, y, maze, mazeWidth, mazeHeight):
    if x < 0 or x > mazeWidth-1 or y < 0 or y > mazeHeight-1 or maze[y][x] == 'v' or maze[y][x] == 'w':
        return False
    else:
        return True

main()

