import pygame
import win32api
import win32con
import win32gui
from player import Player
from plat import Plat
from functions import *
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
selected = None

# Create the player
player = Player(400, 100, PLAYER_SIZE, PLAYER_COLOR)

# Create the platforms pygame.Rect(0, HEIGHT - 20, WIDTH+400, 20), pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 20)
# plat takes in (x, y), width, thickness
# test course
# platforms = [Plat((0,HEIGHT), WIDTH, 20, 0), Plat((400, 500), WIDTH // 4, 20,0), Plat((100, 200),50,300,0), Plat((500,200),20,500,0)]


# Get screen info 
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

##positive num to random generate, -1 for set course
# test course 2
platforms = Plat.makeCourse(30, screen_width, screen_height)
platforms.append(Plat((100,400),30,30,"end"))

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))

# Make the window transparent
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)
    
# menu platforms
button_w = 80
button_h = 22
dist_from_player = 10
menus = [Plat(((player.rect.x + player.size/2) - button_w/2, (player.rect.y) - button_h - dist_from_player), button_w, button_h, "menu"),
            Plat(((player.rect.x + player.size/2) - button_w/2, player.rect.y + player.size + dist_from_player), button_w, button_h, "menu"),
            Plat((player.rect.x - button_w - dist_from_player, player.rect.y + player.size/2 - button_h/2), button_w, button_h, "menu"),
            Plat(((player.rect.x + player.size) + dist_from_player, player.rect.y + player.size/2 - button_h/2), button_w, button_h, "menu")]

# Game loop
running = True
paused = False
appearing_timer = 0
while running:
    if not paused:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                    selected = None
                if event.key == pygame.K_n:
                    platforms = Plat.makeCourse(30, screen_width, screen_height)
                    platforms.append(Plat((100,400),30,30,"end"))
                    player.reset()
                if event.key == pygame.K_r:
                    player.reset()

        keys = pygame.key.get_pressed()
        player.movement(platforms, keys)
        running = player.running
        
        # Draw everything
        screen.fill((255, 0, 128))  # Transparent background
        player.draw(screen)
        for plat in platforms:
            if(plat.type=="end"):
                pygame.draw.rect(screen,(255,0,0),plat)
            else:
                # the middle of the character has a 200 pixel radius, platforms only spawn in this circle/square
                platform = player.in_range(plat)
                if (platform != 0):
                    # if platform is inrange and not fully appeared yet
                    if (plat.appear == False):
                        appear(screen, plat)
                        
                    else:
                        pygame.draw.rect(screen, PLATFORM_COLOR, plat.rect)
                elif plat.appear == True:
                    disappear(screen, plat)
                else:
                    plat.current_plat = pygame.Rect(plat.x + plat.width//2, plat.y + plat.height//2, 1, 1)
                    plat.current_plat.center = plat.rect.center

        # Update the display
        pygame.display.update()
        if(player.rect.y>pygame.display.Info().current_h):
            player.reset()
        clock.tick(60)

    if paused:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    selected = "up"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    selected = "down"
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    selected = "left"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    selected = "right"
                    
                # if the selected button is pressed
                if event.key == pygame.K_RETURN:
                    if selected == "up":
                        paused = False
                    elif selected == "down":
                        quit()
                    elif selected == "left":
                        None
                    elif selected == "right":
                        None
        draw_button(menus, selected, screen, player)
        pygame.display.update()
                    
    
if(player.ended):
    font = pygame.font.Font(None, 180)
    text = font.render("IT'S JOEOVER!!!! ", True, (255, 255, 255))
    text_rect = text.get_rect()
    
    # Set the center of the rectangular object
    text_rect.center = (WIDTH, HEIGHT/2)
    
    # Draw the text onto the screen
    screen.blit(text, text_rect)
    
    # Update the display
    pygame.display.flip()
    
    # Wait for 2 seconds
    time.sleep(1)

# Quit Pygame
pygame.quit()
