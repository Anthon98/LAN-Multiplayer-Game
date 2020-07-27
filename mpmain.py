import pygame
import time
import sys
from threading import Timer

pygame.init()
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Multiplayer Test")

#Player avatars.
playerImg = pygame.image.load('minitest.png')
playerImg2 = pygame.image.load('minitest2.png')

playerX = 370
playerY = 480

otherX = 1
otherY = 1

o_prevX = 1
o_prevY = 1

playerx_change = 0
playery_change = 0

#Shares local client position (LAN).
def update_local_client_pos():
    global playerX
    global playerY
    global otherX
    global otherY
    global o_prevX
    global o_prevY

    combdat = str(playerX)+";"+str(playerY)
    with open(r'C:\Users\User\Desktop\SharedTestiJuttu\Hei2.txt', "w") as loc_data2:
        loc_data2.write(combdat)

    with open(r'C:\Users\User\Desktop\SharedTestiJuttu\Hei.txt') as loc_data:
        data2 = loc_data.read()
        #Sometimes our data is empty due to being written to. Needs a future fix.
        try:
            p2 = data2.split(";")
            otherX = float(p2[0])
            otherY = float(p2[1])

            o_prevX = otherX
            o_prevY = otherY

        except:
            pass

    Timer(0.0001, update_local_client_pos).start()
    #Tick speed.

#Local player location on current client screen.
def player(x, y):

    global otherX
    global otherY
    '''
    global o_prevX
    global o_prevY

    #get the difference between updates
    
    difX = otherX
    difY = otherY

    if o_prevX != otherX:
        if o_prevX > otherX:
            difX = o_prevX - otherX
            otherX - difX
        else:
            difX = otherX - o_prevX
            otherX + difX

    if o_prevY != otherY:
        if o_prevY > otherY:
            difY = o_prevY - otherY
            otherY - difY
        else:
            difY = otherY - o_prevY
            otherY + difY

    '''
    #Client screen update handler.
    #screen.blit(playerImg2,(difX, difY))
    screen.blit(playerImg2,(otherX, otherY))
    screen.blit(playerImg,(x, y))

#Initialize update_local_client_pos Threading. Also gets our other player data.
update_local_client_pos()

running = True
while running:
    time.sleep(.01)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -3
            if event.key == pygame.K_RIGHT:
                playerx_change = 3
            if event.key == pygame.K_UP:
                playery_change = -3
            if event.key == pygame.K_DOWN:
                playery_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerx_change = 0
            if event.key == pygame.K_RIGHT:
                playerx_change = 0
            if event.key == pygame.K_UP:
                playery_change = 0
            if event.key == pygame.K_DOWN:
                playery_change = 0

    playerX+=playerx_change
    playerY+=playery_change

    player(playerX,playerY)

    pygame.display.update()