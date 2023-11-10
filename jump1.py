import pygame
import win32api
import win32con
import win32gui
from player import Player
from plat import Plat
import time

# Initialize Pygame
pygame.init()
# Set up the clock
clock = pygame.time.Clock()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 60
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
platforms = Plat.makeCourse(30, screen_width, screen_height)
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()

    keys = pygame.key.get_pressed()
    player.movement(platforms, keys)
    running = player.running
    # Draw everything
    screen.fill((255, 0, 128))  # Transparent background
    player.draw(screen)
    for plat in platforms:
        # # Create a second surface
        # s = pygame.Surface((plat.x, plat.y), pygame.SRCALPHA)  # Per-pixel alpha

        # # Fill the second surface with white color and 50% transparency
        # s.fill((0, 255, 0, 128))  # Notice the alpha value in the color

        # # Blit the second surface onto the window
        # screen.blit(s, (plat.x, plat.y))

        if(plat.end==True):
            pygame.draw.rect(screen,(255,0,0),plat)
        else:
            pygame.draw.rect(screen, PLATFORM_COLOR, plat)

    # Update the display
    pygame.display.update()
    if(player.rect.y>pygame.display.Info().current_h):
        player.reset()
    clock.tick(60)
if(player.ended):
    font = pygame.font.Font(None, 180)
    text = font.render("IT'S JOEOVER!!!! ", True, (255, 255, 255))
    text_rect = text.get_rect()
    # Set the center of the rectangular object
    text_rect.center = (1000, 500)
    # Draw the text onto the screen
    screen.blit(text, text_rect)
    # Update the display
    pygame.display.flip()
    # Wait for 2 seconds
    time.sleep(1)

# Quit Pygame
pygame.quit()
