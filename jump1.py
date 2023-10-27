import pygame
import win32api
import win32con
import win32gui
from player import Player
from plat import Plat

# Initialize Pygame
pygame.init()
# Set up the clock
clock = pygame.time.Clock()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 30
PLAYER_COLOR = (0, 128, 255)
PLATFORM_COLOR = (0, 255, 0)

# Create the player
player = Player(400, 100, PLAYER_SIZE, PLAYER_COLOR)

# Create the platforms pygame.Rect(0, HEIGHT - 20, WIDTH+400, 20), pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 20)
# plat takes in (x, y), width, thickness
##platforms = [Plat((0,HEIGHT), WIDTH, 20), Plat((400, 500), WIDTH // 4, 20), Plat((100, 200),50,300), Plat((500,200),20,500)]

##positive num to random generate, -1 for set course
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
platforms = Plat.makeCourse(25, screen_width, screen_height)
platforms.append(Plat((100,400),30,30,True))
# Get screen info



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

    keys = pygame.key.get_pressed()
    player.movement(platforms, keys)
    running = player.running
    # Draw everything
    screen.fill((255, 0, 128))  # Transparent background
    player.draw(screen)
    for platform in platforms:
        if(platform.end==True):
            pygame.draw.rect(screen,(255,0,0),platform)
        else:
            pygame.draw.rect(screen, PLATFORM_COLOR, platform)

    # Update the display
    pygame.display.update()
    if(player.rect.y>pygame.display.Info().current_h):
        player.reset()
    clock.tick(60)

# Quit Pygame
pygame.quit()
