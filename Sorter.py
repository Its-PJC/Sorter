import random
import sys
import pygame
from pygame.locals import *


class SorterFeatures:
    def __init__(self, screen):
        self.screen = screen
        self.w_width = self.screen.get_width()
        self.w_height = self.screen.get_height()
        self.background = "Background.png"
        self.arr = [i for i in range(1, 301)]
        self.N = len(self.arr)
        self.inactBut_color = (92, 106, 189)
        self.actBut_color = (212, 140, 56)
        self.text_color = (255, 255, 255)
        self.text_font = 'Arial'
        self.line_width = 3

    def randomArr(self):
        shuffled = random.sample(self.arr, len(self.arr))
        return shuffled

    def buttonOnScreen(self, S,font_size):
        smallfont = pygame.font.SysFont(self.text_font, font_size)
        text = smallfont.render(S, True, self.text_color)
        return smallfont, text

    def activateButtonColor(self, smallfont, text, mouse, b_dim, S):
        if b_dim[0] <= mouse[0] <= b_dim[0] + b_dim[2] and b_dim[1] <= mouse[1] <= b_dim[1] + b_dim[3]:
            pygame.draw.rect(self.screen, self.actBut_color, b_dim)
        else:
            pygame.draw.rect(self.screen, self.inactBut_color, b_dim)

        self.screen.blit(text, (b_dim[0] + b_dim[2] // 2 - smallfont.size(S)[0] // 2,
                                b_dim[1] + b_dim[3] // 2 - smallfont.size(S)[1] // 2))

    def drawLines(self, shuffled):
        N = len(shuffled)
        for i in range(N):
            pygame.draw.line(self.screen, (255, 255, 255),
                             [self.w_width // 2 - N + i * 2, self.w_height - 100],
                             [self.w_width // 2 - N + i * 2, self.w_height - 100 - shuffled[i]],
                             self.line_width)
