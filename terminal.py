import pygame
from config import *


class Terminal:
    def __init__(self):
        self.image = TERM
        self.font = pygame.font.SysFont("Vixar ASCI", 48)
        self.term_string = "Code: "
        self.keys = Keys_info
        self.timer = 1
        self.x = 0
        self.not_available = False

    def update(self, dt):

        # self.x += dt
        if self.not_available:
            self.x += dt
            print(self.x)
            if self.x > self.timer:
                print("reset")
                self.x = 0
                self.term_string = "Code: "
                self.not_available = False

    def input(self, evt, keys):
        if evt.type == pygame.KEYDOWN:
            x = evt.key
            # print(x)
            if str(x) in self.keys:
                # self.term_string = "Code: "
                self.term_string += self.keys[str(x)]
            else:
                x = "Code: Not Available"
                self.term_string = x
                self.not_available = True
            # print(x)

    def draw(self, win):
        win.blit(self.image, (0, 0, win_width, win_height))
        win.blit(self.font.render(self.term_string, True, (255, 255, 255)), (245, 170))
