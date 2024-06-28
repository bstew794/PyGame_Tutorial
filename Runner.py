
# import necessary modules
import pygame
from sys import exit
from random import randint, choice


# This class derives from a PyGame Sprite to provide surfaces and rectangles for the player
class Player(pygame.sprite.Sprite):
    # Initializer function that inherits from the parent class
    def __init__(self):
        # Super initializer
        super().__init__()


        # Load player walking images into surfaces and save to list with index
        walk = pygame.image.load('Graphics/Player/walk.png').convert_alpha()
        walk1 = pygame.image.load('Graphics/Player/walk1.png').convert_alpha()
        self.frames = [walk, walk1]
        self.framesIndex = 0

        # Load player jumping image into a surface
        self.jump = pygame.image.load('Graphics/Player/jump.png').convert_alpha()

        # Set initial player image equal to idnex zero of the walking surface list
        self.image = self.frames[self.framesIndex]

        # Set initial player rectangle and gravity values
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        # Load in Jump SFX as a class variable and set the volume to 1/4 its original value
        self.jumpSound = pygame.mixer.Sound('Audio/jump.mp3')
        self.jumpSound.set_volume(0.25)


    # This function checks for user input
    def player_input(self):
        # Get the keys pressed by the user
        keys = pygame.key.get_pressed()
        mouseButtons = pygame.mouse.get_pressed()
        mousePosition = pygame.mouse.get_pos()

        # Make the player object "jump" after pressing the spacebar or clicking on the player
        if keys[pygame.K_SPACE] or (mouseButtons[0] and self.rect.collidepoint(mousePosition)):
            # Only allow the player to jump if they are touching the ground
            if self.rect.bottom >= 300:
                    self.gravity = -20
                    self.jumpSound.play()
    
    # This function applies gravity to a player object
    def apply_gravity(self):
        # Increment gravity to simulate gravitaional acceleration
        self.gravity += 1
        self.rect.bottom += self.gravity

        # Provide simulated collision with the ground to prevent infinite falling
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0 # original tutorial did not reset the gravity when touching the ground
        
    # This function animates a player object
    def animate(self):    
        # Display jumping animation if the player object is off the floor
        if self.rect.bottom < 300:
            self.image = self.jump
        # Display walking animation if the player object is on the floor
        else:
            # Iterate through the walking frames at a consistent pace

            self.framesIndex += 0.1

            if self.framesIndex >= len(self.frames):
                self.framesIndex = 0
            
            self.image = self.frames[int(self.framesIndex)]
    
    # This function updates a player object by calling class functions
    # Most things that happen during one frame of the game to a player object occurs here
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate()

# This class derives from a PyGame Sprite to provide surfaces and rectangles for the player
class Obstacle(pygame.sprite.Sprite):
    # Initializer function that inherits from the parent class with new field that contains enemy type
    def __init__(self, type):
        # Super initializer
        super().__init__()

        # save type for later
        self.type = type


        # Load fly images into surfaces and save to frames list
        if self.type == 'fly':
            fly = pygame.image.load('Graphics/Obstacles/Fly/fly.png').convert_alpha()
            fly1 = pygame.image.load('Graphics/Obstacles/Fly/fly1.png').convert_alpha()
            self.frames = [fly, fly1]
            yPosition = 210
        # Load snail images into surfaces and save to frames list
        else:
            slide = pygame.image.load('Graphics/Obstacles/Snail/slide.png').convert_alpha()
            slide1 = pygame.image.load('Graphics/Obstacles/Snail/slide1.png').convert_alpha()
            self.frames = [slide, slide1]
            yPosition = 300

        self.framesIndex = 0

        # Set initial obstacle surface and rectangle
        self.image = self.frames[self.framesIndex]
        self.rect = self.image.get_rect(bottomleft = (randint(800, 1000), yPosition))


    # This function animates an obstacle object
    def animate(self):
        # Set animation frequency dependent on enemy type
        if self.type == 'fly': 
            self.framesIndex += 0.2 # faster iteration for flies
        else: 
            self.framesIndex += 0.1
        
        # Display 1st or second enemy frame dependent on the index
        if self.framesIndex >= len(self.frames):
            self.framesIndex = 0
        
        self.image = self.frames[int(self.framesIndex)]
    
    # This function removes obstacles that have moved offscreen from their parent sprite group
    def destroy(self):
        if self.rect.right < 0:
            self.kill()

    # This function updates an obstacle object by calling class functions and moving it to the right
    def update(self):
        self.animate()
        self.rect.left -= 6
        self.destroy()


