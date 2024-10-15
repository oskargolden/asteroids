import pygame
from constants import *


pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

score = 0

WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)


# Base class for information display
class Information_display:
    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, x, y, text, color=WHITE):
        img = self.font.render(text, True, color)
        screen.blit(img, (x, y))


# Lives class inheriting from Information_display
class Lives(Information_display):
    def __init__(self, lives=3) -> None:
        super().__init__()  # Proper call to the superclass constructor
        self.lives = lives

    def draw(self, x, y):
        super().draw(x, y, f"Lives: {self.lives}", RED)


# Score class inheriting from Information_display
class Score(Information_display):
    def __init__(self, score=0) -> None:
        super().__init__()
        self.score = score

    def draw(self, x, y):
        super().draw(x, y, f"Score: {self.score}", WHITE)




"""
color = TEXT_COL if i == self.selected else WHITE
            img = font.render(option, True, color)
            # Center the text horizontally and adjust vertically
            self.screen.blit(
                img,
                (self.screen.get_width() // 2 - img.get_width() // 2,
                 self.screen.get_height() // 2 - len(self.options) * 20 + i * 40)
            )
"""