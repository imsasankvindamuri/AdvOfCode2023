#boilerplate, setting up vars
import os
import msvcrt as m
import random as r
from time import sleep
snake = [(4,4)]
clear = lambda: os.system("cls")
key = 0
#rng the apple
while True:
    apple = (r.randint(0,8),r.randint(0,8))
    if apple not in snake:
        break
#game loop + 'animation' loop
while True:
    #generate new apple
    if apple == snake[0]:
        while True:
            apple = (r.randint(0,8),r.randint(0,8))
            if apple not in snake:
                break
    #draw new frames
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
    #response window
    sleep(0.5)
    #check for input
    if m.kbhit():
        key = m.getch()
    if key == b'H':
        snake = [(snake[0][0]-1,snake[0][1])] + snake   
        snake.pop()
        key = b'H' #makes the snake move in same direction if no input given
    if key == b'P':
        snake = [(snake[0][0]+1,snake[0][1])] + snake
        snake.pop()
        key == b'P'
    if key == b'K':
        snake = [(snake[0][0],snake[0][1]-1)] + snake
        snake.pop()
        key == b'K'
    if key == b'M':
        snake = [(snake[0][0],snake[0][1]+1)] + snake
        snake.pop()
        key == b'M'
    if key == b'\x1b':
        print("GAME OVER!!") #kill prog in case esc is pressed
        exit()
    #snake growth logic
    if snake[0] == apple:
        if key == b'H':
            snake = snake + [(snake[-1][0]+1,snake[-1][1])]
        if key == b'P':
            snake = snake + [(snake[-1][0]-1,snake[-1][1])]
        if key == b'K':
            snake = snake +  [(snake[-1][0],snake[-1][1]+1)]
        if key == b'M':
            snake = snake + [(snake[-1][0],snake[-1][1]-1)]
    #loss condt
    if (snake[0][0] == 9) or (snake[0][0] == -1) or (snake[0][1] == 9) or (snake[0][1] == -1) or (snake[0] in snake[1:]):
        print("GAME OVER!!!")
        exit()