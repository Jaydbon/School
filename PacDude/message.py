
# Ryan Zhao
# 5/2/2022
# pacguy.py
# this program works with pygame

import pygame                # tell it to use the pygame library of code
import random               

pygame.init()                       # activate it

# ******************* VARIABLES ***************************
win_W,win_H = 800,600
brd_W,brd_H = 800,600
play = True
ghstDX=2
ghstDY=2
cherryDX=1
cherryDY=1
intScore = 0
intLives = 3
pwrUP = False
pwrPillOn = True
pwrPillTime = 0 
ppX = brd_W/2
ppY = brd_H/2






#*******SETUP WINDOW********
screen = pygame.display.set_mode((win_W,win_H))
pygame.display.set_caption("PacGuy")
screen.fill((0,0,255))
board = pygame.Surface((brd_W,brd_H))
pygame.display.update()



font = pygame.font.Font("freesansbold.ttf",32)      #sets the font

#Load the images into objects
#look in the images folder for images
pRO=pygame.image.load('Images/PMRO.png')
pRC=pygame.image.load('Images/PMRC.png')
pLO=pygame.image.load('Images/PMLO.png')
pLC=pygame.image.load('Images/PMLC.png')
pUO=pygame.image.load('Images/PMUO.png')
pUC=pygame.image.load('Images/PMUC.png')
pDO=pygame.image.load('Images/PMDO.png')
pDC=pygame.image.load('Images/PMDC.png')
pHA=pygame.image.load('Images/PMHA.png')
pHD=pygame.image.load('Images/PMHD.png')
gRIP1=pygame.image.load('Images/GRIP1.png')
gRIP2=pygame.image.load('Images/GRIP2.png')
gPR=pygame.image.load('Images/GPR.png')
gPL=pygame.image.load('Images/GPL.png')
pwrPillImg=pygame.image.load('Images/p_pill.png')
cherryImg=pygame.image.load('Images/cherry.png')


pwrPill = pwrPillImg

pacImg = pHA
ghstImg = gPR



gRIP1=pygame.image.load('Images/GRIP1.png')
gRIP2=pygame.image.load('Images/GRIP2.png')


pacLOC = pygame.Rect(0,0,50,50)                 #x,y,width,height
ghstLOC = pygame.Rect(300,300,50,50)
pwrPillLOC = pygame.Rect(380,290,50,50)
cherryLOC = pygame.Rect(400,400,50,50)


def draw_window(pacInfo):
    blueBG=(0,0,0)    #red,gree,blue tuple
    screen.fill(blueBG)
    screen.blit(pacImg,(pacLOC.x,pacLOC.y))#draw pacguy on screen
    screen.blit(ghstImg,(ghstLOC.x,ghstLOC.y))#draw ghost on screen
    #screen.blit(pwrPillImg,(pwrPillLOC.x,pwrPillLOC.y))#draw pill on screen
    screen.blit(cherryImg,(cherryLOC.x,cherryLOC.y))
    
        
    

    pygame.display.update()                 #update the display

    #if pwrPillOn == True:
        #board.blit(pwrPillImg,(ppX,ppY))
    #screen.blit(board,(0,0))
    #pygame.display.flip



def ghstMove():
    global ghstDX,  ghstDY    #global function

    #*****check for obstacles before moving****
    if (ghstLOC.y + ghstLOC.height + ghstDY >= 600 or ghstLOC.y + ghstDY <= 0):  #bottom of the ball at bottom of window
        ghstDY = ghstDY*-1
        #random direction change in other axis
        changeDir = random.randint(0,10)
        if changeDir >=8:
            ghstDX = ghstDX*-1
        
    if (ghstLOC.x + ghstLOC.width + ghstDX >= 800 or ghstLOC.x + ghstDX <= 0):  #bottom of the ball at bottom of window
        ghstDX = ghstDX*-1
        #random direction change in other axis
        changeDir = random.randint(0,10)
        if changeDir >=8:
            ghstDY = ghstDY*-1




    #random change anywhere
    #print(changeDir)
    changeDir = random.randint(0,500)
    if changeDir >=499:
        ghstDY = ghstDY*-1
        ghstDX = ghstDX*-1


    ghstLOC.x = ghstLOC.x + ghstDX  #sideways
    ghstLOC.y = ghstLOC.y + ghstDY  #up and down

    

       



