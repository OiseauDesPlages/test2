import pygame


class Cube(pygame.sprite.Sprite):

    def __init__(self, world, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/cube.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draws(self, screen):
        screen.blit(self.image, self.rect)
