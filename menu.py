import pygame


pygame.init()


#define  colours
TEXT_COL = (255, 255, 255)

BLACK = (0, 0, 0)  # Define the black color

#define font
font = pygame.font.SysFont("arialblack", 40)

def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x, y))


