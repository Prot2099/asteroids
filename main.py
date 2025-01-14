# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, drawable, updatable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        
        #player.update(dt)
        for obj in updatable:  
            obj.update(dt)

        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collision(player):
                print("Game Over")
                sys.exit()
            for shot in shots:
                if obj.collision(shot):
                    shot.kill()
                    obj.split()
                    
        
                
                

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()