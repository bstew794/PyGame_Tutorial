
'''

'''

# import necessary modules
import pygame
from sys import exit


# initialize the pygame system to allow me to run and display the game
pygame.init()


# define some variables that will be used in the rest of the code including images, the clock, and surfaces
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
sky_surf = pygame.image.load('Graphics\Enviroment\Sky.png')

# display an opening screen
pygame.display.set_caption('Runner')

# main game loop
while True:
    # check for user input events
    for event in pygame.event.get():
        # exit the game and close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # display the skybox surface on the screen surface
    screen.blit(sky_surf, (0, 0))

    # update the visual aspects of the game for each loop
    pygame.display.update()

    # limit the game to run at a maximum of roughly 60 frames a second
    clock.tick(60)