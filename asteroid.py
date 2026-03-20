import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, dt):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            deflection_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_1.velocity = pygame.math.Vector2.rotate(self.velocity, deflection_angle) * 1.2
            new_asteroid_2.velocity = pygame.math.Vector2.rotate(self.velocity, -deflection_angle) * 1.2
            
            self.kill()
            log_event("asteroid_split")