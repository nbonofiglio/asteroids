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
    player_sprite = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # setting frames-per-second cap along with .tick() below
    clock = pygame.time.Clock()
    dt = 0

    # update game state for each frame
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        print(player_sprite.position, player_sprite.radius, player_sprite.rotation)
        triangle_sprite = player_sprite.draw(screen)
        print(triangle_sprite)
        pygame.display.flip()

        # lock sceen to 60 FPS
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
