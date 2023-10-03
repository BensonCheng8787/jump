import pygame
import win32api
import win32con
import win32gui
from player import Player

# Initialize Pygame
pygame.init()
# Set up the clock
clock = pygame.time.Clock()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 128, 255)
PLATFORM_COLOR = (0, 255, 0)
GRAVITY = 0.001
JUMP_STRENGTH = 20
vel = 5

# Create the player
player = Player(400, 100, PLAYER_SIZE, PLAYER_COLOR)

# Create the platforms
platforms = [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 20)]

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make the window transparent
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)

# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        # Move sideways
        player.move_sideways(5)
        player.jump(JUMP_STRENGTH)
        if event.type == pygame.QUIT:
            running = False
            
    # Apply gravity
    player.apply_gravity(GRAVITY)
    # Check for collisions
    player.check_collisions(platforms)

    # Draw everything
    screen.fill((255, 0, 128))  # Transparent background
    player.draw(screen)
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
