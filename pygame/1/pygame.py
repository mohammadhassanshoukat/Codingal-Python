#import necessary libraries
import pygame

#initialize required module
pygame.init()

#setup window geometry
screen = pygame.display.set_mode((400, 500))

#create  loop to run it until user exits
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    #make the changes visible
    pygame.display.flip()
