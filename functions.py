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
    # print(plat.appear,plat.width//10, plat.height//10,"    ", plat.current_plat.width, plat.current_plat.height,"    ",plat.current_plat.x, plat.current_plat.y, "    ", plat.rect.x, plat.rect.y, "   ", plat.current_plat.center, plat.rect.center)
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
    
    text_size = int(button_h//1.3)
    # resume text:
    font = pygame.font.SysFont("comicsansms", text_size)
    resume_txt = font.render("resume", True, (255, 255, 255))
    resume_txt_rect = resume_txt.get_rect()
    resume_txt_rect.center = menus[0].rect.center
    
    # quit text:
    font = pygame.font.SysFont("comicsansms", text_size)
    quit_txt = font.render("quit", True, (255, 255, 255))
    quit_txt_rect = quit_txt.get_rect()
    quit_txt_rect.center = menus[1].rect.center
    
    # options text:
    font = pygame.font.SysFont("comicsansms", text_size)
    options_txt = font.render("options", True, (255, 255, 255))
    options_txt_rect = options_txt.get_rect()
    options_txt_rect.center = menus[2].rect.center
    # options Top text:
    font = pygame.font.SysFont("comicsansms", text_size)
    options1_txt = font.render("course1", True, (255, 255, 255))
    options1_txt_rect = options1_txt.get_rect()
    options1_txt_rect.center = menus[4].rect.center
    
    # options Mid text:
    font = pygame.font.SysFont("comicsansms", text_size)
    options2_txt = font.render("course2", True, (255, 255, 255))
    options2_txt_rect = options2_txt.get_rect()
    options2_txt_rect.center = menus[5].rect.center
    
    # options Bottom text:
    font = pygame.font.SysFont("comicsansms", text_size)
    options3_txt = font.render("course3", True, (255, 255, 255))
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
        
def Main_Course():
    PLATFORM_COLOR = (0, 255, 0)
    TST = (0, 0, 255)
    PLAT_SIZE = 18
    
    # Get screen info 
    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h
    
    # plat takes in (x, y), width, thickness, type, color
    # sec1
    course = [Plat((screen_width-200,screen_height-60), 200, PLAT_SIZE, "norm",PLATFORM_COLOR),#0
              Plat((screen_width-240,screen_height-115), 75, PLAT_SIZE, "norm",PLATFORM_COLOR)]#1
    course.append(Plat((course[1].x-100,course[1].y-30), 65, PLAT_SIZE, "norm",PLATFORM_COLOR))#2
    course.append(Plat((course[2].x-100,course[2].y-30), 65, PLAT_SIZE, "norm",PLATFORM_COLOR))#3
    course.append(Plat((course[3].x+100,course[3].y-60), 65, PLAT_SIZE, "norm",PLATFORM_COLOR))#4
    course.append(Plat((course[4].x+120,course[4].y+20), 88, PLAT_SIZE, "norm",PLATFORM_COLOR))#5
    course.append(Plat((course[5].x+140,course[5].y-40), 65, PLAT_SIZE, "norm",PLATFORM_COLOR))#6
    # sec2
    course.append(Plat((course[6].x-150,course[6].y-50), 100, PLAT_SIZE, "norm",PLATFORM_COLOR))#7
    course.append(Plat((course[7].x,course[7].y-100), PLAT_SIZE, 100, "norm",PLATFORM_COLOR))#8
    course.append(Plat((course[8].x+PLAT_SIZE,course[8].y+40), 30, PLAT_SIZE, "norm",PLATFORM_COLOR))#9
    course.append(Plat((course[8].x-180,course[8].y), 100, PLAT_SIZE, "norm",PLATFORM_COLOR))#10
    course.append(Plat((course[8].x+100,course[8].y), 130, PLAT_SIZE, "norm",PLATFORM_COLOR))#11
    course.append(Plat((course[11].x+115,course[11].y-140), PLAT_SIZE, 140, "norm",PLATFORM_COLOR))#12
    course.append(Plat((course[12].x-20,course[12].y+80), 30, PLAT_SIZE, "norm",PLATFORM_COLOR))#13
    course.append(Plat((course[13].x-70,course[13].y-110), PLAT_SIZE, 130, "norm",PLATFORM_COLOR))#14
    course.append(Plat((course[14].x+15,course[14].y+65), 20, PLAT_SIZE, "norm",PLATFORM_COLOR))#15
    course.append(Plat((course[14].x-40,course[14].y-2), 58, PLAT_SIZE, "norm",PLATFORM_COLOR))#16
    course.append(Plat((course[16].x-70,course[16].y+30), 35, PLAT_SIZE, "norm",PLATFORM_COLOR))#17
    course.append(Plat((course[17].x-70,course[17].y+30), 40, PLAT_SIZE, "norm",PLATFORM_COLOR))#18
    # sec3
    course.append(Plat((course[18].x-60,course[18].y-30), 20, PLAT_SIZE, "norm",PLATFORM_COLOR))#19
    course.append(Plat((course[19].x-PLAT_SIZE,course[19].y-40), PLAT_SIZE, 40+PLAT_SIZE, "norm",PLATFORM_COLOR))#20
    course.append(Plat((course[20].x+80,course[20].y-30), 30, PLAT_SIZE, "norm",PLATFORM_COLOR))#21
    course.append(Plat((course[21].x+80,course[21].y-35), 35, PLAT_SIZE, "norm",PLATFORM_COLOR))#22
    course.append(Plat((course[22].x+70,course[22].y-30), PLAT_SIZE, 40, "norm",PLATFORM_COLOR))#23
    course.append(Plat((course[23].x+55,course[23].y-30), 20, PLAT_SIZE, "norm",PLATFORM_COLOR))#24
    course.append(Plat((course[24].x-70,course[24].y-40), 25, PLAT_SIZE, "norm",PLATFORM_COLOR))#25
    course.append(Plat((course[25].x-70,course[25].y-40), 20, PLAT_SIZE, "norm",PLATFORM_COLOR))#26
    course.append(Plat((course[26].x-60,course[26].y-40), PLAT_SIZE, PLAT_SIZE, "norm",PLATFORM_COLOR))#27
    course.append(Plat((course[27].x-50,course[27].y+40), PLAT_SIZE, PLAT_SIZE, "norm",PLATFORM_COLOR))#28
    course.append(Plat((course[28].x-80,course[28].y+50),PLAT_SIZE,PLAT_SIZE,"end", (255,0,0))) #29 end




    

    return course