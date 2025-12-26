import pygame

pygame.init()
#create  the display surface  object of specific dimension
window = pygame.display.set_mode((400,400))

#fill the screen with white colour 
window.fill((255,255,255))

#define colours
green = (0,255,0)

#draw solid circle
pygame.draw.circle(window,green,(300,300),50)

#draw outlined circle
pygame.draw.circle(window,green,(100,100),50,3)

#draw the surface object on the screen
pygame.display.flip()

#game loop
running = True
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Quit game
pygame.quit()