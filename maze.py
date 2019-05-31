#!/usr/bin/python

import sys

# the maze. these positions present walls
maze = [
        [0,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],
        [0,1],[2,1],[3,1],[9,1],
        [0,2],[2,2],[3,2],[5,2],[6,2],[7,2],[9,2],
        [0,3],[2,3],[3,3],[4,3],[5,3],[9,3],
        [0,4],[6,4],[7,4],[9,4],
        [0,5],[2,5],[4,5],[5,5],[6,5],[7,5],[9,5],
        [0,6],[2,6],[4,6],[6,6],[7,6],[9,6],
        [0,7],[2,7],[4,7],[6,7],[7,7],[9,7],
        [0,8],[2,8],[7,8],
        [0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9]
    ]

# save already tried positions to prevent repitition
already_tried = []

# start and finis location
start = [1,0]
finish = [9,8]

# execution limit
function_call_limit = 10
function_call_count = 0

# function to visit all neighbouring (left, right, top, bottom) visitable positions
def visitNextPosition(pos):
    global function_call_count
    function_call_count += 1
    already_tried.append(pos)

    print("discovering position %s" % pos)

    if function_call_count >= function_call_limit:
        print("max function call count reached")
        sys.exit()

    top = [pos[0], pos[1]-1]
    bottom = [pos[0], pos[1]+1]
    left = [pos[0]-1, pos[1]]
    right = [pos[0]+1, pos[1]]

    if top not in already_tried:
        print("checking top position")
        if not isWall(top):
            visitNextPosition(top)
    else:
        print("location already visited")

    if bottom not in already_tried:
        print("checking bottom position")
        if not isWall(bottom):
            visitNextPosition(bottom)
    else:
        print("location already visited")

    if left not in already_tried:
        if not isWall(left):
            print("checking left position")
            visitNextPosition(left)
    else:
        print("location already visited")

    if right not in already_tried:
        if not isWall(right):
            print("checking right position")
            visitNextPosition(right)
    else:
        print("location already visited")

    print("reached return condition")
    return

# check if pos is a wall or a position outside the maze grid
def isWall(pos):
    if pos in maze or pos[0] < 0 or pos[1] < 0 or pos:
        return True
    else:
        return False

visitNextPosition(start)
