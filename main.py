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

    
        
    start_menu = ["Start Game", "Leader Board", "Options", "Quit"]
    menu = Menu(screen, start_menu)

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
    in_menu = True  # Flag to track if we're in the menu

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    
                    in_menu = True

            # Handle menu events if in the menu
            if in_menu:
                selected_option = menu.handle_event(event)
                if selected_option == "Start Game":
                    print("Starting the game...")
                    in_menu = False  # Exit the menu
                elif selected_option == "Quit":
                    pygame.quit()
                    sys.exit()

        # Clear the screen at the start of each frame
        screen.fill("black")

        if in_menu:
            menu.draw()  # Draw the menu
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