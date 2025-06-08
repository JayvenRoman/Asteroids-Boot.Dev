# this will allow us to use code from
# python's open-source pygame library
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = True
    color_black = (0,0,0)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
        
    while x is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color_black)
        pygame.display.flip()



#This line ensures that main() is only called when run directly
if __name__ == "__main__":
    main()