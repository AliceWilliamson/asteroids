import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0,0)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

