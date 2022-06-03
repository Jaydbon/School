# Jayden Barber
# 2022 05 01
# Barber_Jayden_pong.py
# this program is a pygame version of pong
import random
import pygame
pygame.init()

# ******************* VARIABLES ***************************
width,height = 800,600
ball1x = int(random.uniform(25, 775))
ball1y = 100 # starting position
ballR = 25
rectx = 300
recty = 450
ball1DY = 4 # direction
ball1DX = 4
intScore = 0
intlives = 3
rectLength = 250
ballColour = int(random.uniform(0,255)), int(random.uniform(1,255)), int(random.uniform(1,255))
play = True

# ************** FUNCTIONS **********************
def Score():
    global intScore
    text = font.render("Score:" + str(intScore), True,(255,255,0),(6,57,112))
    textRECT = text.get_rect() 
    textRECT = (0,567)         # Location
    screen.blit(text, textRECT)  # put this object on the screen

def Lives():
    global intlives
    text = font.render("Lives:" + str(intlives), True,(255,255,0),(6,57,112))
    textRECT = text.get_rect() 
    textRECT = (0,534)         # Location
    screen.blit( text, textRECT)  # put this object on the screen


# **************** SETUP THE WINDOW ********************
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ball")
screen.fill((37, 150, 190))
pygame.display.update()
font = pygame.font.Font('freesansbold.ttf',32) # sets the font

while play:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.draw.rect(screen,(6,57,112),(0,0,800,600))
    pygame.draw.circle(screen,(ballColour),(ball1x ,ball1y),ballR) # location at center and radius
    pygame.draw.rect(screen,(255,255,255),(rectx,recty,rectLength,20))

    # Move the ball
    ball1x = ball1x + ball1DX
    ball1y = ball1y + ball1DY
    if (ball1y - ballR <= 0): # ball hitting top
        ball1DY = ball1DY * -1
    if (ball1x - ballR <= 0 or ball1x + ballR > width):
        ball1DX = ball1DX * -1

    
    # Moving the slider
    keys = pygame.key.get_pressed() # check for key press
    if keys[pygame.K_LEFT]:
        rectx = rectx - 5
        if rectx <= 0:
            rectx = 0
    elif keys[pygame.K_RIGHT]:
        rectx = rectx + 5
        if rectx >= width - rectLength:
            rectx = width - rectLength


#********** check for colide *******
    if (ball1y + ballR > recty and ball1x + ballR > rectx and ball1x < rectx + rectLength and ball1y < recty + ballR):
        ball1DY = ball1DY * -1  # switches direction
        intScore = intScore + 10
        ballColour = int(random.uniform(1,255)), int(random.uniform(1,255)), int(random.uniform(1,255))

    # paddle shrinks per 50 points
        if int(intScore) >= 50:
            if int(intScore)/50 < 2: # divides by 50 to check for level 50 = 1 100 = 2 etc
                rectLength = 200
            elif int(intScore)/50 < 3:
                rectLength = 150
            elif int(intScore)/50 < 4:
                rectLength = 100
            elif int(intScore)/50 < 5:
                rectLength = 50
    Score()


#************** Lives *******************
    if ball1y >= 600:
        ball1x = 100
        ball1y = 100
        intlives = intlives - 1
        ball1x = int(random.uniform(25, 775))
    Lives()

# ************** Speed up ****************



# *********** Game Over************
    if intlives <= 0:
        text = font.render("YOU LOST", True,(255,255,0),(6,57,112))
        textRECT = text.get_rect() 
        textRECT = (300, 300)
        screen.blit(text, textRECT) 
        text = font.render("With a score of " + str(intScore), True,(255,255,0),(6,57,112))
        textRECT = text.get_rect() 
        textRECT = (300, 333)
        screen.blit(text, textRECT)
        ball1DY = 0
        ball1DX = 0
        text = font.render("Press Enter To Play Again", True,(255,255,0),(6,57,112))
        textRECT = text.get_rect() 
        textRECT = (300, 399)
        screen.blit(text, textRECT)
        if keys[pygame.K_RETURN]:
            intlives = 3
            ball1DY = 4
            ball1DX = 4
            intScore = 0
            rectLength = 250
            ball1x = int(random.uniform(25, 775))




    #************* end of the loop **************
    pygame.display.update()
pygame.quit() # closes the game window
