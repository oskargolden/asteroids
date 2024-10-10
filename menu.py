import pygame 
import sys
pygame.font.init()
pygame.init()

# Define colours
TEXT_COL = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.SysFont("arialblack", 40)





class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options  # List of menu options (text)
        self.selected = 0  # Index of the currently selected option

    def draw(self):
        # Fill the screen with black to clear previous drawings
        self.screen.fill(BLACK)

        # Create a semi-transparent grey overlay
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)  # Create a surface with an alpha channel
        overlay.fill((128, 128, 128, 128))  # Fill with grey and 50% opacity (RGBA)
        self.screen.blit(overlay, (0, 0))  # Blit the overlay on top of the screen

        for i, option in enumerate(self.options):
            color = TEXT_COL if i == self.selected else WHITE
            img = font.render(option, True, color)
            # Center the text horizontally and adjust vertically
            self.screen.blit(img, (self.screen.get_width() // 2 - img.get_width() // 2, 
                                self.screen.get_height() // 2 - len(self.options) * 20 + i * 40))

    def move_selection(self, direction):
        self.selected += direction
        if self.selected < 0:
            self.selected = len(self.options) - 1  # Wrap to the bottom
        elif self.selected >= len(self.options):
            self.selected = 0  # Wrap to the top

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_selection(-1)  # Move up in the menu
            elif event.key == pygame.K_DOWN:
                self.move_selection(1)  # Move down in the menu
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]  # Return the selected option
        return None



#menu types# Create a menu with options
"""start_menu = ["Start Game", 
                  "Leader Board", 
                  "Options",
                  "Quit"]
menu = Menu(menu_options, font, screen)"""