import math
import random
import pygame

pygame.init()

#constant
width = 800
hieght = 500
playerstartx = 370
playerstarty = 380
enmiestartymin = 50
enmiestartymax = 150
enmiespeedx = 4
enemyspeedy = 40
bulletspeedy= 10
collsionsistance=27

#create the game screen
screen = pygame.display.set_mode((width, hieght))
background = pygame.Surface((width, hieght))
background.fill((0, 0, 0))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.jfif')
pygame.display.set_icon(icon)

player_image = pygame.image.load('icon.jfif')
playerx = playerstartx
playery = playerstarty
playerx_change = 0

#enemy
enemy_image = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
number_of_enemies = 6

for _i in range(number_of_enemies):
    enemy_image.append(pygame.image.load('icon.jfif'))
    enemyx.append(random.randint(0, width - 64))
    enemyy.append(random.randint(enmiestartymin, enmiestartymax))
    enemyx_change.append(enmiespeedx)
    enemyy_change.append(enemyspeedy)


#bullet
bulletIMG = pygame.Surface((10, 20))
bulletIMG.fill((255, 255, 255))
bulletx = 0
bullety = playerstarty
bulletx_change = 0
bullety_change = bulletspeedy
bullet_state = "ready"  

#score
scorevalue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    #display the cureent score on the screen
    score = font.render("Score : " + str(scorevalue), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    #display game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    #draw the player on the screen
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    #draw an enemy on the screen
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x, y):
    #fire the bullet from the player
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))

def iscollision(enemyx, enemyy, bulletx, bullety):
    #check if there is a collision between bullet and enemy
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety) ** 2)
    return distance < collsionsistance

#game loop
clock = pygame.time.Clock()
running = True
game_over = False

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))  
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                fire_bullet(bulletx, bullety)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    if not game_over:
        #player movement
        playerx += playerx_change
        playerx = max(0, min(playerx, width - 64))

        #enemy movement
        for i in range(number_of_enemies):
            if enemyy[i] > 440:
                for j in range(number_of_enemies):
                    enemyy[j] = 2000
                game_over = True
                break

            enemyx[i] += enemyx_change[i]
            if enemyx[i] <= 0:
                enemyx_change[i] = enmiespeedx
                enemyy[i] += enemyspeedy
            elif enemyx[i] >= width - 64:
                enemyx_change[i] = -enmiespeedx
                enemyy[i] += enemyspeedy

            #collision
            if iscollision(enemyx[i], enemyy[i], bulletx, bullety):
                bullety = playerstarty
                bullet_state = "ready"
                scorevalue += 1
                enemyx[i] = random.randint(0, width - 64)
                enemyy[i] = random.randint(enmiestartymin, enmiestartymax)

            enemy(enemyx[i], enemyy[i], i)

        #bullet movement
        if bullety <= 0:
            bullety = playerstarty
            bullet_state = "ready"
        elif bullet_state == "fire":
            fire_bullet(bulletx, bullety)
            bullety -= bullety_change

        player(playerx, playery)
        show_score(textX, textY)
    else:
        game_over_text()
    
    pygame.display.update()