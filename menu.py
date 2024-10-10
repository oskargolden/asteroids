from pygame import *

pygame.font.init()
pygame.init()

# Define colours
TEXT_COL = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.SysFont("arialblack", 40)


#menu types# Create a menu with options
start_menu = ["Start Game", 
                  "Leader Board", 
                  "Options",
                  "Quit"]
menu = Menu(menu_options, font, screen)

class Menu:
    def __init__(self, x, y, options):
        self.x = x
        self.y = y
        self.options = options  # List of menu options (text)
        self.selected = 0  # Index of the currently selected option

    def draw(self):
        self.screen.fill("grey")  # Clear the screen
        for i, option in enumerate(self.options):
            color = TEXT_COL if i == self.selected_option else WHITE
            img = self.font.render(option, True, color)
            # Center the text horizontally and adjust vertically
            self.screen.blit(img, (SCREEN_WIDTH // 2 - img.get_width() // 2, 
                                   SCREEN_HEIGHT // 2 - len(self.options) * 20 + i * 40))
        pygame.display.flip()  # Update the display

    def draw_menu(self, screen):
        # Loop through the menu options and display them
        for i, option in enumerate(self.options):
            if i == self.selected:
                # Highlight selected option
                self.draw_text(screen, option, font, WHITE, self.x, self.y + i * 60)
            else:
                self.draw_text(screen, option, font, TEXT_COL, self.x, self.y + i * 60)

    def move_selection(self, direction):
        # Move the selection up or down in the menu
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

    def make_menu(self):# Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            selected_option = self.handle_event()
            if selected_option == "Start Game":
                break  # Exit the menu loop to start the game
            elif selected_option == "Quit":
                pygame.quit()
                sys.exit()

            self.draw()  # Draw the menu

