import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_asteroid_angle = random.uniform(20, 50)
            new_asteroid_vector1 = self.velocity.rotate(random_asteroid_angle)
            new_asteroid_vector2 = self.velocity.rotate(-random_asteroid_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            Asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            Asteroid1.velocity = new_asteroid_vector1 * 1.2
            Asteroid2.velocity = new_asteroid_vector2 * 1.2