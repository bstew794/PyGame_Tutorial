
# import necessary modules
import pygame
from sys import exit

# initialize the pygame system to allow me to run and display the game
pygame.init()

# define some variables that will be used in the rest of the code including the screen, clock, and fonts
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font('Font/PixelType.ttf', 50)

#define some surfaces including the environment, actors, and text
sky_surf = pygame.image.load('Graphics/Enviroment/Sky.png')
grnd_surf = pygame.image.load('Graphics/Enviroment/Ground.png')
test_surf = pygame.Surface((100, 200))
text_surf = test_font.render('My game', False, 'Black')

# display an opening screen and change the fill of the test surface to red
pygame.display.set_caption('Runner')
test_surf.fill('Red')

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

    # display the ground surface on the screen surface
    screen.blit(grnd_surf, (0, 300))

    # display the text surface on the screen surface
    screen.blit(text_surf, (300, 50))

    # display the test surface on the screen surface
    screen.blit(test_surf, (200, 100))

    # update the visual aspects of the game for each loop
    pygame.display.update()

    # limit the game to run at a maximum of roughly 60 frames a second
    clock.tick(60)