def CheckColide():
    global ghstImg,pacImg,pwrUP, intScore, intLives,pwrPillTime
    
    pac_rect = pacImg.get_rect(topleft = (pacLOC.x, pacLOC.y)) #PacGuy hitbox
    ghst_rect = ghstImg.get_rect(topleft = (ghstLOC.x, ghstLOC.y)) #Ghost hitbox
    pwrPill_rect = pwrPillImg.get_rect(topleft = (pwrPillLOC.x, pwrPillLOC.y))#powerPill hitbox
    cherry_rect = cherryImg.get_rect(topleft = (cherryLOC.x, cherryLOC.y))#cherry hitbox
    if pac_rect.colliderect(pwrPill_rect):
        pwrUP = True
        pwrPillOn = False
        print('xxx')
        print(pwrUP)
        pwrPillTime=pygame.time.get_ticks()+7500
    if pac_rect.colliderect(ghst_rect):#check to see if hitboxes touch eachother
        
        if pwrUP == True:
            ghstImg = gRIP1 
        
        #*****flash between 2 different dead images
            for x in range(10):
                screen.blit(ghstImg, (ghstLOC.x, ghstLOC.y))   #draw ghost on screen
                pygame.display.update(ghstLOC.x, ghstLOC.y,50,50)#update where ghost is only
                pygame.time.delay(100)
                if ghstImg == gRIP1:
                    ghstImg = gRIP2
                else:
                    ghstImg = gRIP1

        if pwrUP == False:
            pacImg = pHD
            ghstImg = gPR
            screen.blit(pacImg, (pacLOC.x, pacLOC.y))
            pygame.display.update(pacLOC.x, pacLOC.y,50,50)
            pygame.time.delay(2000)

    
        
        #revive spook and put in different location
        ghstImg = gPR
        ghstLOC.x = random.randint(100,win_W-100)
        ghstLOC.y = random.randint(100,win_H-100)

        if pac_rect.colliderect(cherry_rect):#check to see if pacdude hitbox touches cherry
            intScore = intScore + 5

           



 
        
        




def powerUP():
    global pwrUP, pwrPillTime, brd_W, currTime, cntDOWN
    if pwrUP == True:
        currTime = pygame.time.get_ticks()
        timeLEFT = pwrPillTime - pygame.time.get_ticks()
        pygame.draw.rect(screen, (255,0,0), (brd_W/2-25, 625, 50, 150))
        textPOWER = font.render('POWER UP', True, (0,0,0))
        
        screen.blit(textPOWER, (320, 775))

        if  timeLEFT <= 0:
            pwrUP = False
        else:
            cntDOWN = (timeLEFT/7500)*150
            pygame.draw.rect(screen, (0,255,0), (brd_W/2-25, 625, 50, 150-cntDOWN))
    else:
        pygame.draw.rect(screen, (255,255,255), (brd_W/2-100, 625, 200, 200))

        
# Puts the power pill on the screen randomly

def PowerPill():
    global pwrPillTime, pwrPillOn, pwrPill,ppX,ppY,pwrPill,pacImg,currTime,pwrUP
    print(pwrUP)
    if pwrUP == True:
        return()

    pwrPill = random.randint(0,100)
    if pwrPill > 75:
        if pwrPillOn == False:
            pwrPillOn= True
            pwrPillTime = pygame.time.get_ticks()
            ppRand = random.randint(200,brd_W/2)
            if pacLOC.x >= brd_W/2:
                ppX = pacLOC.x - ppRand
            else:
                ppX = pacLOC.x + ppRand

            if pacLOC.y >= brd_H/2:
                ppY = pacLOC.y - ppRand
            else:
                ppY = pacLOC.y + ppRand
    
    if pwrPillOn == True:
        screen.blit(pwrPillImg,(ppX,ppY))
        currTime = pygame.time.get_ticks()
        pygame.display.update(ppX,ppY,50,50)
        board.blit(board, (0,  0))
   
        if currTime - pwrPillTime > 7500:
            pwrPillOn = False



def Score():            #gain score function
    global intScore
    text = font.render("SCORE:" + str(intScore),True,(255,255,255),(128,128,128))
    textRECT = text.get_rect()
    textRECT = (300,500)
    screen.blit(text,textRECT)

def Lives():            #lose lives function
    global intLives
    text = font.render("LIVES:" + str(intLives),True,(255,255,255),(128,128,128))
    textRECT = text.get_rect()
    textRECT = (200,400)
    screen.blit(text,textRECT)


            
    


    

    
    




                                               
while play:         #game play loop
    pygame.time.delay(10)               #need to smooth things out

    for event in pygame.event.get():    #get user input
        if event.type == pygame.QUIT:   #if it's the X button then quit
            play = False                #gets us out of the while loop

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:         #to go left
        if pacImg == pLO:
            pacImg = pLC
        else:
            pacImg = pLO

        if pacLOC.x <0:
            pacLOC.x=800

        pacLOC.x -=10
        

    elif keys_pressed[pygame.K_RIGHT]:      #to go right
        if pacImg == pRO:
            pacImg = pRC
        else:
            pacImg = pRO

        if pacLOC.x > 800:
            pacLOC.x=0

        pacLOC.x+=10                   #this is the actual move

    elif keys_pressed[pygame.K_UP]:
        if pacImg == pUO:
            pacImg = pUC
        else:
            pacImg = pUO

        if pacLOC.y <0:
            pacLOC.y=600

        pacLOC.y-=10

    elif keys_pressed[pygame.K_DOWN]:
        if pacImg == pDO:
            pacImg = pDC
        else:
            pacImg = pDO

        if pacLOC.y > 600:
            pacLOC.y=0

        pacLOC.y+=10
    else:
        pacImg = pHA


    if ghstDX >= 0:
        ghstImg = gPR
    if ghstDX <= 0:
        ghstImg = gPL

    Lives()
    Score()
    powerUP()
    PowerPill()
    CheckColide()
    ghstMove()
    draw_window(pacLOC)
    pygame.time.delay(5)
    
