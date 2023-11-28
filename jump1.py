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

# Get screen info 
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Create the player
player = Player(400, 100, PLAYER_SIZE, PLAYER_COLOR)

# Create the platforms pygame.Rect(0, HEIGHT - 20, WIDTH+400, 20), pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 20)
# plat takes in (x, y), width, thickness, type, color
# ===========================test course 1====================================
# platforms = [Plat((0,HEIGHT), WIDTH, 20, "norm",(0, 255, 0)), Plat((400, 500), WIDTH // 4, 20,"norm",(0, 255, 0)), Plat((100, 200),50,300,"norm",(0, 255, 0)), Plat((500,200),20,500,"norm",(0, 255, 0))]

##positive num to random generate, -1 for set course
# ===========================test course 2====================================
platforms = Plat.makeCourse(30, screen_width, screen_height)

# ===========================test course 3====================================


# add end block
platforms.append(Plat((100,400),30,30,"end", (255,0,0)))

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
# locations updated in draw button function
menus = [Plat((0, 0), button_w, button_h, "menu", (0, 100, 255)),
            Plat((0, 0), button_w, button_h, "menu", (0, 100, 255)),
            Plat((0, 0), button_w, button_h, "menu", (0, 100, 255)),
            Plat((0, 0), button_w, button_h, "menu", (0, 100, 255)),
            Plat((0, 0), button_w, button_h, "menu", (0, 100, 255)),
            Plat((0, 0), button_w, button_h, "menu", (0, 100, 255)),
            Plat((0, 0), button_w, button_h, "menu", (0, 100, 255))]

# Game loop
running = True
paused = False
dis = False
clicked = None
selected = None
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
                    platforms.append(Plat((100,400),30,30,"end",(255,0,0)))
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
                pygame.draw.rect(screen,plat.color,plat)
            else:
                # the middle of the character has a 200 pixel radius, platforms only spawn in this circle/square
                platform = player.in_range(plat)
                if (platform != 0):
                    # if platform is inrange and not fully appeared yet
                    if (plat.appear == False):
                        appear(screen, plat)
                    else:
                        pygame.draw.rect(screen, plat.color, plat.rect)
                elif plat.appear == True:
                    disappear(screen, plat)
                else:
                    plat.current_plat = pygame.Rect(plat.x + plat.width//2, plat.y + plat.height//2, 1, 1)
                    plat.current_plat.center = plat.rect.center

        if(player.rect.y>pygame.display.Info().current_h):
            player.reset()
        clock.tick(60)

    if paused:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and dis == False:
                if event.key == pygame.K_ESCAPE:
                    dis = True
                    clicked = None
                    selected = None
                    for menu in menus:
                        menu.color = (0, 100, 255)
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if selected == "leftMid":
                        selected = "leftTop"
                    elif selected == "leftBotm":
                        selected = "leftMid"
                    elif selected == "leftTop":
                        selected = "leftTop"
                    else:
                        selected = "up"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if selected == "leftMid":
                        selected = "leftBotm"
                    elif selected == "leftTop":
                        selected = "leftMid"
                    elif selected == "leftBotm":
                        selected = "leftBotm"
                    else:
                        selected = "down"
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if selected == "left":
                        selected = "leftMid"
                    elif selected != "leftTop" or selected != "leftMid" or selected != "leftBotm":
                        selected = "left"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if selected == "leftTop" or selected == "leftMid" or selected == "leftBotm":
                        selected = "left"
                    else:
                        selected = "right"
                    
                # if the selected button is pressed
                if event.key == pygame.K_RETURN:
                    if selected == "up":
                        dis = True
                        clicked = None
                        selected = None
                        for menu in menus:
                            menu.color = (0, 100, 255)
                    elif selected == "down":
                        quit()
                    elif selected == "left":
                        clicked = "left"
                    elif selected == "right":
                        None

        draw_button(menus, selected, screen, player, dis, clicked)
        
        if(menus[3].appear == False and dis == True):
            print("dis")
            dis = False
            paused = False
            
    # Update the display
    pygame.display.flip()
    
        
    
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
