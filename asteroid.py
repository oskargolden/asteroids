import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, score_display):
        super().__init__(x, y, radius)
        self.score_display = score_display

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Increment the score by the asteroid's value
        self.score_display.score += ASTERIOD_VALUE  # Add 500 points to the score
        self.kill()

        # If the asteroid is at minimum size, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Randomize the angle of the split
        random_angle = random.uniform(20, 50)

        # Create two smaller asteroids
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create and add new smaller asteroids
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius, self.score_display)
        asteroid_a.velocity = a * 1.2
        asteroid_a.add(Asteroid.containers)  # Add to relevant sprite groups

        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius, self.score_display)
        asteroid_b.velocity = b * 1.2
        asteroid_b.add(Asteroid.containers)  # Add to relevant sprite groups
