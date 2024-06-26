
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
game_actv = True

# define some surfaces including the environment, actors, and score
sky_surf = pygame.image.load('Graphics/Enviroment/sky.png').convert_alpha()
grnd_surf = pygame.image.load('Graphics/Enviroment/ground.png').convert_alpha()
scor_surf = test_font.render('My game', False, (64, 64, 64))
snal_surf = pygame.image.load('Graphics/Enemies/Snail/snail1.png').convert_alpha()
play_surf = pygame.image.load('Graphics/Player/walk1.png').convert_alpha()

# define a rectangle hitbox for the player, enemies, and menu items
play_rect = play_surf.get_rect(midbottom = (80, 300))
snal_rect = snal_surf.get_rect(bottomleft = (800, 300))
scor_rect = scor_surf.get_rect(center = (400, 50))

# define player attributes
play_grav = 0

# main game loop
while True:
    # check for user input events
    for event in pygame.event.get():
        # exit the game and close the window if the red x is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

        # Check for play input during an active game state
        if game_actv:
            # jump if the player is clicked on
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    if play_rect.bottom >= 300:
                        play_grav = -20

            # jump if space key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if play_rect.bottom >= 300:
                            play_grav = -20
        # player input during an inactive game state
        else:
            # jump if any keyboard key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_actv = True
                    snal_rect.left = 800

    
    # The actual Game Logic
    if game_actv:
        # move the snail to the left by a predetermined amount
        snal_rect.left -= 4   

        # loops snail back to the right
        if snal_rect.right <= 0:
            snal_rect.left = 800


        # display the skybox surface on the screen surface
        screen.blit(sky_surf, (0, 0))

        # display the ground surface on the screen surface
        screen.blit(grnd_surf, (0, 300))


        # manage player gravity
        play_grav += 1
        play_rect.bottom += play_grav

        # add ground collision
        if play_rect.bottom >= 300:
            play_rect.bottom = 300
            play_grav = 0 # original tutorial did not reset the gravity

        # display the player on the screen surface
        screen.blit(play_surf, play_rect)


        # display the snail on the screen surface
        screen.blit(snal_surf, snal_rect)

        # add a background to the score
        pygame.draw.rect(screen, '#c0e8ec', scor_rect)
        pygame.draw.rect(screen, '#c0e8ec', scor_rect, 10)

        # display the score surface on the screen surface
        screen.blit(scor_surf, scor_rect)


        # Manage player collision with snails
        if play_rect.colliderect(snal_rect):
            game_actv = False
    # The menu logic
    else:
        screen.fill('Yellow')

    
    # update the visual aspects of the game for each loop
    pygame.display.update()

    # limit the game to run at a maximum of roughly 60 frames a second
    clock.tick(60)