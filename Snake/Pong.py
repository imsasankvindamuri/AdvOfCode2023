import os
import msvcrt as m
from time import sleep
clear = lambda: os.system("cls")
class player:
    def __init__(self,pos):
        self.pos = pos
        self.score = 0
    def playerMove(self,key):
        if key == b'K':
            if (self.pos[1]-1 > -1):
                self.pos = (self.pos[0],self.pos[1]-1)
        if key == b'M':
            if (self.pos[1]+1 < 17):
                self.pos = (self.pos[0],self.pos[1]+1)
        else:
            pass
class ball:
    def __init__(self,speed,pos):
        self.speed = speed
        self.pos = pos
board = player((8,8))
while True:
    grid = [["□" for i in range(17)] for j in range(9)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) == board.pos:
                grid[i][j] = "_"
    clear()
    for row in grid:
        print(" ".join(row))
    #response window
    sleep(0.05)
    #check for input
    if m.kbhit():
        key = m.getch()
        board.playerMove(key)