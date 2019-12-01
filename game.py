import pygame
import time

SPEED = 2
DEBUG_MODE = False

pygame.display.init()
screen = pygame.display.set_mode((640, 480))#, pygame.FULLSCREEN)
screen.fill((40,60,80))

lev = ['###########################',
       '#                         #',
       '#                 #       #',
       '###############   #       #',
       '#                 #   #####',
       '#                 #       #',
       '#     #############       #',
       '#         #               #',
       '#         #               #',
       '#  #      #               #',
       '#  #      #    ############',
       '#  #      #               #',
       '#  #      #               #',
       '#  #                      #',
       '#  #      ###########     #',
       '#  #      #               #',
       '#  ####   #               #',
       '#     #   #     #         #',
       '#     #         #         #',
       '###########################',
       ]
       
wall = pygame.image.load('gfx/wall.png')
grass = pygame.image.load('gfx/grass.png')
debug = pygame.image.load('gfx/debugtile.png')

tiles = {'#': wall,
         ' ': grass,
         }

left1 = pygame.image.load('gfx/player_left1.png')
left2 = pygame.image.load('gfx/player_left2.png')
right1 = pygame.image.load('gfx/player_right1.png')
right2 = pygame.image.load('gfx/player_right2.png')
up1 = pygame.image.load('gfx/player_up1.png')
up2 = pygame.image.load('gfx/player_up2.png')
down1 = pygame.image.load('gfx/player_down1.png')
down2 = pygame.image.load('gfx/player_down2.png')
idle = pygame.image.load('gfx/player_idle.png')

animation = [(left1, left2),
             (right1, right2),
             (up1, up2),
             (down1, down2),
             (idle, idle),
             ]

playerx = 48
playery = 240

xdir = 0
ydir = 0

clock = pygame.time.Clock()

running = True

while running:
    t = time.time()
    screen.fill((40,60,80))
    
    # level zeichnen
    
    for y in range(len(lev)):
        for x in range(len(lev[0])):
            tileno = lev[y][x]
            tile = tiles[tileno]
            screen.blit(tile, (x * 24, y * 24))
    
    # spieler zeichnen
    
    if xdir < 0:
        animdir = 0
    elif xdir > 0:
        animdir = 1
    elif ydir < 0:
        animdir = 2
    elif ydir > 0:
        animdir = 3
    else:
        animdir = 4
        
    animphase = 0 if int(t * 1000) % 400 > 200 else 1
    player_sprite = animation[animdir][animphase]

    screen.blit(player_sprite, (playerx, playery))
    
    # tastatur-events abfragen
    
    while True:
        e = pygame.event.poll()
        
        if not e:
            break

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                xdir = -SPEED
                ydir = 0
            elif e.key == pygame.K_RIGHT:
                xdir = SPEED
                ydir = 0
            if e.key == pygame.K_UP:
                ydir = -SPEED
                xdir = 0
            elif e.key == pygame.K_DOWN:
                ydir = SPEED
                xdir = 0
                
            elif e.key == pygame.K_ESCAPE:
                running = False
                
            elif e.key == pygame.K_F12:
                DEBUG_MODE = not DEBUG_MODE
                
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                if xdir < 0:
                    xdir = 0
            elif e.key == pygame.K_RIGHT:
                if xdir > 0:
                    xdir = 0
            if e.key == pygame.K_UP:
                if ydir < 0:
                    ydir = 0
            elif e.key == pygame.K_DOWN:
                if ydir > 0:
                    ydir = 0
    
    # richtungen und positionen erstmal sichern
    
    newxdir = xdir
    newydir = ydir
    
    newplayerx = playerx + newxdir
    newplayery = playery + newydir
    
    # kollisions-relevante tiles ermitteln (tilesize = 24x24)
    
    x1 = int(newplayerx / 24)
    x2 = int((newplayerx + 23) / 24)
    y1 = int(newplayery / 24)
    y2 = int((newplayery + 23) / 24)
    
    collisiontile1 = lev[y1][x1]
    collisiontile2 = lev[y1][x2]
    collisiontile3 = lev[y2][x1]
    collisiontile4 = lev[y2][x2]
    
    if DEBUG_MODE:
        screen.blit(debug, (x1 * 24, y1 * 24))
        screen.blit(debug, (x2 * 24, y1 * 24))
        screen.blit(debug, (x1 * 24, y2 * 24))
        screen.blit(debug, (x2 * 24, y2 * 24))
    
    # supergenialer smooth-um-die-ecken-lauf-algorithmus
    
    if xdir < 0:
        if collisiontile1 == '#' and collisiontile3 == '#':
            newxdir = 0
        elif collisiontile1 == '#' and collisiontile3 == ' ':
            newxdir = 0
            newydir = SPEED
        elif collisiontile1 == ' ' and collisiontile3 == '#':
            newxdir = 0
            newydir = -SPEED
    elif xdir > 0:
        if collisiontile2 == '#' and collisiontile4 == '#':
            newxdir = 0
        elif collisiontile2 == '#' and collisiontile4 == ' ':
            newxdir = 0
            newydir = SPEED
        elif collisiontile2 == ' ' and collisiontile4 == '#':
            newxdir = 0
            newydir = -SPEED
    elif ydir < 0:
        if collisiontile1 == '#' and collisiontile2 == '#':
            newydir = 0
        elif collisiontile1 == '#' and collisiontile2 == ' ':
            newydir = 0
            newxdir = SPEED
        elif collisiontile1 == ' ' and collisiontile2 == '#':
            newydir = 0
            newxdir = -SPEED
    elif ydir > 0:
        if collisiontile3 == '#' and collisiontile4 == '#':
            newydir = 0
        elif collisiontile3 == '#' and collisiontile4 == ' ':
            newydir = 0
            newxdir = SPEED
        elif collisiontile3 == ' ' and collisiontile4 == '#':
            newydir = 0
            newxdir = -SPEED
    
    # geaenderte position anwenden
    
    playerx += newxdir
    playery += newydir
    
    # buffer wechseln (gerendertes bild anzeigen) und auf 60 fps begrenzen
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
   
