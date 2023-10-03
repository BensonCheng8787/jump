import pygame

class Player:
    def __init__(self, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.vy = 0
        self.on_ground = False

    def jump(self, jumpstr):
        keys = pygame.key.get_pressed()
        if(keys == pygame.K_SPACE and self.on_ground):
            self.vy = -jumpstr

    def move_sideways(self, vel):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += vel

    def apply_gravity(self, gravity):
        self.vy += gravity
        self.rect.y += self.vy

    def check_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vy > 0:
                    self.rect.y = platform.y - self.rect.height
                    self.vy = 0
                    self.on_ground = True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
