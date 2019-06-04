#!/usr/bin/python

import sys
from graphics import (GraphWin, Rectangle, Point)
import time

def main():
    # the maze
    # w = wall
    # g = gate
    # s = start
    # f = finish
    # v = visited
    maze = [['w','s','w','w','w','w','w','w','w','w'], 
    ['w','g','w','w','g','g','g','g','g','w'],
    ['w','g','w','w','g','w','w','w','g','w'],
    ['w','g','w','w','w','w','g','g','g','w'],
    ['w','g','g','g','g','g','w','w','g','w'],
    ['w','g','w','g','w','w','w','w','g','w'],
    ['w','g','w','g','w','g','g','g','g','w'],
    ['w','g','w','g','w','g','w','w','g','w'],
    ['w','g','w','g','g','g','g','w','g','f'],
    ['w','w','w','w','w','w','w','w','w','w']]

    # start and finis location
    startpos_x = 1
    startpos_y = 0

    # maze dimensions
    maze_width = 10
    maze_height = 10
    block_dim = 25

    win = GraphWin("My Maze", block_dim*2+maze_width*block_dim, block_dim*2+maze_height*block_dim)

    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == 'w':
                drawGrid(win, x, y, 'green', block_dim)
            else:
                drawGrid(win, x, y, 'white', block_dim)

    visitNextPosition(startpos_x, startpos_y, maze, win, block_dim)

    win.getMouse() # Pause to view result
    win.close()

def drawGrid(window, x, y, color, block_dim):
    xpos = (x + 1) * block_dim
    ypos = (y + 1) * block_dim
    rect = Rectangle(Point(xpos, ypos), Point(xpos+block_dim, ypos+block_dim))
    rect.setFill(color)
    rect.draw(window)

# function to visit all neighbouring (left, right, top, bottom) visitable positions
def visitNextPosition(x, y, maze, window, block_dim):
    maze[x][y] = 'v'

    if maze[x][y] == 'f':
        drawGrid(window, x, y, 'blue', block_dim)
        return

    drawGrid(window, x, y, 'yellow', block_dim)

    time.sleep(.5)

    if isVisitable(x-1, y, maze):
        visitNextPosition(x-1, y, maze, window, block_dim)

    if isVisitable(x+1, y, maze):
        visitNextPosition(x+1, y, maze, window, block_dim)

    if isVisitable(x, y-1, maze):
        visitNextPosition(x, y-1, maze, window, block_dim)

    if isVisitable(x, y+1, maze):
        visitNextPosition(x, y+1, maze, window, block_dim)

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

