import pygame
import player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state

def main():
    # startup messages
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # initializing game, window, and player sprite
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # setting frames-per-second cap along with .tick() in game loop
    clock = pygame.time.Clock()
    dt = 0

    # grouping objects to make them easier to interact with
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add player object to groups and calculate starting location
    player.Player.containers = (updatable, drawable)
    player_sprite = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # update game state for each frame
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # syncs object movement rate with frame rate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
