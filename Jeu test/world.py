

import pygame
from cube import Cube


class World:

    def __init__(self):
        self.map = []
        with open('data/maps/map1.txt', 'r') as f:
            data = f.read()
        data = data.split('\n')
        for row in data:
            self.map.append(list(row))
        self.size = 25
        self.all_cubes = pygame.sprite.Group()

    def generation(self):
        print(self.map)
        y = 0
        for i in self.map:
            x = 0
            for j in i:
                if j == '1':
                    self.all_cubes.add(Cube(self, x*self.size, y*self.size))
                x += 1
            y += 1

    def update(self, screen):
        self.all_cubes.draw(screen)