# This function helps calculate the score of the player
def display_score():
    # calculate number of seconds spent alive
    currentTime = int((pygame.time.get_ticks() - startTime) / 1000)

    # display formatted score string on screen surface
    scoreSurface = pixelFont.render(f'Score: {currentTime} s', False, (64, 64, 64))
    scoreRectangle = scoreSurface.get_rect(center = (400, 50))
    screen.blit(scoreSurface, scoreRectangle)

    return currentTime

# This function checks for collision between the player and obstacles but with refreshing SPRITE
def sprite_collision_check():
    # Use built-in sprite collision detection function
    if pygame.sprite.spritecollide(player.sprite, obstacles, False):
        # Delete all obstacles if player dies
        obstacles.empty()

        return False
    return True


# Initialize the pygame system to allow me to run and display the game
pygame.init()

# Set the name of the window
pygame.display.set_caption('Runner')


# Define some variables that will be used in the rest of the code including the screen, clock, and fonts
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pixelFont = pygame.font.Font('Font/PixelType.ttf', 50)
gameActive = False
startTime = 0
score = 0
backgroundMusic = pygame.mixer.Sound('Audio/music.wav')
backgroundMusic.set_volume(0.0625)

# Define sprite group for player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Define sprite group for enemies
obstacles = pygame.sprite.Group()

# Define some surfaces including the environment, actors, and text
skySurface = pygame.image.load('Graphics/Enviroment/sky.png').convert_alpha()
groundSurface = pygame.image.load('Graphics/Enviroment/ground.png').convert_alpha()
# Is this a JoJo reference?
playerStand = pygame.image.load('Graphics/Player/stand.png').convert_alpha()
playerStand = pygame.transform.rotozoom(playerStand, 0, 2)
gameName = pixelFont.render('Pixel Runner', False, (111, 196, 169))
gameMessage = pixelFont.render('Press space to run', False, (111, 196, 169))

# Define a rectangle for the player, and menu items
standRectangle = playerStand.get_rect(center = (400, 200))
nameRectangle = gameName.get_rect(center = (400, 80))
messRectangle = gameMessage.get_rect(center = (400, 330))

# Define timer variables
obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer, 1400)

# Start playing background music
backgroundMusic.play(loops = -1)

# Main game loop
while True:
    # Check for user input events
    for event in pygame.event.get():
        # Exit the game and close the window if the red x is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

        # Conditional statements while game state is active
        if gameActive:           
            # Obstacle addition timer logic
            if event.type == obstacleTimer:
                # Conditionally add a new enemy to the obstacle list
                obstacles.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                
        # Player input during an inactive game state
        else:
            # Reset the game state if the space key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameActive = True

                    player.sprite.rect.bottom = 300
                    player.sprite.gravity = 0
                    player.sprite.framesIndex = 0

                    startTime = pygame.time.get_ticks()

    
    # The active game state logic
    if gameActive:
        # Display the skybox surface on the screen surface
        screen.blit(skySurface, (0, 0))

        # Display the ground surface on the screen surface
        screen.blit(groundSurface, (0, 300))

        # Display the score surface on the screen surface
        score = display_score()


        # Draw a sprite of the Player object
        player.draw(screen)

        # Update the Player sprite object
        player.update()

        
        # Draw the sprites from the enemy group
        obstacles.draw(screen)

        # Update the enemy sprites
        obstacles.update()


        # Manage player collision with obstacles
        gameActive = sprite_collision_check()
    # The menu logic
    else:
        # Show player character standing on menu screen
        screen.fill((94, 129, 162))
        screen.blit(playerStand, standRectangle)


        # Define score message surface and rectangle
        scoreMessage = pixelFont.render(f'Your score: {score} s', False, (111, 196, 169))
        scoreRectangle = scoreMessage.get_rect(center = (400, 330))

        # Show game name
        screen.blit(gameName, nameRectangle)

        # Conditionally show the game or score message
        if score == 0:
            screen.blit(gameMessage, messRectangle)
        else:
            screen.blit(scoreMessage, scoreRectangle)

    
    # Update the visual aspects of the game for each loop
    pygame.display.update()

    # Limit the game to run at a maximum of roughly 60 frames a second
    clock.tick(60)