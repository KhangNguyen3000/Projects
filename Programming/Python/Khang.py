import pygame
import time
import random
import os

pygame.init()

clock = pygame.time.Clock()

bX = 10 #largeur du bloc
bY = 10 #longueur du bloc
bX2 = 20 #largeur du food
bY2 = 20 #longueur du food
bX3 = 10 #largeur du enemy
bY3 = 10 #longueur du enemy
pR = []#player rectangle


rR = 60 # refreshRate

dW = 1280 # longueur du fenetre
dH = 720 # largeur du fentre
x = dW/2
y = dH/2

m = 7 # vitesse du bloc
eS = 5 #enemy speed
spawner = 300 #milliseconf par enemy

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)


mFont = "verdana"#menu font
smallFont = pygame.font.SysFont(mFont, 15)
mediumFont = pygame.font.SysFont(mFont, 30)
largeFont = pygame.font.SysFont(mFont, 50)






fps = pygame.time.Clock()
display = pygame.display.set_mode((dW,dH))
pygame.display.set_caption("Khang")
pygame.display.update()
eSpawn = pygame.USEREVENT + 1

pygame.time.set_timer(eSpawn, spawner)




def Intro():
    
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    os._exit(1)
                if event.key == pygame.K_c:
                    intro = False
        
        display.fill(white)
        Msg("Welcome to Khang's Snake Game", green, yC = -100 , size = "large")
        Msg("Dodge the red boxes while eating the green food", black, yC = 0, size = "medium")
        Msg("Q to quit, C to start", black, yC = 50)
        pygame.display.update()
        clock.tick(10)


def Snake(sList, bX, bY):
    global pR
    pR = []
    for xY in sList:
        pR.append(display.fill(black, rect = (xY[0], xY[1], bX, bY)))





def TObj (text, color, size):
    if size == "small":
        tSurf = smallFont.render(text, True, color) #creer le msg
    if size == "medium":
        tSurf = mediumFont.render(text, True, color) #creer le msg
    if size == "large":
        tSurf = largeFont.render(text, True, color) #creer le msg
    return tSurf, tSurf.get_rect() # return le msg et le rectangle du msg (lespace pris)


def Msg(msg, color, yC, size = "small"):
    tSurf, tRect = TObj(msg, color, size)
    tRect.center = (dW/2), ((dH/2)+yC)
    display.blit(tSurf, tRect) # display l'image
    pygame.display.update()#update le display


def MsgS(msg, color = black, size = "small"):
    tSurf, tRect = TObj(msg, color, size)
    display.blit(tSurf, tRect) # display l'image
    pygame.display.update()#update le display



def Game ():
    ex = False
    gOver = False

    d = 0
    
    x = dW/2
    y = dH/2

    sList = []
    sL = 1

    eList = []
    eR = []

    score = 0
    
    cx = 0 #vitesse x commene
    cy = 0 # vitesse y commence

    rX = random.randrange(0,(dW-bX2))
    rY = random.randrange(0,(dH-bY2))

    p = display.fill(black, rect = (x, y, bX, bY)) # player

    while not ex:
        clock.tick(60)
        zz = 0
        yy = 0

        while gOver == True:
            clock.tick(5)
            display.fill(black)
            Msg("C to play again. Q to quit", white, yC = 50, size = "medium")
            MsgS("Score: "+str(score), white)
            Msg("Game Over", red, yC =  -50, size = "large")
            

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        ex = True
                        gOver = False

                    elif event.key == pygame.K_c:
                        Game()
            

        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(1)
            
            if event.type == eSpawn:
                eL = []
                eL.append(random.randrange(0, (dW-bX)))
                eL.append(0)
                eList.append(eL)
                eR.append(display.fill(red, rect = (eL[0], 0, bX3, bY3)))
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        cx = -m
                        cy = 0
                elif event.key == pygame.K_RIGHT:
                        cx = m
                        cy = 0
                elif event.key == pygame.K_DOWN:
                        cy = m
                        cx = 0
                elif event.key == pygame.K_UP:
                        cy = -m
                        cx = 0
                elif event.key == pygame.K_e:
                    gOver = True


        
        if x <= 0:
            cx = m
            cy = 0
        if y <= 0:
            cy = m
            cx = 0
        if x >= (dW-bX):
            cy = 0
            cx = -m
        if y >= (dH-bY):
            cy = -m
            cx = 0

            
        x += cx
        y += cy
        
        display.fill(white)
        
        f = display.fill(green, rect = (rX, rY, bX2, bY2))


        s = []
        s.append(x)
        s.append(y)
        sList.append(s)
        Snake(sList, bX, bY)

        iV = 0
        for i in eList:
            #print(i)
            eR.append(display.fill(red, rect = (i[0], i[1], bX3, bY3)))
            #print (str(i[1]))
            del eR[0]
            if i[1] > dH:
                del eR[-1]
                del eList[iV]
            i[1] += eS + d
            iV+=1
            

        if len(sList) > sL: # si il touche pas la nourriture
            del sList[0]
            

        while zz < len(pR): #check si il touche enemy
            #print("zz"+str(zz))
            #print(pR)
            while yy < len(eR):
                #print("yy"+str(yy))
               #print (eR[yy])
                if pR[zz].colliderect(eR[yy]) == True:
                    gOver = True
                yy += 1
            zz += 1
            yy =0;
        


        if pR[-1].colliderect(f) == True:# si il touche la nourriture
            sL +=1
            rX = random.randrange(0,(dW-bX2))
            rY = random.randrange(0,(dH-bY2))
            score+=1
            d += 1

        MsgS("Score: "+str(score))
            
        pygame.display.update()
        fps.tick(rR)

    pygame.quit()
    os._exit(1)
    
Intro()
Game()
