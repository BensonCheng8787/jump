import pygame

class Player:
    def __init__(self, x, y, size, color):
        # left, top, width, height
        self.rect = pygame.Rect(x, y, size, size)
        self.size = size
        self.color = color
        self.on_ground = False
        self.JUMP_HEIGHT = 25     # jump height
        self.X_Vel = 3            # horizontal movement
        self.Velocity = 0
        self.jumping = False

    def jump(self, grav):
        if(not self.jumping):
            self.Velocity = self.JUMP_HEIGHT
        self.jumping = True
        self.rect.y -= self.Velocity
        if (self.rect.y <= 0):
            self.rect.y = 1
        # gravity
        self.Velocity -= grav
        if self.Velocity < -self.JUMP_HEIGHT:
            self.jumping = False
        

    def move_sideways(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.X_Vel
        if keys[pygame.K_RIGHT] and self.rect.x < pygame.display.Info().current_w:
            self.rect.x += self.X_Vel

    def apply_gravity(self, gravity):
        self.rect.y -= self.Velocity
        self.Velocity -= gravity

    def check_collisions(self, platforms):
        for platform in platforms:
            if platform.y <= self.rect.y+self.size and platform.y >= self.rect.y and platform.x <= self.rect.x+self.size and platform.x+platform.size >= self.rect.x:
                if self.rect.y:
                    self.rect.y = platform.y - self.rect.height
                    self.on_ground = True
                    self.jumping = False
                    self.Velocity = 0
                
            self.on_ground = False

            


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
