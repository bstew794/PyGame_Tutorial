
# import necessary modules
import pygame
from sys import exit

# initialize the pygame system to allow me to run and display the game
pygame.init()

# Set the name of the window
pygame.display.set_caption('Runner')

# define some variables that will be used in the rest of the code including the screen, clock, and fonts
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font('Font/PixelType.ttf', 50)

# define some surfaces including the environment, actors, and text
sky_surf = pygame.image.load('Graphics/Enviroment/sky.png').convert_alpha()
grnd_surf = pygame.image.load('Graphics/Enviroment/ground.png').convert_alpha()
text_surf = test_font.render('My game', False, 'Black')
snal_surf = pygame.image.load('Graphics/Enemies/Snail/snail1.png').convert_alpha()
play_surf = pygame.image.load('Graphics/Player/walk1.png').convert_alpha()

# define a rectangle hitbox for the player, and enemies
play_rect = play_surf.get_rect(midbottom = (80, 300))
snal_rect = snal_surf.get_rect(bottomleft = (800, 300))

# main game loop
while True:
    # check for user input events
    for event in pygame.event.get():
        # exit the game and close the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    # move the snail by a predetermined amount
    snal_rect.left -= 4

    if snal_rect.right <= 0:
        snal_rect.left = 800

    # move the player by a predetermined amount
    play_rect.left += 1


    # display the skybox surface on the screen surface
    screen.blit(sky_surf, (0, 0))

    # display the ground surface on the screen surface
    screen.blit(grnd_surf, (0, 300))

    # display the player on the screen surface
    screen.blit(play_surf, play_rect)

    # display the snail on the screen surface
    screen.blit(snal_surf, snal_rect)

    # display the text surface on the screen surface
    screen.blit(text_surf, (300, 50))


    # update the visual aspects of the game for each loop
    pygame.display.update()

    # limit the game to run at a maximum of roughly 60 frames a second
    clock.tick(60)