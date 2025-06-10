import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, )
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # First asteroid
        velocity1 = self.velocity.rotate(random.uniform(20.0, 40.0))
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1 * 1.2

        # Second asteroid
        velocity2 = self.velocity.rotate(random.uniform(-40.0, -20.0))
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2 * 1.2



            


    def update(self, dt):
        self.position +=  self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius, 2)