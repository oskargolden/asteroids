import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menu import *
from score import *


def main():
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Initialize menu
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

    # Initialize score and lives before creating the asteroid
    
    lives_display = Lives(3)  # Starting with 3 lives

    score_display = Score(0)  # Initialize score_display first
    asteroid_field = AsteroidField(score_display)  # Pass score_display to AsteroidField

    asteroid = Asteroid(100, 100, ASTEROID_MAX_RADIUS, score_display)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    # MENU SELECTING FLAGS
    in_menu = True
    in_settings = False
    in_difficulty = False
    in_leader = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not in_menu:
                        in_menu = True
                        menu.get_subsurface()

            if in_menu:
                if in_settings:
                    selected_option = menu_settings.handle_event(event)
                    if selected_option == "Difficulty":
                        in_difficulty = True
                        in_settings = False
                    elif selected_option == "Back":
                        in_settings = False
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
                        in_menu = False
                    elif selected_option == "Settings":
                        in_settings = True
                    elif selected_option == "Leader Board":
                        in_leader = True
                    elif selected_option == "Quit":
                        pygame.quit()
                        sys.exit()

        screen.fill("black")

        # Information Display
        lives_display.draw(20, 20)  # Top-left corner
        score_display.draw(20, 60)  # Below the lives display

        if in_menu:
            if in_settings:
                menu_settings.draw()
            elif in_difficulty:
                menu_difficulty.draw()
            elif in_leader:
                menu_leader.draw()
            else:
                menu.draw()
        else:
            # Update and draw game objects
            for obj in updatable:
                obj.update(dt)

            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    lives_display.lives -= 1  # Deduct a life
                    if lives_display.lives <= 0:
                        print("Collision Life Lost")
                        

            for shot in shots:
                for asteroid in asteroids:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()

            for obj in drawable:
                obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()