import pygame


class Bullet:
    def __init__(self, position, dir=1):
        self.pos = position.copy()
        self.dir = dir
        self.speed = 300
        self.rad = 3

    def update(self, dt):
        if self.dir == 2:
            self.pos[1] -= self.speed * dt
        elif self.dir == 1:
            self.pos[0] += -self.speed * dt
            self.pos[1] -= self.speed * dt
        elif self.dir == 3:
            self.pos[0] += self.speed * dt
            self.pos[1] -= self.speed * dt
        elif self.dir == -2:
            self.pos[1] += self.speed * dt
        elif self.dir == -1:
            self.pos[0] -= -self.speed * dt
            self.pos[1] += self.speed * dt
        elif self.dir == -3:
            self.pos[0] -= self.speed * dt
            self.pos[1] += self.speed * dt

    def draw(self, win):
        pygame.draw.circle(win, (0, 255, 0), (int(self.pos[0]), int(self.pos[1])), self.rad)
