import pygame
import random

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

    @staticmethod
    ##returns a course of #num platforms randomly generated.
    def makeCourse(num):
        course = []
        for c in range(0,num):
            hv = random.randint(0,2)
            xpos = random.randint(50,500)
            ypos = random.randint(50,700)
            if(hv%2==0):
                ##height = random.randint(100,600)
                width = random.randint(100,800)
                thick = random.randint(3,30)
            else:
                ##height = random.randint(100,600)
                width = random.randint(10,80)
                thick = random.randint(100,400)
            course.append(Plat((xpos,ypos), width, thick))

        return(course)

