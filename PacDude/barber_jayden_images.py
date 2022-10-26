import random
import pygame
pygame.init()
win_W,win_H = 800,800
brd_W,brd_H = 800, 600
play = True
spookDirx = 2
spookDiry = 2
ppX = brd_W/2
ppY = brd_H/2
pwrPillOn = True
pwrUP = False
pwrUPtime = 0
score = 0
lives = 3
cherryX, cherryY = random.randint(0,600), 0


board = pygame.Surface((brd_W, brd_H)) # the board for pacman and spook
screen = pygame.display.set_mode((win_W,win_H))
pygame.display.set_caption("pacdude")
screen.fill((0,0,255))
pygame.display.update()
font = pygame.font.Font('freesansbold.ttf',32) # sets the font
pwrPillTime = pygame.time.get_ticks()


# ********** Load the images into objects
# look in the images folder for images
pRO = pygame.image.load('images\PMRO.png')
pRC = pygame.image.load('images\PMRC.png')
pDO = pygame.image.load('images\PMDO.png')
pDC = pygame.image.load('images\PMDC.png')
pUO = pygame.image.load('images\PMUO.png')
pUC = pygame.image.load('images\PMUC.png')
pLO = pygame.image.load('images\PMLO.png')
pLC = pygame.image.load('images\PMLC.png')
GPL = pygame.image.load('images\GPL.png')
GPR = pygame.image.load('images\GPR.png')
sRIP1 = pygame.image.load('images\GRIP1.png')
sRIP2 = pygame.image.load('images\GRIP2.png')
p_pill = pygame.image.load('images\p_pill.png')
PMHA = pygame.image.load('images\PMHA.png')
PMHD = pygame.image.load('images\PMHD.png')
cherry = pygame.image.load('images\cherry.png')

pacImg = pRO
spookImg = GPL

spookLOC = pygame.Rect(300,300,50, 50) # setting up locations
pacLOC = pygame.Rect(0,0,50,50)



# Loading Images
def draw_window(pacInfo):
    blueBG = (0,0,255)
    screen.fill(blueBG)
    screen.blit(pacImg, (pacLOC.x, pacLOC.y)) # draw pacdude on screen

def draw_spook(spookInfo):
    screen.blit(spookImg, (spookLOC.x, spookLOC.y))





#ghost movement
def spookMove():
    global spookDirx, spookDiry, spookImg
    
    if (spookLOC.y + spookLOC.height + spookDiry >= brd_H or spookLOC.y + spookDiry <= 0): # bouncing off sides
        spookDiry = spookDiry * -1
        chgDir = random.randint(0,4)
        if chgDir >=3:
            spookDirx = spookDirx * -1
            
    if (spookLOC.x <= 0 or spookLOC.x > 750):
        spookDirx = spookDirx * -1
        if spookDirx<= 0:
          spookImg = GPL
        else:
            spookImg = GPR

    chgDir = random.randint(0,10000) # random direction change
    if chgDir >=9995:
        spookDiry = spookDiry * -1
    if chgDir >= 9995:
        spookDirx = spookDirx * -1

    spookLOC.x = spookLOC.x + spookDirx
    spookLOC.y = spookLOC.y + spookDiry


# checking for pacdude coliding with objects
def colideCheck():
    global spookImg, pacImg, pwrUP, pwrUPtime, pwrPillOn, cherryX, cherryY, score, cherry, lives
    pp_rect = p_pill.get_rect(topleft = (ppX, ppY))
    pac_rect = pacImg.get_rect(topleft = (pacLOC.x, pacLOC.y))
    spook_rect = spookImg.get_rect(topleft = (spookLOC.x, spookLOC.y))
    cherry_rect = cherry.get_rect(topleft = (cherryX, cherryY))
    
    if pwrUP == True:   # if pacdude is powered and coliding with ghost
        if pac_rect.colliderect(spook_rect):
            spookImg == GPR
        if pac_rect.colliderect(spook_rect):
            spookImg = sRIP1
        
            for x in range(10): # ghost blinking
                screen.blit(spookImg, (spookLOC.x, spookLOC.y))
                pygame.display.update(spookLOC.x, spookLOC.y,50,50)
                pygame.time.delay(100)
                if spookImg == sRIP1:
                    spookImg = sRIP2
                else:
                    spookImg = sRIP1
            spookImg = GPR
            spookLOC.x = random.randint(100, 500)   # random location
            spookLOC.y = random.randint(100, 500)
    else:
        if pac_rect.colliderect(spook_rect):
            pacImg == pRO
        if pac_rect.colliderect(spook_rect):
            pacImg = PMHA
        
            for x in range(10): # pacdude blinking death
                screen.blit(pacImg, (pacLOC.x, pacLOC.y))
                pygame.display.update(pacLOC.x, pacLOC.y,50,50)
                pygame.time.delay(100)
                if pacImg == PMHA:
                    pacImg = PMHD
                else:
                    pacImg = PMHA
            pacImg = pRO
            pacLOC.x = random.randint(100, 500)
            pacLOC.y = random.randint(100, 500)
            lives = lives - 1   # removes 1 life after death
            
    if pac_rect.colliderect(pp_rect):   #colision with power pill
        pwrUPtime = pygame.time.get_ticks() + 7500  # setting the time the pill lasts for
        pwrUP = True
        pwrPillOn = False
        
    if pac_rect.colliderect(cherry_rect):   # coliding with cherry
        cherryX = random.randint(0,600) # random spawn for cherry and make it start at the top
        cherryY = 0
        score = score + 10  # add to score
        
    


