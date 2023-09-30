import pygame
import win32api
import win32con
import win32gui

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 128, 255)
PLATFORM_COLOR = (0, 255, 0)
GRAVITY = 1
JUMP_STRENGTH = 20
vel = 5

# Create the player
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
player_vy = 0
on_ground = False

# Create the platforms
platforms = [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 20)]

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make the window transparent
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)

##sideway movement
def move_sideways(player, vel):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= vel
    if keys[pygame.K_RIGHT]:
        player.x += vel


# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and on_ground:
            player_vy = -JUMP_STRENGTH

    # Apply gravity
    player_vy += GRAVITY
    player.y += player_vy

    # Check for collisions
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if player_vy > 0:
                player.y = platform.y - PLAYER_SIZE
                player_vy = 0
                on_ground = True
       # Move sideways
    move_sideways(player, vel)

    # Draw everything
    screen.fill((255, 0, 128))  # Transparent background
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
