import pygame

import constants as u
from asteroid import Asteroid
from ship import Ship

# pygame setup
pygame.init()
screen = pygame.display.set_mode((u.SCREEN_SIZE, u.SCREEN_SIZE))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
running = True
dt = 0

ship = Ship(pygame.Vector2(u.SCREEN_SIZE / 2, u.SCREEN_SIZE / 2))
asteroid = Asteroid()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(u.BACKGROUND_COLOR)

    # pygame.draw.circle(screen,"red",(u.SCREEN_SIZE/2, u.SCREEN_SIZE/2), 3)
    ship.draw(screen)
    asteroid.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        ship.turn_left(dt)
    if keys[pygame.K_LEFT]:
        ship.turn_right(dt)
    if keys[pygame.K_UP]:
        ship.power_on(dt)
    else:
        ship.power_off(dt)
    ship.move(dt)
    asteroid.move(dt)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()