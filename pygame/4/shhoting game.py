import math
import random
import pygame

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

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.jfif')
pygame.display.set_icon(icon)

player_image = pygame.image.load('player.png')
playerx = playerstartx
playery = playerstarty
playerx_change = 0

#enemy
enemy_image = []
enemyx = []
enemyy = []
enemyx_change = []
number_of_enemies = 6

for _i in range(number_of_enemies):
    enemy_image.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, width - 64))
    enemyy.append(random.randint(enmiestartymin, enmiestartymax))
    enemyx_change.append(enmiespeedx)
    enemyy_change.append(enemyspeedy)

#bullet
bulletIMG = pygame.image.load('bullet.png')
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
running = True
while running:
    screen.fill((0, 0, 0))  
    screen.blit(background, (0, 0))

