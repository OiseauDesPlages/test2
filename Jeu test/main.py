import pygame
from player import Player
from world import World
pygame.init()
bg = pygame.image.load('assets/bg.jpg')

pygame.display.set_caption("le meilleur jeu")
width = 1080
height = 720
# Taille
screen = pygame.display.set_mode((width, height))

running = True
player = Player()
world = World()
world.generation()
while 1:

    screen.blit(bg, (0, 0))
    player.update(screen, width, height, world)
    for event in pygame.event.get():

        if event == pygame.QUIT:
            running = False
            pygame.quit()

    world.update(screen)

    pygame.display.flip()
