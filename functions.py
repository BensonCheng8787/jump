import pygame
from plat import Plat

# appear function to make platforms and menus appear on screen
def appear(screen, plat):
    # increases based on how wide or tall it is, center stays the same
    plat.current_plat = pygame.Rect(plat.x + plat.width//2, plat.y + plat.height//2, plat.current_plat.width + plat.width//10, plat.current_plat.height + plat.height//10)
    
    # stops once it reaches the platforms size
    if(plat.current_plat.width >= plat.width):
        plat.current_plat.width = plat.width
    if(plat.current_plat.height >= plat.height):
        plat.current_plat.height = plat.height
        
    # once the size is the same, appearing is True
    if(plat.current_plat.width >= plat.width and plat.current_plat.height >= plat.height):
        plat.current_plat = plat.rect
        plat.appear = True
        
    plat.current_plat.center = plat.rect.center
    print(plat.appear,plat.width//10, plat.height//10,"    ", plat.current_plat.width, plat.current_plat.height,"    ",plat.current_plat.x, plat.current_plat.y, "    ", plat.rect.x, plat.rect.y, "   ", plat.current_plat.center, plat.rect.center)
    pygame.draw.rect(screen, plat.color, plat.current_plat)    
    
# disappear function to make platforms and menus disappear 
def disappear(screen, plat):
    # decreases based on how wide or tall it is, center stays the same
    plat.current_plat = pygame.Rect(plat.x + plat.width//2, plat.y + plat.height//2, plat.current_plat.width - plat.width//10, plat.current_plat.height - plat.height//10)
    plat.current_plat.center = plat.rect.center
        
    # stops once it reaches 0
    if(plat.current_plat.width <= 1):
        plat.current_plat.width = 1
    if(plat.current_plat.height <= 1):
        plat.current_plat.height = 1
        
    # once the size is 0, appearing is False
    if(plat.current_plat.width <= 1 and plat.current_plat.height <= 1):
        plat.appear = False
        
        
    # print(plat.appear,plat.width//10, plat.height//10,"    ", plat.current_plat.width, plat.current_plat.height,"    ",plat.current_plat.x, plat.current_plat.y, "    ", plat.rect.x, plat.rect.y, "   ", plat.current_plat.center, plat.current_plat.center)
    pygame.draw.rect(screen, plat.color, plat.current_plat)
    
    # pygame.draw.rect(screen, plat.color, pygame.Rect(plat.current_plat.x+100,plat.current_plat.y,plat.current_plat.width,plat.current_plat.height))

# Function to draw button
def draw_button(menus, button_selected, screen, player, dis, clicked):
    button_w = menus[0].width
    button_h = menus[0].height
    dist_from_player = 10   # also defined in jump1
    color1 = (0, 100, 255)
    color2 = (240, 60, 60)
    
    # update locations
    # up, resume button
    menus[0].rect.x = player.rect.x + player.size/2 - button_w/2
    menus[0].rect.y = player.rect.y - button_h - dist_from_player
    # down, quit
    menus[1].rect.x = player.rect.x + player.size/2 - button_w/2
    menus[1].rect.y =  player.rect.y + player.size + dist_from_player
    # left, options
    menus[2].rect.x = player.rect.x - button_w - dist_from_player
    menus[2].rect.y = player.rect.y + player.size/2 - button_h/2
    # right, none
    menus[3].rect.x = player.rect.x + player.size + dist_from_player
    menus[3].rect.y = player.rect.y + player.size/2 - button_h/2
    # options 1, left of options top-most
    menus[4].rect.x = menus[2].rect.x - button_w + dist_from_player
    menus[4].rect.y = menus[2].rect.y - button_h - dist_from_player
    # options 2, left of options middle
    menus[5].rect.x = menus[2].rect.x - button_w - dist_from_player
    menus[5].rect.y = menus[2].rect.y
    # options 3, left of options bottom-most
    menus[6].rect.x = menus[2].rect.x - button_w + dist_from_player
    menus[6].rect.y = menus[2].rect.y + button_h + dist_from_player
    
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
    
    # options text:
    font = pygame.font.SysFont("comicsansms", button_h-1)
    options_txt = font.render("options", True, (255, 255, 255))
    options_txt_rect = options_txt.get_rect()
    options_txt_rect.center = (player.rect.x-button_w/2-dist_from_player, player.rect.y+player.size/2-3)
    
    # options Top text:
    font = pygame.font.SysFont("comicsansms", button_h-1)
    options1_txt = font.render("course 1", True, (255, 255, 255))
    options1_txt_rect = options1_txt.get_rect()
    options1_txt_rect.center = menus[4].rect.center
    
    # options Mid text:
    font = pygame.font.SysFont("comicsansms", button_h-1)
    options2_txt = font.render("course 2", True, (255, 255, 255))
    options2_txt_rect = options2_txt.get_rect()
    options2_txt_rect.center = menus[5].rect.center
    
    # options Bottom text:
    font = pygame.font.SysFont("comicsansms", button_h-1)
    options3_txt = font.render("course 3", True, (255, 255, 255))
    options3_txt_rect = options3_txt.get_rect()
    options3_txt_rect.center = menus[6].rect.center
    
    # # quit text:
    # font = pygame.font.SysFont("comicsansms", button_h-2)
    # quit_txt = font.render("quit", True, (255, 255, 255))
    # quit_txt_rect = quit_txt.get_rect()
    # quit_txt_rect.center = (player.rect.x+player.size/2, player.rect.y+dist_from_player+button_h/2+3)
    # screen.blit(quit_txt, quit_txt_rect)
    
    tmp = 0
    # make the menu appear like the platforms
    for menu in menus:

        if (menus[tmp].appear == False and dis == False):
            if clicked == None:
                if tmp > 3:
                    break
            appear(screen, menu)
        if dis == True:
            menu.appear = False
            menu.current_plat = pygame.Rect(menu.x + menu.width//2, menu.y + menu.height//2, 1, 1)
        tmp+=1

    if menus[0].appear == True:
        # resume button centered above player, switches color when selected
        if button_selected == "up":
            menus[0].color = color2
        else:
            menus[0].color = color1            
        pygame.draw.rect(screen, menus[0].color, menus[0].current_plat)
        
        # quit button centered below player, switches color when selected
        if button_selected == "down":
            menus[1].color = color2
        else:
            menus[1].color = color1            
        pygame.draw.rect(screen, menus[1].color, menus[1].current_plat)

        # options button centered left of player, switches color when selected
        if button_selected == "left":
            menus[2].color = color2
        else:
            menus[2].color = color1            
        pygame.draw.rect(screen, menus[2].color, menus[2].current_plat)

        #  button centered right of player, switches color when selected
        if button_selected == "right":
            menus[3].color = color2
        else:
            menus[3].color = color1            
        pygame.draw.rect(screen, menus[3].color, menus[3].current_plat)
    
        if dis == False:
            screen.blit(resume_txt, resume_txt_rect)
            screen.blit(options_txt, options_txt_rect)
            screen.blit(quit_txt, quit_txt_rect)
            
    if clicked == "left":
        if button_selected == "leftTop":
            menus[4].color = color2
        else:
            menus[4].color = color1            
        pygame.draw.rect(screen, menus[4].color, menus[4].current_plat)
        
        if button_selected == "leftMid":
            menus[5].color = color2
        else:
            menus[5].color = color1            
        pygame.draw.rect(screen, menus[5].color, menus[5].current_plat)
        
        if button_selected == "leftBotm":
            menus[6].color = color2
        else:
            menus[6].color = color1 
        pygame.draw.rect(screen, menus[6].color, menus[6].current_plat)
        
        screen.blit(options1_txt, options1_txt_rect)
        screen.blit(options2_txt, options2_txt_rect)
        screen.blit(options3_txt, options3_txt_rect)
        
