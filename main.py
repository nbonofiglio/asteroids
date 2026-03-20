import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
from logger import log_state, log_event

def main():
    # startup messages
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    
    # initializing game, window, and player sprite
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # setting frames-per-second cap along with .tick() in game loop
    clock = pygame.time.Clock()
    dt = 0

    # grouping objects to make them easier to interact with
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    # create player sprite and calculate starting location
    player_sprite = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # create asteroid field
    asteroid_field = AsteroidField()

    # update game state for each frame
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        
        # update position of all objects
        updatable.update(dt)

        # check for collision with player
        for astr in asteroids:
            if player_sprite.collides_with(astr):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(astr):
                    log_event("asteroid_shot")
                    astr.kill()
                    shot.kill()

        # draw all drawable objects 
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # syncs object movement rate with frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
