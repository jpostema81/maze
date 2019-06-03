#!/usr/bin/python

import sys
from graphics import *
import time

# the maze. these positions present walls
maze = [
        [0,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],
        [0,1],[2,1],[3,1],[9,1],
        [0,2],[2,2],[3,2],[5,2],[6,2],[7,2],[9,2],
        [0,3],[2,3],[3,3],[4,3],[5,3],[9,3],
        [0,4],[6,4],[7,4],[9,4],
        [0,5],[2,5],[4,5],[5,5],[6,5],[7,5],[9,5],
        [0,6],[2,6],[4,6],[9,6],
        [0,7],[2,7],[4,7],[6,7],[7,7],[9,7],
        [0,8],[2,8],[7,8],
        [0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9]
    ]

# save already tried positions to prevent repitition
already_tried = []

# start and finis location
start = [1,0]
finish = [9,8]

# maze dimensions
maze_width = 9
maze_height = 9

# execution limit
function_call_limit = 100
function_call_count = 0

def main():
    win = GraphWin("My Maze", 1000, 1000)

    for x in range(maze_width+1):
        for y in range(maze_height+1):
            pos = [x, y]

            if pos in maze:
                drawGrid(win, pos, 'green')
            else:
                drawGrid(win, pos, 'white')

    visitNextPosition(start, win)

    win.getMouse() # Pause to view result
    win.close()

def drawGrid(window, pos, color):
    x = (pos[0] + 1) * 50
    y = (pos[1] + 1) * 50
    rect = Rectangle(Point(x, y), Point(x+50, y+50))
    rect.setFill(color)
    rect.draw(window)

# function to visit all neighbouring (left, right, top, bottom) visitable positions
def visitNextPosition(pos, window):
    global function_call_count

    function_call_count += 1
    already_tried.append(pos)

    if pos == finish:
        print("found finish at position %s" % pos)
        drawGrid(window, pos, 'blue')
        return

    print("discovering position %s" % pos)
    drawGrid(window, pos, 'yellow')

    time.sleep(1)

    if function_call_count >= function_call_limit:
        print("max function call count reached")
        return

    top = [pos[0], pos[1]-1]
    bottom = [pos[0], pos[1]+1]
    left = [pos[0]-1, pos[1]]
    right = [pos[0]+1, pos[1]]

    if top not in already_tried:
        print("checking top position")
        if not isWall(top):
            visitNextPosition(top, window)
    else:
        print("location %s already visited" % top)

    if bottom not in already_tried:
        print("checking bottom position")
        if not isWall(bottom):
            visitNextPosition(bottom, window)
    else:
        print("location %s already visited" % bottom)

    if left not in already_tried:
        if not isWall(left):
            print("checking left position")
            visitNextPosition(left, window)
    else:
        print("location %s already visited" % left)

    if right not in already_tried:
        if not isWall(right):
            print("checking right position")
            visitNextPosition(right, window)
    else:
        print("location %s already visited" % right)

    print("reached return condition")
    return

# check if pos is a wall or a position outside the maze grid
def isWall(pos):
    if pos in maze or pos[0] < 0 or pos[0] > 9 or pos[1] < 0 or pos[1] > 9:
        print("next position %s is an inaccessable position" % pos)
        return True
    else:
        print("next position %s is an accessable position" % pos)
        return False

main()

