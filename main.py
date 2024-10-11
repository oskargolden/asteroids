import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menu import *


def main():
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    
        
    
    menu = Menu(screen, start_menu)
    menu_settings = Menu(screen, settings_menu)
    menu_difficulty = Menu(screen, difficulty_settings) 
    menu_leader = Menu(screen, leader_board_menu)

    # Game initialization
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    # MENU SELECTING FLAGS
    in_menu = True  # Flag to track if we're in the main menu
    in_settings = False  # Flag for settings menu
    in_difficulty = False  # Flag for difficulty settings
    in_leader = False  # Flag for leaderboard

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not in_menu:
                        in_menu = True  # Go back to the main menu
                        menu.get_subsurface()  # Capture game state when entering menu

            # Handle menu events if in the menu
            if in_menu:
                if in_settings:
                    selected_option = menu_settings.handle_event(event)
                    if selected_option == "Difficulty":
                        in_difficulty = True
                        in_settings = False
                    elif selected_option == "Back":
                        in_settings = False
                    # Add more options handling here as needed
                elif in_difficulty:
                    selected_option = menu_difficulty.handle_event(event)
                    if selected_option == "Back":
                        in_difficulty = False
                        in_settings = True
                elif in_leader:
                    selected_option = menu_leader.handle_event(event)
                    if selected_option == "Back":
                        in_leader = False
                else:
                    selected_option = menu.handle_event(event)
                    if selected_option == "Start Game":
                        in_menu = False  # Exit the menu to start the game
                    elif selected_option == "Settings":
                        in_settings = True
                    elif selected_option == "Leader Board":
                        in_leader = True
                    elif selected_option == "Quit":
                        pygame.quit()
                        sys.exit()

        # Clear the screen at the start of each frame
        screen.fill("black")

        if in_menu:
            if in_settings:
                menu_settings.draw()  # Draw settings menu
            elif in_difficulty:
                menu_difficulty.draw()  # Draw difficulty menu
            elif in_leader:
                menu_leader.draw()  # Draw leaderboard
            else:
                menu.draw()  # Draw main menu
        else:
            # Update and draw game objects
            for obj in updatable:
                obj.update(dt)

            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    print("Game over!")
                    pygame.quit()
                    sys.exit()

            for shot in shots:
                for asteroid in asteroids:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()

            # Draw all drawable objects
            for obj in drawable:
                obj.draw(screen)

        # Update the display once after drawing everything
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()