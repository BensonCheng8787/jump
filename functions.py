import pygame

# appear function to make platforms and menus appear on screen
def appear(screen, plat):
    # increases based on how wide or tall it is, center stays the same
    plat.current_plat = pygame.Rect(plat.x + plat.width//2, plat.y + plat.height//2, plat.current_plat.width + plat.width//10, plat.current_plat.height + plat.height//10)
    plat.current_plat.center = plat.rect.center
    
    # stops once it reaches the platforms size
    if(plat.current_plat.width >= plat.width):
        plat.current_plat.width = plat.width
    if(plat.current_plat.height >= plat.height):
        plat.current_plat.height = plat.height
        
    # once the size is the same, appearing is True
    if(plat.current_plat.width >= plat.width and plat.current_plat.height >= plat.height):
        plat.current_plat = plat.rect
        plat.appear = True
        
    pygame.draw.rect(screen, plat.color, plat.current_plat)
    
# disappear function to make platforms and menus disappear 
def disappear(screen, plat):
    # decreases based on how wide or tall it is, center stays the same
    plat.current_plat = pygame.Rect(plat.x + plat.width//2, plat.y + plat.height//2, plat.current_plat.width - plat.width//10, plat.current_plat.height - plat.height//10)
    plat.current_plat.center = plat.rect.center
    
    print(plat.appear,plat.width//10, plat.height//10, "    ",plat.current_plat.x, plat.current_plat.y, "    ", plat.rect.x, plat.rect.y, "   ", plat.current_plat.center, plat.current_plat.center)

    
    # stops once it reaches 0
    if(plat.current_plat.width <= 1):
        plat.current_plat.width = 1
    if(plat.current_plat.height <= 1):
        plat.current_plat.height = 1
        
    # once the size is 0, appearing is False
    if(plat.current_plat.width <= 1 and plat.current_plat.height <= 1):
        plat.appear = False
        
    pygame.draw.rect(screen, plat.color, plat.current_plat)
            

# Function to draw button
def draw_button(button_selected, screen, player):
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
