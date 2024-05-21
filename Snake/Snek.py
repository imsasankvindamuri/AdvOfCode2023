import os
import msvcrt as m
import random as r
snake = [(4,4)]
clear = lambda: os.system("cls")
while True:
    apple = (r.randint(0,8),r.randint(0,8))
    if apple not in snake:
        break
while True:
    if apple == snake[0]:
        while True:
            apple = (r.randint(0,8),r.randint(0,8))
            if apple not in snake:
                break
    grid = [["□" for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if (i,j) == apple:
                grid[i][j] = "●"
            if (i,j) in snake:
                grid[i][j] = "■"                        
    clear()
    for row in grid:
        print(" ".join(row))
    key = m.getch()
    if key == b'H':
        snake = [(snake[0][0]-1,snake[0][1])] + snake   
        snake.pop()
    if key == b'P':
        snake = [(snake[0][0]+1,snake[0][1])] + snake
        snake.pop()
    if key == b'K':
        snake = [(snake[0][0],snake[0][1]-1)] + snake
        snake.pop()
    if key == b'M':
        snake = [(snake[0][0],snake[0][1]+1)] + snake
        snake.pop()
    if key == b'\x1b':
        print("GAME OVER!!")
        exit()
    if snake[0] == apple:
        if key == b'H':
            snake = snake + [(snake[-1][0]+1,snake[-1][1])]
        if key == b'P':
            snake = snake + [(snake[-1][0]-1,snake[-1][1])]
        if key == b'K':
            snake = snake +  [(snake[-1][0],snake[-1][1]+1)]
        if key == b'M':
            snake = snake + [(snake[-1][0],snake[-1][1]-1)]
    if (snake[0][0] == 9) or (snake[0][0] == -1) or (snake[0][1] == 9) or (snake[0][1] == -1) or (snake[0] in snake[1:]):
        print("GAME OVER!!!")
        exit()