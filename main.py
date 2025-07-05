#Imports
import pygame
from obj import Cube
from render import Renderer

#Global Vars
resolution = 1000, 1000
half_res = 500
caption = "3D Cube Prototype"
tfps = 30
running = True
bg_color = 0, 0, 0
cube = Cube()
tick = 0
index = 0

#Main Block
    #Init program
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption(caption)
clock = pygame.time.Clock()
renderer = Renderer(cube, screen, half_res)

    #Main Loop
while running:
    #Update display & reset buffer
    clock.tick(tfps)
    pygame.display.flip()
    screen.fill(bg_color)

    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Render
    tick += 1
    if (0 == tick % 90):
        tick = 0
        index += 1
        index %= 3
    match index:
        case 0:
            renderer.draw_vertexs()
        case 1:
            renderer.draw_edges()
        case 2:
            renderer.draw_faces()
        case _:
            pass
    cube.rotate(0.06,0.02,0.01)
    
