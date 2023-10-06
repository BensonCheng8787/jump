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
PLAYER_SIZE = 30
PLAYER_COLOR = (0, 128, 255)
PLATFORM_COLOR = (0, 255, 0)
GRAVITY = 1

# Create the player
player = Player(400, 100, PLAYER_SIZE, PLAYER_COLOR)

# Create the platforms
platforms = [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 20)]

# Get screen info
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))

# Make the window transparent
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)

# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move sideways
    keys = pygame.key.get_pressed()
    player.move_sideways(keys)

    # jumping
    if (player.jumping):
        player.jump(GRAVITY)
    elif(keys[pygame.K_SPACE]):
        player.jumping = False
        player.jump(GRAVITY)
     
    # Apply gravity
    if not player.jumping and not player.on_ground:
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

    clock.tick(60)

# Quit Pygame
pygame.quit()
