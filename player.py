import pygame

class Player:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
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
        # gravity
        self.Velocity -= grav
        if self.Velocity < -self.JUMP_HEIGHT:
            self.jumping = False
        

    def move_sideways(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.X_Vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.X_Vel

    def apply_gravity(self, gravity):
        self.rect.y -= self.Velocity
        self.Velocity -= gravity

    def check_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.rect.y > 0:
                    self.rect.y = platform.y - self.rect.height
                    self.on_ground = True
                    self.Velocity = 0

            


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
