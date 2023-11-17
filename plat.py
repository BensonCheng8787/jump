import pygame
import random

class Plat:
    def __init__(self, loc, width, height, type):
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(loc[0], loc[1], width, height)
        self.loc = loc
        self.y = loc[1]
        self.x= loc[0]
        self.height = height
        self.width = width
        self.type = type
        self.appear = False
        self.current_plat = pygame.Rect(self.x + width//2, self.y + height//2, 1, 1)
        self.current_plat.center = self.rect.center

        # detects location of where the player is hitting it
        self.collision_types = {'top': False, 'bottom': False, 'left': False, 'right': False}

    def __str__(self):
        return(True)

    @staticmethod
    ##returns a course of #num platforms randomly generated.
    def makeCourse(num, screenwidth, screenheight):
        course = []
        if(num==-1):
            course.append(Plat((100,200),600,20,"norm"))
        else:
            for c in range(0,num):
                hv = random.randint(0,2)
                xpos = random.randint(50,screenwidth)
                ypos = random.randint(50,screenheight)
                for i in range(0,c):
                    if course[i].x==ypos:
                        ypos+=random.randint(10,20)
                    if course[i].y==xpos:
                        xpos+=random.randint(20,30)
                if(hv%2==0):
                    ##height = random.randint(100,600)
                    width = random.randint(100,800)
                    height = random.randint(10,30)
                else:
                    ##height = random.randint(100,600)
                    width = random.randint(10,80)
                    height = random.randint(100,400)
                course.append(Plat((xpos,ypos), width, height, "norm"))

        return(course)