# powering up pacdude and showing it
def powerUP():
    global pwrUP, pwrUPtime, brd_W, currTime, cntDOWN
    if pwrUP == True:
        currTime = pygame.time.get_ticks()
        timeLEFT = pwrUPtime - pygame.time.get_ticks()
        pygame.draw.rect(screen, (0,0,0), (brd_W/2-25, 625, 50, 150))
        textPOWER = font.render('POWER UP', True, (255,255,255))
        screen.blit(textPOWER, (320, 775))
        if  timeLEFT <= 0:
            pwrUP = False
        else:
            cntDOWN = (timeLEFT/7500)*150  # formula to make the rectangle shrink to remove time
            pygame.draw.rect(screen, (255,255,255), (brd_W/2-25, 625, 50, cntDOWN))
    else:
        pygame.draw.rect(screen, (0,0,255), (brd_W/2-100, 625, 200, 200))   # cover up timer when over





def powerPill():
    global pwrPillTime, pwrPillOn, pwrPill,ppX,ppY, pwrUPtime, pwrUP
    if pwrUP == True:   # do nothing if pacdude is powered
        return()
    pwrPill = random.randint(0,100)
    if pwrPill >= 99:   # random respawn for pill
        if pwrPillOn == False:
            pwrPillOn= True
            pwrPillTime = pygame.time.get_ticks()
            ppRand = random.randint(200,brd_W/2)
            if pacLOC.x >= brd_W/2:
                ppX = pacLOC.x - ppRand # avoiding pill spawning on pacdude
            else:
                ppX = pacLOC.x + ppRand

            if pacLOC.y >= brd_H/2:
                ppY = pacLOC.y - ppRand
            else:
                ppY = pacLOC.y + ppRand
           
    if pwrPillOn == True:   
        screen.blit(p_pill, (ppX, ppY)) 
        currTime = pygame.time.get_ticks()
        pygame.display.update(ppX,ppY,30,30)
        
        if currTime - pwrPillTime > 7500:
            pwrPillOn = False
        
# socre boards
def gui():
    global score, lives
    scoreBoard = font.render('Score: ' + str(score), True, (255,255,255))   # score placement
    screen.blit(scoreBoard, (0, 620))

    livesBoard = font.render('Lives: ' + str(lives), True, (255,255,255))   # lives placement
    screen.blit(livesBoard, (0, 650))


# ending the game
def gameOver():
    global cherryY, spookDirx, spookDiry, ppX, ppY, score, keys, lives, pwrUP, score
    if lives <= 0:
        pacLOC.x, pacLOC.y = 0,0
        cherryY = 0
        spookDirx, spookDiry = 0,0
        ppX, ppY = 0,0
        
        GameOver = font.render('GAME OVER', True, (255,255,255)) # loading game over
        screen.blit(GameOver, (100, 100))
        
        GameOver = font.render('You ended with a score of ' + str(score), True, (255,255,255)) # display score
        screen.blit(GameOver, (100, 140))
        playAgain = font.render('Press Enter to play again', True, (255,255,255))
        screen.blit(playAgain, (100, 200))
        if keys[pygame.K_RETURN]:   # reset variables to play again after enter is pressed
            lives = 3
            spookDirx = 2
            spookDiry = 2
            pwrUP = False
            ppX = random.randint(20, 550)
            ppY = random.randint(20, 550)
            score = 0



while play:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    draw_window(pacLOC)
    draw_spook(spookLOC)
    
# MOVEMENT
    keys = pygame.key.get_pressed() # check for key press
    if keys[pygame.K_LEFT]:
        if pacImg == pLO:
            pacImg = pLC
        else:
            pacImg = pLO
        if pacLOC.x <= 0 - 50: # moving to the other side of the screen
            pacLOC.x = brd_W
        pacLOC.x -= 5
    elif keys[pygame.K_RIGHT]:
        if pacImg == pRO:
            pacImg = pRC
        else:
            pacImg = pRO
        if pacLOC.x >= brd_W + 25:
            pacLOC.x = 0 - 49
        pacLOC.x += 5
    elif keys[pygame.K_UP]:
        if pacImg == pUO:
            pacImg = pUC
        else:
            pacImg = pUO
        if pacLOC.y <= 0 - 50:
            pacLOC.y = brd_H
        pacLOC.y -= 5
    elif keys[pygame.K_DOWN]:
        if pacImg == pDO:
            pacImg = pDC
        else:
            pacImg = pDO
        if pacLOC.y >= brd_H + 25:
            pacLOC.y = 0 - 49
        pacLOC.y += 5

    # moving cherry
    cherryY = cherryY + 1
    if cherryY >= 600:
        cherryY = 0
    screen.blit(cherry, (cherryX, cherryY)) 
    
    # lives system
    if lives <= 0: 
        gameOver()
    
    
    spookMove()
    colideCheck()
    powerPill()
    powerUP()
    gui()
    
    pygame.display.update()
pygame.quit()
