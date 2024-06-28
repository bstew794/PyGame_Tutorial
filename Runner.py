
# import necessary modules
import pygame
from sys import exit
from random import randint, choice


# This class derives from a PyGame Sprite to provide surfaces and rectangles for the player
class Play(pygame.sprite.Sprite):
    # Initializer function that inherits from the parent class
    def __init__(self):
        # Super initializer
        super().__init__()


        # Load player walking images into surfaces and save to list with index
        walk_1 = pygame.image.load('Graphics/Player/walk1.png').convert_alpha()
        walk_2 = pygame.image.load('Graphics/Player/walk2.png').convert_alpha()
        self.walk = [walk_1, walk_2]
        self.walk_indx = 0

        # Load player jumping image into a surface
        self.jump = pygame.image.load('Graphics/Player/jump.png').convert_alpha()

        # Set initial player image equal to idnex zero of the walking surface list
        self.image = self.walk[self.walk_indx]

        # Set initial player rectangle and gravity values
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.grav = 0

        # Load in Jump SFX as a class variable
        self.jump_sfx = pygame.mixer.Sound('Audio/jump.mp3')
        self.jump_sfx.set_volume(0.25)


    # This function checks for user input
    def play_inpt(self):
        # Get the keys pressed by teh user
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # Make the player object "jump" after pressing the spacebar or clicking on teh player
        if keys[pygame.K_SPACE] or (mouse_buttons and self.rect.collidepoint(mouse_pos)):
            # Only allow the player to jump if they are touching the ground
            if self.rect.bottom >= 300:
                    self.grav = -20
                    self.jump_sfx.play()
    
    # This function applies gravity to a player object
    def aply_grav(self):
        # Increment gravity to simulate gravitaional acceleration
        self.grav += 1
        self.rect.bottom += self.grav

        # Provide simulated collision with the ground to prevent infinite falling
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.grav = 0 # original tutorial did not reset the gravity when touching the ground
        
    # This function animates a player object
    def anm8(self):    
        # Display jumping animation if the player object is off the floor
        if self.rect.bottom < 300:
            self.image = self.jump
        # Display walking animation if the player object is on the floor
        else:
            self.walk_indx += 0.1

            if self.walk_indx >= len(self.walk):
                self.walk_indx = 0
            
            self.image = self.walk[int(self.walk_indx)]
    
    # This function updates a player object by calling class functions
    def update(self):
        self.play_inpt()
        self.aply_grav()
        self.anm8()

# This class derives from a PyGame Sprite to provide surfaces and rectangles for the player
class Obst(pygame.sprite.Sprite):
    # Initializer function that inherits from the parent class with new field that contains enemy type
    def __init__(self, type):
        # Super initializer
        super().__init__()

        # save type for later
        self.type = type


        # Load fly images into surfaces and save to frames list
        if self.type == 'fly':
            fly_1 = pygame.image.load('Graphics/Enemies/Fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('Graphics/Enemies/Fly/fly2.png').convert_alpha()
            self.frmes = [fly_1, fly_2]
            y_pos = 210
        # Load snail images into surfaces and save to frames list
        else:
            slid_1 = pygame.image.load('Graphics/Enemies/Snail/snail1.png').convert_alpha()
            slid_2 = pygame.image.load('Graphics/Enemies/Snail/snail2.png').convert_alpha()
            self.frmes = [slid_1, slid_2]
            y_pos = 300

        self.frme_index = 0

        # Set initial obstacle surface and rectangle
        self.image = self.frmes[self.frme_index]
        self.rect = self.image.get_rect(bottomleft = (randint(800, 1000), y_pos))


    # This function animates an obstacle object
    def anm8(self):
        # Set animation frequency dependent on enemy type
        if self.type == 'fly': 
            self.frme_index += 0.2
        else: 
            self.frme_index += 0.1
        
        # Display 1st or second enemy frame dependent on the index
        if self.frme_index >= len(self.frmes):
            self.frme_index = 0
        
        self.image = self.frmes[int(self.frme_index)]
    
    # This function removes obstacles that have moved offscreen from their parent sprite group
    def destroy(self):
        if self.rect.right < 0:
            self.kill()

    # This function updates an obstacle object by calling class fucntions
    def update(self):
        self.anm8()
        self.rect.left -= 6
        self.destroy()


# This function helps calculate the score of the player
def disp_scor():
    # calculate number of seconds spent alive
    curr_time = int((pygame.time.get_ticks() - star_time) / 1000)

    # display formatted score string on screen surface
    scor_surf = pixe_font.render(f'Score: {curr_time} s', False, (64, 64, 64))
    scor_rect = scor_surf.get_rect(center = (400, 50))
    screen.blit(scor_surf, scor_rect)

    return curr_time

# This function checks for collision between the player and obstacles but with refreshing SPRITE
def chec_for_coll_sprit():
    # Use built-in sprite collision detection function
    if pygame.sprite.spritecollide(play.sprite, obsts, False):
        # Delete all obstacles if player dies
        obsts.empty()

        return False
    return True


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
bg_music = pygame.mixer.Sound('Audio/music.wav')
bg_music.set_volume(0.0625)

# Define sprite group for player
play = pygame.sprite.GroupSingle()
play.add(Play())

# Define sprite group for enemies
obsts = pygame.sprite.Group()

# Define some surfaces including the environment, actors, and text
sky_surf = pygame.image.load('Graphics/Enviroment/sky.png').convert_alpha()
grnd_surf = pygame.image.load('Graphics/Enviroment/ground.png').convert_alpha()
play_stan = pygame.image.load('Graphics/Player/stand.png').convert_alpha()
play_stan = pygame.transform.rotozoom(play_stan, 0, 2)
game_name = pixe_font.render('Pixel Runner', False, (111, 196, 169))
game_mess = pixe_font.render('Press space to run', False, (111, 196, 169))

# Define a rectangle hitbox for the player, and menu items
stan_rect = play_stan.get_rect(center = (400, 200))
name_rect = game_name.get_rect(center = (400, 80))
mess_rect = game_mess.get_rect(center = (400, 330))

# Define timer variables
obst_tmer = pygame.USEREVENT + 1
pygame.time.set_timer(obst_tmer, 1400)

# Start playing background music
bg_music.play(loops = -1)

# Main game loop
while True:
    # Check for user input events
    for event in pygame.event.get():
        # Exit the game and close the window if the red x is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

        # Conditional statements while game state is active
        if game_actv:            
            # Obstacle addition timer logic
            if event.type == obst_tmer:
                # Conditionally add a new enemy to the obstacle list
                obsts.add(Obst(choice(['fly', 'snail', 'snail', 'snail'])))
                
        # Player input during an inactive game state
        else:
            # Reset the game state if the space key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_actv = True

                    play.sprite.rect.bottom = 300
                    play.sprite.grav = 0
                    play.sprite.walk_indx = 0

                    star_time = pygame.time.get_ticks()

    
    # The active game state logic
    if game_actv:
        # Display the skybox surface on the screen surface
        screen.blit(sky_surf, (0, 0))

        # Display the ground surface on the screen surface
        screen.blit(grnd_surf, (0, 300))

        # Display the score surface on the screen surface
        score = disp_scor()


        # Draw a sprite of the Player object
        play.draw(screen)

        # Update the Player sprite object
        play.update()

        
        # Draw the sprites from the enemy group
        obsts.draw(screen)

        # Update the enemy sprites
        obsts.update()


        # Manage player collision with obstacles
        game_actv = chec_for_coll_sprit()
    # The menu logic
    else:
        # Show player character standing on menu screen
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