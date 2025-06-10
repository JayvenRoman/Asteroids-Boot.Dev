import pygame
from constants import *
from circleshape import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        
        direction = pygame.Vector2(0, 1).rotate(rotation)
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.position +=  self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), self.position, self.radius, 2)