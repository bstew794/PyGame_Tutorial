
# import necessary modules
import pygame
from sys import exit
from random import randint


# This function helps calculate the score of the player
def disp_scor():
    # calculate number of seconds spent alive
    curr_time = int((pygame.time.get_ticks() - star_time) / 1000)

    # display formatted score string on screen surface
    scor_surf = pixe_font.render(f'Score: {curr_time} s', False, (64, 64, 64))
    scor_rect = scor_surf.get_rect(center = (400, 50))
    screen.blit(scor_surf, scor_rect)

    return curr_time


# This function moves each obstacle in the provided list
def obst_move(obst_list):
    # Check if the obstacle lsit is empty
    if obst_list:
        # Iterate through the obstacle list
        for obst_rect in obst_list:
            # Move the obstacle by 5 pixels to the left
            obst_rect.left -= 5

            # Display a snail if the obastacle is touching the ground, and a fly otherwise
            if obst_rect.bottom == 300:
                screen.blit(snal_surf, obst_rect)
            else:
                screen.blit(fly_surf, obst_rect)


        # Remove obstacles that are now offscreen
        obst_list = [obst for obst in obst_list if obst.right >= 0]


        # Return the obstacle list for overwriting
        return obst_list
    # Logic required if an empty list is passed into the function
    else:
        return []


# This function checks for collision between the player and obstacles
def chec_for_coll(play, obst_list):
    # if the obstacle list is not empty then check if the player collided with any of them
    if obst_list:
        for obst_rect in obst_list:
            if play.colliderect(obst_rect):
                return False
    return True


# This function animates the player
def play_anim():
    global play_surf, play_walk_indx
    
    # Display jumping animation if player is off the floor
    if play_rect.bottom < 300:
        play_surf = play_jump
    # Display walking animation if player is on the floor
    else:
        play_walk_indx += 0.1

        if play_walk_indx >= len(play_walks):
            play_walk_indx = 0
        
        play_surf = play_walks[int(play_walk_indx)]


# Initialize the pygame system to allow me to run and display the game
pygame.init()

# Set the name of the window
pygame.display.set_caption('Runner')


# Define some variables that will be used in the rest of the code including the screen, clock, and fonts
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pixe_font = pygame.font.Font('Font/PixelType.ttf', 50)
game_actv = False
star_time = 0
score = 0

# Define some surfaces including the environment, actors, and text
sky_surf = pygame.image.load('Graphics/Enviroment/sky.png').convert_alpha()
grnd_surf = pygame.image.load('Graphics/Enviroment/ground.png').convert_alpha()
snal_surf = pygame.image.load('Graphics/Enemies/Snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('Graphics/Enemies/Fly/fly1.png').convert_alpha()
play_walk_1 = pygame.image.load('Graphics/Player/walk1.png').convert_alpha()
play_walk_2 = pygame.image.load('Graphics/Player/walk2.png').convert_alpha()
play_jump = pygame.image.load('Graphics/Player/jump.png').convert_alpha()
play_stan = pygame.image.load('Graphics/Player/stand.png').convert_alpha()
play_stan = pygame.transform.rotozoom(play_stan, 0, 2)
game_name = pixe_font.render('Pixel Runner', False, (111, 196, 169))
game_mess = pixe_font.render('Press space to run', False, (111, 196, 169))

# Define player attributes
play_grav = 0
play_walks = [play_walk_1, play_walk_2]
play_walk_indx = 0
play_surf = play_walks[play_walk_indx]

# Define a rectangle hitbox for the player, and menu items
play_rect = play_surf.get_rect(midbottom = (80, 300))
stan_rect = play_stan.get_rect(center = (400, 200))
name_rect = game_name.get_rect(center = (400, 80))
mess_rect = game_mess.get_rect(center = (400, 330))

# Define obstacles list
obst_rects = []

# Define timer variables
obst_tmer = pygame.USEREVENT + 1
pygame.time.set_timer(obst_tmer, 1400)


# Main game loop
while True:
    # Check for user input events
    for event in pygame.event.get():
        # Exit the game and close the window if the red x is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

        # Player input during an active game state
        if game_actv:
            # Jump if the player is clicked on
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    if play_rect.bottom >= 300:
                        play_grav = -20

            # Jump if space key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if play_rect.bottom >= 300:
                            play_grav = -20
            
            # Timer logic
            if event.type == obst_tmer:
                # Conditionally add a new enemy to the obstacle list
                if randint(0,2):
                    obst_rects.append(snal_surf.get_rect(bottomleft = (randint(800, 1000), 300)))
                else:
                    obst_rects.append(fly_surf.get_rect(bottomleft = (randint(800, 1000), 210)))
        # Player input during an inactive game state
        else:
            # Reset the game state if the space key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_actv = True
                    obst_rects = []
                    play_rect.bottom = 300
                    play_grav = 0
                    play_walk_indx = 0
                    star_time = pygame.time.get_ticks()

    
    # The actual Game Logic
    if game_actv:
        # Display the skybox surface on the screen surface
        screen.blit(sky_surf, (0, 0))

        # Display the ground surface on the screen surface
        screen.blit(grnd_surf, (0, 300))


        # Display the score surface on the screen surface
        score = disp_scor()


        # Manage player gravity
        play_grav += 1
        play_rect.bottom += play_grav

        # Add ground collision
        if play_rect.bottom >= 300:
            play_rect.bottom = 300
            play_grav = 0 # original tutorial did not reset the gravity when touching the ground

        # Determine player surface to use
        play_anim()

        # Display the player on the screen surface
        screen.blit(play_surf, play_rect)


        # Move the obstacles
        obst_rects = obst_move(obst_rects)


        # Manage player collision with obstacles
        game_actv = chec_for_coll(play_rect, obst_rects)
    # The menu logic
    else:
        # Show player character standing
        screen.fill((94, 129, 162))
        screen.blit(play_stan, stan_rect)


        # Define score message surface and rectangle
        scor_mess = pixe_font.render(f'Your score: {score} s', False, (111, 196, 169))
        scor_mess_rect = scor_mess.get_rect(center = (400, 330))


        # Show game name
        screen.blit(game_name, name_rect)

        # Conditionally show the game or score message
        if score == 0:
            screen.blit(game_mess, mess_rect)
        else:
            screen.blit(scor_mess, scor_mess_rect)

    
    # Update the visual aspects of the game for each loop
    pygame.display.update()

    # Limit the game to run at a maximum of roughly 60 frames a second
    clock.tick(60)