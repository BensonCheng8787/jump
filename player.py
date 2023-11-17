import pygame
from plat import Plat

class Player:
    def __init__(self, x, y, size, color):
        # left, top, width, height
        self.rect = pygame.Rect(x, y, size, size)
        self.circle = None
        self.im = []
        self.im.append(pygame.transform.scale(pygame.image.load("jawn0.png"), (size,size)))
        self.im.append(pygame.transform.scale(pygame.image.load("jawn1.png"), (size,size)))
        self.im.append(pygame.transform.scale(pygame.image.load("jawn2.png"), (size,size)))
        self.size = size
        self.color = color
        self.JUMP_HEIGHT = 15    # jump height
        self.X_Vel = 3            # horizontal movement
        self.Velocity = 0
        self.jumping = False
        self.gravity = 1
        self.freeFall = True
        self.running = True
        self.ended= False
        self.steppre = 0
        self.step=0

        # location of a collision of the player with other objects
        self.collision_types = {'top': Plat, 'bottom': Plat, 'left': Plat, 'right': Plat}

    # jump simulates gravity accelerating downward with initial velocity upward
    # collides with bottom of platforms
    def jump(self, platforms):
        self.collision_types['bottom'] == None

        if(not self.jumping):
            self.Velocity = self.JUMP_HEIGHT
        self.jumping = True

        # hits top of the screen
        if (self.rect.y <= 0):
            self.rect.y = 1
            self.Velocity = 0

        # platfroms collided with
        hit_list = self.collided_plats(platforms)

        # collison with a platform above the player
        for plat in hit_list:
            if (self.collision_types['left']!=plat and self.collision_types['right']!=plat) and self.rect.bottom >= plat.rect.bottom:
                self.rect.top = plat.rect.bottom
                self.collision_types['top'] = plat
                self.Velocity = 0
            else:
                self.collision_types['top'] = None
        self.check_free_fall(platforms)


    # includes x collisons with platforms
    def move_sideways(self, keys, platforms):
        # moving left or right
        moving = "none"
        # movment
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 0:
            self.rect.x -= self.X_Vel
            moving = "left"
            self.steppre+=1
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.x+self.size < pygame.display.Info().current_w:
            self.rect.x += self.X_Vel
            moving = "right"
            self.steppre+=1
        if(self.steppre>5): self.step = 1
        if(self.steppre>10): self.step = 2
        if(self.steppre>15): self.step = 1
        if(self.steppre>20):
            self.step =0
            self.steppre =0
        # platfroms collided with
        hit_list = self.collided_plats(platforms)

        # collison with left or right sides of a platform
        for plat in hit_list:
            
            # if (self.freeFall == False and self.collision_types['left']!=plat and self.collision_types['right']!=plat) and self.rect.bottom >= plat.rect.bottom:
            #     self.rect.top = plat.rect.bottom
            #     self.collision_types['top'] = plat
            #     self.Velocity = 0
            #     break
            
            # moving left hits right side of a plat
            if moving == "left" and self.rect.right >= plat.rect.right and (self.collision_types['top']!=plat and self.collision_types['bottom']!=plat):
                self.rect.left = plat.rect.right
                self.collision_types['left'] = plat
            else:
                self.collision_types['left'] = None

            # moving right hits left side of a plat
            if moving == "right" and self.rect.left <= plat.rect.left and (self.collision_types['top']!=plat and self.collision_types['bottom']!=plat):
                self.rect.right = plat.rect.left
                self.collision_types['right'] = plat
            else:
                self.collision_types['right'] = None

    # accelerates downward until a platform is hit
    def apply_gravity(self, gravity, platforms):
        # accelerate downward, jumps if velocity is positive
        if self.collision_types['bottom'] == None or self.jumping == True:
            # terminal Velocity
            if self.Velocity <= -10:
                self.Velocity = -10
            self.rect.y -= self.Velocity
            self.Velocity -= gravity
            # if the jump is over
            if self.Velocity <= 0:
                self.jumping = False


        # platfroms collided with
        hit_list = self.collided_plats(platforms)
        
        # collison with a platform below the player
        for plat in hit_list:
            ##print(self.rect.right, plat.rect.right, self.rect.right <= plat.rect.left)
            if (self.collision_types['left']!=plat and self.collision_types['right']!=plat) and self.rect.top <= plat.rect.top and not self.jumping:
                self.rect.bottom = plat.rect.top + 1
                self.collision_types['bottom'] = plat
                self.Velocity = 0
        self.check_free_fall(platforms)
            
 
    def collided_plats(self, platforms):
        # tiles collided 
        hit_list = []
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                if(plat.type=="end"):
                    self.running=False
                    self.ended = True
                else:
                    hit_list.append(plat)
        return hit_list
    
    def in_range(self, plat):
        # tiles collided 
        if self.circle.colliderect(plat.rect):
            return plat
        return 0
    
    def movement(self, platforms, keys):
        
        # Apply gravity
        self.apply_gravity(self.gravity, platforms)
        
        # jumping
        if (self.jumping):
            self.jump(platforms)
        elif((keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.collision_types['bottom'] != None):
            self.jumping = False
            self.jump(platforms)

        # Move sideways and check x collisions
        self.move_sideways(keys, platforms)

        ##print(self.collision_types, self.jumping, self.Velocity, self.freeFall)


    def draw(self, surface):
        self.circle = pygame.draw.circle(surface, (255, 0, 128), (self.rect.x+30, self.rect.y+30), 200)
        surface.blit(self.im[self.step], (self.rect.x,self.rect.y))
        
        # pygame.Surface.blit(self.im, surface, (self.rect.x,self.rect.y))
        # pygame.draw.rect(surface, self.color, self.rect)

    def check_free_fall(self, platforms):
        # platfroms collided with
        hit_list = self.collided_plats(platforms)
        # free fall
        if len(hit_list) == 0:
            self.collision_types['top'] = None
            self.collision_types['bottom'] = None
            self.collision_types['right'] = None
            self.collision_types['left'] = None
            if(not self.jumping):self.freeFall = True
        else:
            self.freeFall = False

    #resets to default
    def reset(self):
        self.rect.y = 100
        self.rect.x= 400