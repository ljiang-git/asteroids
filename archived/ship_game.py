import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids - Ship")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ship properties
ship_pos = [WIDTH // 2, HEIGHT // 2]
ship_angle = 0
ship_speed = 5

def draw_ship(screen, position, angle):
    # Define the ship as a triangle
    ship_points = [
        (0, -10),
        (5, 10),
        (-5, 10)
    ]
    
    # Rotate the ship
    rotated_points = []
    for point in ship_points:
        rotated_x = point[0] * math.cos(math.radians(angle)) - point[1] * math.sin(math.radians(angle))
        rotated_y = point[0] * math.sin(math.radians(angle)) + point[1] * math.cos(math.radians(angle))
        rotated_points.append((rotated_x + position[0], rotated_y + position[1]))
    
    # Draw the ship
    pygame.draw.polygon(screen, WHITE, rotated_points)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ship
    draw_ship(screen, ship_pos, ship_angle)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()