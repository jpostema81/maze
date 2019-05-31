#!/usr/bin/python

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

# start and finis location
start = [1,0]
finish = [9,8]

# function to visit all neighbouring (left, right, top, bottom) visitable positions
def visitNextPosition(pos):
    
    print(isWall([pos]))

# check if pos is a wall
def isWall(pos):
    if pos in maze:
        return True
    else:
        return False

visitNextPosition(start)

