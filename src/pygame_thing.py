import pygame
import random

# Loads images
fish1 = pygame.image.load('images/fish1.jpg')
fish2 = pygame.image.load('images/fish2.jpg')
fish3 = pygame.image.load('images/fish3.jpg')

# Homogenizes their size
fish1 = pygame.transform.scale(fish1, (100, 100))
fish2 = pygame.transform.scale(fish2, (100, 100))
fish3 = pygame.transform.scale(fish3, (100, 100))

background_color = (255, 123, 255) 
WIN = pygame.display.set_mode((900, 600)) 

WIN.fill(background_color)

class Object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.fish = fish1
        self.velocity = -1
    
    @staticmethod 
    def new_object():
        new_obj = Object()
        
        object_num = random.randint(1,3)
        object_y = random.randint(100,400)
        
        if object_num == 1:
            new_obj.fish = fish1
        elif object_num == 2:
            new_obj.fish = fish2
        else:
            new_obj.fish = fish3

        new_obj.x = 600
        new_obj.y = object_y
        return new_obj
    
    def move(self):
        self.x += self.velocity

def draw(win, objects):
    for object in objects:
        rect = object.fish.get_rect()
        rect.x = object.x
        rect.y = object.y
        win.blit(object.fish, rect)
    pygame.display.update()

running = True
object = Object.new_object()

while running: 
# for loop through the event queue
    object.move()   
    draw(WIN, [object])

    for event in pygame.event.get(): 
        
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
