import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # draw circle
    def draw(self, screen):
        # must override
        pass

    # update circle position
    def update(self, dt):
        # must override
        pass
    
    # check for collision between two circles
    def collides_with(self, other):
        return pygame.math.Vector2.distance_to(self.position, other.position) <= (self.radius + other.radius)