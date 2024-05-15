import pygame
import random
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
foodx = random.randint(10,710)
foody = random.randint(10,710)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False
        if event.type == pygame.KEYDOWN:
            foodx = random.randint(30,680)
            foody = random.randint(30,680)
    screen.fill("black")
    pygame.draw.rect(screen,"Red",pygame.Rect(foodx,foody,30,30))
    pygame.display.flip()

    clock.tick(60) 
pygame.quit()
