import pygame
import random

#initialize pygame
pygame.init()

#custom event IDs
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

#define basic colors usingpygame.Color
#background Colors
BLUE = pygame.Color('blue')
Light_BLUE = pygame.Color('lightblue')
DarkBLUE = pygame.Color('darkblue')

#sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


#object class
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-1, 1), random.randint(-1, 1)]

def update (self):
    self.rect.move_ip(self.velocity)
    boundary_hit = False
    if self.rect.left <= 0 or self.rect.right >=500:
        self.velocity[0] = -self.velocity[0]
        boundary_hit = True
    if self.rect.top <= 0 or self.rect.bottom >=400:
        self.velocity[1] = -self.velocity[1]
        boundary_hit = True

    if boundary_hit:
        pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
        pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

def change_color(self):
    self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

def change_background_color(screen):
    global bg_color
    bg_color = random.choice([BLUE, Light_BLUE, DarkBLUE])



all_sprites = pygame.sprite.Group()
sp1 = Sprite(WHITE, 50, 50)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites.add(sp1)