import pygame
from sys import exit


pygame.init()


screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
sky_surf = pygame.image.load('Graphics\Enviroment\Sky.png')

pygame.display.set_caption('Runner')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)