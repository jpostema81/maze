#!/usr/bin/python

import sys
from graphics import (GraphWin, Rectangle, Point)
import time

def main():
    # start and finis location
    startPosX = 1
    startPosY = 0

    # maze dimensions
    mazeWidth = 10
    mazeHeight = 10
    blockDim = 25

    window = GraphWin("My Maze", blockDim*2+mazeWidth*blockDim, blockDim*2+mazeHeight*blockDim)
    maze = createMaze(True)
    drawMaze(window, maze, blockDim)
    visitNextPosition(startPosX, startPosY, maze, window, blockDim)
    window.getMouse() # Pause to view result
    window.close()

def createMaze(returnStaticMaze):
    if(returnStaticMaze):
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
    else:
        return False

def drawMaze(window, maze, blockDim):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == 'w':
                drawBlock(window, x, y, 'green', blockDim)
            else:
                drawBlock(window, x, y, 'white', blockDim)

def drawBlock(window, x, y, color, blockDim):
    xPos = (x + 1) * blockDim
    yPos = (y + 1) * blockDim
    rect = Rectangle(Point(xPos, yPos), Point(xPos+blockDim, yPos+blockDim))
    rect.setFill(color)
    rect.draw(window)

# function to visit all neighbouring (left, right, top, bottom) visitable positions
def visitNextPosition(x, y, maze, window, blockDim):
    maze[x][y] = 'v'

    if maze[x][y] == 'f':
        drawBlock(window, x, y, 'blue', blockDim)
        return

    drawBlock(window, x, y, 'yellow', blockDim)
    time.sleep(.5)

    if isVisitable(x-1, y, maze):
        visitNextPosition(x-1, y, maze, window, blockDim)

    if isVisitable(x+1, y, maze):
        visitNextPosition(x+1, y, maze, window, blockDim)

    if isVisitable(x, y-1, maze):
        visitNextPosition(x, y-1, maze, window, blockDim)

    if isVisitable(x, y+1, maze):
        visitNextPosition(x, y+1, maze, window, blockDim)

    return

def isVisitable(x, y, maze):
    try:
        if maze[x][y] == 'v' or maze[x][y] == 'w':
            return False
        else:
            return True
    except IndexError:
        return False

main()

