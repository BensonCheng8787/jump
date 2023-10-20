import pygame

class Plat:
    def __init__(self,loc, width, thickness):
        self.rect = pygame.Rect(loc[0], loc[1],width, thickness)
        self.loc = loc
        self.y = loc[1]
        self.x= loc[0]
        self.thickness = thickness
        self.width = width

        # detects location of where the player is hitting it
        self.collision_types = {'top': False, 'bottom': False, 'left': False, 'right': False}

    def __str__(self):
        return(True)

