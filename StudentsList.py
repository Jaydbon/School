import pygame         # tell it to use the pygame library of code

pygame.init()                       # activate it

# ******************* VARIABLES ***************************
width,height = 800,600
ballx = 50
bally = 50
play = True

# **************** SETUP THE WINDOW ********************
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ball")
screen.fill((153,136,59))
pygame.display.update()

while play:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pygame.draw.circle(screen,(100,100,100), (ballx, bally),25)
    ballx = ballx+1
    bally = bally+1



    pygame.display.update()
pygame.quit()
