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
