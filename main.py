# this will allow us to use code from
# python's open-source pygame library
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    i = True
    color_black = (0,0,0)

    game_clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y, PLAYER_RADIUS)

    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #This is the basic infinite loop that allows Pygame's 'X' button to close the game  
    while i is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #this fills the screen with the specified color 
        screen.fill(color_black)
        #updates and draws the player's position
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()
                
            if player.collision_check(asteroid):
                print("Game over!")
                pygame.quit()
                return
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000





#This line ensures that main() is only called when run directly
if __name__ == "__main__":
    main()