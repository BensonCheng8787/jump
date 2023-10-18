import pygame

class Player:
    def __init__(self, x, y, size, color):
        # left, top, width, height
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.color = color
        self.JUMP_HEIGHT = 15    # jump height
        self.X_Vel = 3            # horizontal movement
        self.Velocity = 0
        self.jumping = False
        self.gravity = 1

        # location of a collision of the player with other objects
        self.collision_types = {'top': False, 'bottom': False, 'left': False, 'right': False}

    # jump simulates gravity accelerating downward with initial velocity upward
    # collides with bottom of platforms
    def jump(self, platforms):
        self.collision_types['bottom'] == False

        if(not self.jumping):
            self.Velocity = self.JUMP_HEIGHT
        self.jumping = True

        # hits top of the screen
        if (self.rect.y <= 0):
            self.rect.y = 1

        if self.Velocity < -self.JUMP_HEIGHT:
            self.jumping = False

        # platfroms collided with
        hit_list = self.collided_plats(platforms)

        # collison with a platform above the player
        for plat in hit_list:
            if self.rect.bottom >= plat.rect.bottom:
                self.rect.top = plat.rect.bottom
                self.collision_types['top'] = True
                self.Velocity = 0
            else:
                self.collision_types['top'] = False
        self.check_free_fall(platforms)


    # includes x collisons with platforms
    def move_sideways(self, keys, platforms):
        # moving left or right
        moving = "none"
        
        # movment
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.X_Vel
            moving = "left"
        elif keys[pygame.K_RIGHT] and self.rect.x+self.size < pygame.display.Info().current_w:
            self.rect.x += self.X_Vel
            moving = "right"

        # platfroms collided with
        hit_list = self.collided_plats(platforms)

        # collison with left or right sides of a platform
        for plat in hit_list:
            # moving left hits right side of a plat
            if (self.jumping==True or self.collision_types['top']) == False and self.collision_types['bottom']== False:
                if moving == "left" and self.rect.right >= plat.rect.right:
                    self.rect.left = plat.rect.right
                    self.collision_types['left'] = True
                else:
                    self.collision_types['left'] = False

                # moving right hits left side of a plat
                if moving == "right" and self.rect.left <= plat.rect.left:
                    self.rect.right = plat.rect.left
                    self.collision_types['right'] = True
                else:
                    self.collision_types['right'] = False

    # accelerates downward until a platform is hit
    def apply_gravity(self, gravity, platforms):
        # accelerate downward, jumps if velocity is positive
        if self.collision_types['bottom'] == False or self.jumping == True:
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
            if self.rect.top <= plat.rect.top and not self.jumping:
                self.rect.bottom = plat.rect.top + 1
                self.collision_types['bottom'] = True
                self.Velocity = 0
        self.check_free_fall(platforms)
            
 
    def collided_plats(self, platforms):
        # tiles collided 
        hit_list = []
        for plat in platforms:
            if self.rect.colliderect(plat.rect):
                hit_list.append(plat)
        return hit_list
    
    def movement(self, platforms, keys):
        # self.collision_types['top'] = False
        # self.collision_types['bottom'] = False
        # self.collision_types['right'] = False
        # self.collision_types['left'] = False

        # jumping
        if (self.jumping):
            self.jump(platforms)
        elif(keys[pygame.K_SPACE] and self.collision_types['bottom'] == True):
            self.jumping = False
            self.jump(platforms)
        
        # Apply gravity
        self.apply_gravity(self.gravity, platforms)

        # Move sideways and check x collisions
        self.move_sideways(keys, platforms)

        print(self.collision_types, self.jumping, self.Velocity)


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def check_free_fall(self, platforms):
        # platfroms collided with
        hit_list = self.collided_plats(platforms)
        # free fall
        if len(hit_list) == 0:
            self.collision_types['top'] = False
            self.collision_types['bottom'] = False
            self.collision_types['right'] = False
            self.collision_types['left'] = False

    #resets to default
    def reset(self):
        self.rect.y = 100
        self.rect.x= 400