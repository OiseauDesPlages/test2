import pygame
from world import World


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load('assets/perso.png')

        self.rect = self.image.get_rect()
        self.puissance = 0.002
        self.pressed = {}
        self.rect.x = 0
        self.rect.y = 0
        self.rect_width = 10
        self.rect_height = 10
        self.vx = 1
        self.vy = 0
        self.ax = 0
        self.ay = 0.006
        self.y = 400
        self.x = 0
        self.crebond = 0.5
        self.frottement = 0.99

    def update(self, screen, width, height, world):
        # print(self.pressed)
        self.motion()
        if self.y <= 0:
            self.y = 0
            self.vy = -self.vy * self.crebond
            self.vx = self.vx * self.frottement

        if self.x <= 0:
            self.x = 0
            self.vx = -self.vx * self.crebond

        if self.x >= width - 10:
            self.x = width - 10
            self.vx = -self.vx * self.crebond

        # detection des collision x et y
        # avec le tableau map de la classe world

        y = 0
        for i in world.map:

            x = 0
            for j in i:

                if j == '1':
                    # if self.rect.x >= x * world.size - self.rect_width and self.rect.x <= (1 + x) * world.size + self.rect_width and self.rect.y >= y * world.size - self.rect_height and self.rect.y <= (1 + y) * world.size + self.rect_height:
                    if self.rect.x >= x * world.size - self.rect_width and self.rect.x <= (x+1) * world.size - self.rect_width and self.vx > 0 and self.rect.y >= y * world.size and self.rect.y <= (1 + y) * world.size-self.rect_height+1:
                        #print("collision par la gauche")
                        self.x = x*world.size-self.rect_width
                        self.vx = -self.vx * self.crebond
                        self.vy = self.vy * self.frottement
                    if self.rect.x >= x * world.size and self.rect.x <= (x+1) * world.size and self.vx < 0 and self.rect.y >= y * world.size and self.rect.y <= (1 + y) * world.size-self.rect_height+1:
                        #print("collision par la droite")
                        self.x = (x+1)*world.size
                        self.vx = -self.vx * self.crebond
                        self.vy = self.vy * self.frottement
                    if self.rect.y >= y * world.size - self.rect_height and self.rect.y <= (y+1) * world.size - self.rect_height and self.vy > 0 and self.rect.x >= x * world.size and self.rect.x <= (1 + x) * world.size-self.rect_width+1:
                        #print("collision par le haut")
                        self.y = y*world.size-self.rect_height
                        self.vy = -self.vy * self.crebond
                        self.vx = self.vx * self.frottement
                        if self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_SPACE):
                            self.vy -= self.puissance * 800
                    if self.rect.y >= y * world.size and self.rect.y <= (y+1) * world.size and self.vy < 0 and self.rect.x >= x * world.size and self.rect.x <= (1 + x) * world.size-self.rect_width+1:
                        #print("collision par le bas")
                        self.y = (y+1)*world.size
                        self.vy = -self.vy * self.crebond
                        self.vx = self.vx * self.frottement

                x += 1
            y += 1

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
        if self.pressed.get(pygame.K_1):
            self.ay = 0.006
            self.ax = 0
        if self.pressed.get(pygame.K_2):
            self.ay = -0.006
            self.ax = 0
        if self.pressed.get(pygame.K_3):
            self.ax = 0.006
            self.ay = 0
        if self.pressed.get(pygame.K_4):
            self.ax = -0.006
            self.ay = 0

        if self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d):
            self.vx += self.puissance * 2

        if self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q):
            self.vx -= self.puissance * 2

        if self.pressed.get(pygame.K_DOWN) or self.pressed.get(pygame.K_LSHIFT):
            self.vy += self.puissance * 2

        if self.pressed.get(pygame.K_LCTRL):
            self.crebond = 0
        else:
            self.crebond = self.crebond

        screen.blit(self.image, self.rect)

    def motion(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.rect.y = self.y
