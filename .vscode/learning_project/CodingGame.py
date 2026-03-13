import pygame
import time
import os
from sys import exit

NEMOPHILA_BLUE = (143, 203, 235)
ROAD_COLOR = (80,80,80)
Screen_width = 512
Screen_height = 512
Road_height = 100

background = pygame.image.load(os.path.join("image","PeroroDayTime.png"))
background = pygame.transform.scale(background,(512,445))
Icon = pygame.image.load(os.path.join("image","Perorodzilla_Icon.png"))
road = pygame.Rect(0,Screen_height-Road_height,Screen_width,Road_height)
peroro = pygame.image.load(os.path.join("image","peroro_left.png"))
peroro = pygame.transform.scale(peroro,(50,50))
town = pygame.image.load(os.path.join("image","PeroroTownMain.png"))
town = pygame.transform.scale(town,(610,512))

def draw():
    screen.fill(NEMOPHILA_BLUE)
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,ROAD_COLOR,road)
    screen.blit(town,(-34,Road_height-60))

    player.draw(screen)

pygame.init()
screen = pygame.display.set_mode((Screen_width,Screen_height))                             #HIGHILIGHT#
clock = pygame.time.Clock()
pygame.display.set_caption("PeroroRun")
pygame.display.set_icon(Icon)

class Player:
    def __init__(self):
        self.image = peroro
        self.rect = self.image.get_rect()
        self.rect.midbottom = (200, road.top)
        self.velocity_y = 0
        self.on_ground = True
    def move(self,keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -=5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x +=5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Screen_width:
            self.rect.right = Screen_width

    def update(self):
        self.velocity_y += 1 
        self.rect.y += self.velocity_y
        if self.rect.bottom >= road.top:
            self.rect.bottom = road.top
            self.velocity_y = 0
            self.on_ground = True
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
    def draw(self,screen):
        screen.blit(self.image,self.rect)

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.update()

    draw()
    pygame.display.update()
    clock.tick(60)
#------------------------------------------------