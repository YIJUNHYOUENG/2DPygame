import pygame
import time

pygame.init()

width = 800
height = 480

count = 0

background = pygame.display.set_mode((width, height))
pygame.display.set_caption("main")

font = pygame.font.SysFont("arial",120, True, False)
font1 = pygame.font.SysFont("arial",80, True, False)


play = True
while play:
    
    if count == 1:
        text = font.render("Tetris",True, (255,255,255))
        background.blit(text,(270,170))
    elif count == 2:
        text = font.render("Game1",True, (255,255,255))
        background.blit(text,(260,170))
    elif count == 0:
        text = font1.render("chose 'left' or 'right'",True,(255,255,255))
        background.blit(text,(100,190))
        
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.type == pygame.QUIT:
                play = False
            if event.key == pygame.K_a:
                if count == 0:
                    count = 1
                if count == 2:
                    count-=1
            elif event.key == pygame.K_d:
                if count == 0:
                    count = 2
                if count == 1:
                    count+=1
            elif event.key == pygame.K_j:
                if count == 1:
                    exec(open("tetris.py").read())
                elif count == 2:
                    exec(open("mario.py").read())


                        
    pygame.display.update()
    background.fill((0,0,0))
pygame.quit()
