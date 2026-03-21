from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt) 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_vector = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        new_size = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position, self.position, new_size)
        new_asteroid2 = Asteroid(self.position, self.position, new_size)
        new_asteroid.velocity = new_vector * 1.2
        new_asteroid2.velocity = new_vector2 * 1.2




        
