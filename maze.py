#!/usr/bin/python

import sys
from graphics import *
import time

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

# execution limit
function_call_limit = 100
function_call_count = 0

def main():
    win = GraphWin("My Maze", 1000, 1000)

    for x in range(len(maze)):
        for y in range(len(maze[x])):
            print('x: %s, y: %s' % (x, y))

            if maze[x][y] == 'w':
                drawGrid(win, x, y, 'green')
            else:
                drawGrid(win, x, y, 'white')

    visitNextPosition(startpos_x, startpos_y, win)

    win.getMouse() # Pause to view result
    win.close()

def drawGrid(window, x, y, color):
    xpos = (x + 1) * 50
    ypos = (y + 1) * 50
    rect = Rectangle(Point(xpos, ypos), Point(xpos+50, ypos+50))
    rect.setFill(color)
    rect.draw(window)

# function to visit all neighbouring (left, right, top, bottom) visitable positions
def visitNextPosition(x, y, window):
    global function_call_count
    global maze

    function_call_count += 1
    print('x: %s, y: %s' % (x, y))
    maze[x][y] = 'v'

    if maze[x][y] == 'f':
        drawGrid(window, x, y, 'blue')
        return

    drawGrid(window, x, y, 'yellow')

    time.sleep(1)

    if not isVisitable(x-1, y):
        visitNextPosition(x-1, y, window)

    if not isVisitable(x+1, y):
        visitNextPosition(x+1, y, window)

    if not isVisitable(x, y-1):
        visitNextPosition(x, y-1, window)

    if not isVisitable(x, y+1):
        visitNextPosition(x, y+1, window)

    return

def isVisitable(x, y):
    if maze[x][y] == 'v' or maze[x][y] == 'w' or x < 0 or x > maze_width-1 or y < 0 or y > maze_height-1:
        return True
    else:
        return False

main()

