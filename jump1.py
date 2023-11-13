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
selected = None

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

# Function to draw button
def draw_button(button_selected):
    button_w = 80
    button_h = 22
    dist_from_player = 10
    color1 = (0, 100, 255)
    color2 = (240, 60, 60)
    
    
    # resume text:
    font = pygame.font.SysFont("comicsansms", button_h-1)
    resume_txt = font.render("resume", True, (255, 255, 255))
    resume_txt_rect = resume_txt.get_rect()
    resume_txt_rect.center = (player.rect.x+player.size/2, player.rect.y-dist_from_player-button_h/2-4)
    
    # quit text:
    font = pygame.font.SysFont("comicsansms", button_h-1)
    quit_txt = font.render("quit", True, (255, 255, 255))
    quit_txt_rect = quit_txt.get_rect()
    quit_txt_rect.center = (player.rect.x+player.size/2, player.rect.y+player.size+dist_from_player+button_h/2-4)
    screen.blit(quit_txt, quit_txt_rect)
    
    # options text:
    font = pygame.font.SysFont("comicsansms", button_h-1)
    options_txt = font.render("options", True, (255, 255, 255))
    options_txt_rect = options_txt.get_rect()
    options_txt_rect.center = (player.rect.x-button_w/2-dist_from_player, player.rect.y+player.size/2-3)
    screen.blit(options_txt, options_txt_rect)
    
    # # quit text:
    # font = pygame.font.SysFont("comicsansms", button_h-2)
    # quit_txt = font.render("quit", True, (255, 255, 255))
    # quit_txt_rect = quit_txt.get_rect()
    # quit_txt_rect.center = (player.rect.x+player.size/2, player.rect.y+dist_from_player+button_h/2+3)
    # screen.blit(quit_txt, quit_txt_rect)
    
    # resume button centered above player, switches color when selected
    if button_selected == "up":
        pygame.draw.rect(screen, color2, pygame.Rect((player.rect.x + player.size/2) - button_w/2, (player.rect.y) - button_h - dist_from_player, button_w, button_h))
    else:
        pygame.draw.rect(screen, color1, pygame.Rect((player.rect.x + player.size/2) - button_w/2, (player.rect.y) - button_h - dist_from_player, button_w, button_h))
    screen.blit(resume_txt, resume_txt_rect)
    
    # quit button centered below player, switches color when selected
    if button_selected == "down":
        pygame.draw.rect(screen, color2, pygame.Rect((player.rect.x + player.size/2) - button_w/2, player.rect.y + player.size + dist_from_player, button_w, button_h))
    else:
        pygame.draw.rect(screen, color1, pygame.Rect((player.rect.x + player.size/2) - button_w/2, player.rect.y + player.size + dist_from_player, button_w, button_h))
    screen.blit(quit_txt, quit_txt_rect)

    # options button centered left of player, switches color when selected
    if button_selected == "left":
        pygame.draw.rect(screen, color2, pygame.Rect(player.rect.x - button_w - dist_from_player, player.rect.y + player.size/2 - button_h/2, button_w, button_h))
    else:
        pygame.draw.rect(screen, color1, pygame.Rect(player.rect.x - button_w - dist_from_player, player.rect.y + player.size/2 - button_h/2, button_w, button_h))
    screen.blit(options_txt, options_txt_rect)

    #  button centered right of player, switches color when selected
    if button_selected == "right":
        pygame.draw.rect(screen, color2, pygame.Rect((player.rect.x + player.size) + dist_from_player, player.rect.y + player.size/2 - button_h/2, button_w, button_h))
    else:
        pygame.draw.rect(screen, color1, pygame.Rect((player.rect.x + player.size) + dist_from_player, player.rect.y + player.size/2 - button_h/2, button_w, button_h))

    
# Game loop
running = True
paused = False
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
                    platforms.append(Plat((100,400),30,30,True))
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

            if(plat.end==True):
                pygame.draw.rect(screen,(255,0,0),plat)
            else:
                # the middle of the character has a 200 pixel radius, platforms only spawn in this circle/square
                platform = player.in_range(plat)
                if (platform != 0):
                    pygame.draw.rect(screen, PLATFORM_COLOR, plat)

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
        draw_button(selected)
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
