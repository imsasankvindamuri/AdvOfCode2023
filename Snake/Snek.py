import os
import msvcrt as m
lst = [(4,4),(5,4),(6,4)]
clear = lambda: os.system("cls")
count = 0
while True:
    grid = [["□" for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if (i,j) in lst:
                grid[i][j] = "■"                        
    clear()
    for row in grid:
        print(" ".join(row))
    key = m.getch()
    if key == b'H':
        lst = [(lst[0][0]-1,lst[0][1])] + lst
        lst.pop()
    if key == b'P':
        lst = [(lst[0][0]+1,lst[0][1])] + lst
        lst.pop()
    if key == b'K':
        lst = [(lst[0][0],lst[0][1]-1)] + lst
        lst.pop()
    if key == b'M':
        lst = [(lst[0][0],lst[0][1]+1)] + lst
        lst.pop()
    if key == b'\x1b':
        exit()
    count +=1