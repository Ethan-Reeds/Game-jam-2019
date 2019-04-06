import pygame
from config import *
from bullet import *

class Player:
    def __init__(self,screen_dems, img = None):

        # screen dimensions
        self.screenwidth = screen_dems[0]
        self.screenheight = screen_dems[1]

        # player stuff
        self.pos = [self.screenwidth//2,500]
        self.speed = 150
        self.player_hitbox = ship_directions["framewidth"]//2
        self.bullets = []   # bullet class objects
        self.frame_row = 6
        self.frame_column = 0

        # stuff for the image
        self.img = img
        self.img_w = ship_directions["frameheight"]
        self.img_h = ship_directions["frameheight"]

    def update(self, dt):
        self.dt = dt

        # keep on screen code
        if self.pos[0] < 0 + self.player_hitbox:
            self.pos[0] = 0 + self.player_hitbox
        if self.pos[0] > self.screenwidth - self.player_hitbox:
            self.pos[0] = self.screenwidth - self.player_hitbox
        if self.pos[1] < 0 + (self.player_hitbox * 2):
            self.pos[1] = 0 + (self.player_hitbox * 2)
        if self.pos[1] > self.screenheight - (self.player_hitbox *  2):
            self.pos[1] = self.screenheight - (self.player_hitbox * 2)

    def input(self, evt, keys):
        # Moving player_ship
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed * self.dt
            self.frame_row = 4
            self.frame_column = 1

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed * self.dt
            self.frame_row = 6
            self.frame_column = 1
        else:
            self.frame_row = 6
            self.frame_column = 0

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.pos[1] -= self.speed * self.dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.pos[1] += self.speed * self.dt
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_SPACE:
                self.bullet_list.append(Bullet(self.Player.pos, 1))
                self.bullet_list.append(Bullet(self.Player.pos, 2))
                self.bullet_list.append(Bullet(self.Player.pos, 3))

    def draw(self,surf):
        # temorary player
        pygame.draw.circle(surf, (0,255,0), (int(self.pos[0]), int(self.pos[1])), self.player_hitbox, 1)

        rect = (self.img_w * self.frame_column, self.img_h * self.frame_row,
        self.img_w, self.img_h)

        surf.blit(self.img, (int(self.pos[0] - (self.img_w/2 + 15)),int(self.pos[1] - (self.img_h/2 + 15))), rect)

        for i in self.bullet_list:
            i.draw(win)
