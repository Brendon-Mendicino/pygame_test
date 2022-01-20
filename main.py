
import pygame
from pygame.locals import *

import mappa
import player


pygame.init()


resize = 3
mappa = mappa.Map(resize)
initial_pos = mappa.new_map("map/map01")

player = player.Player(resize)
player.set_pos(initial_pos[0], initial_pos[1])


width = 16
height = 10
screen = pygame.display.set_mode((mappa.tile_w*width, mappa.tile_h*height))
#screen = pygame.display.set_mode((1000, 800))
#screen = pygame.display.set_mode((mappa.tile_w*12, mappa.tile_h*10), HWSURFACE | DOUBLEBUF | RESIZABLE)


loop = True
FPS = 60
clock = pygame.time.Clock()

while loop:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                player.move( 0,  1, mappa)
            elif event.key == K_UP:
                player.move( 0, -1, mappa)
            elif event.key == K_LEFT:
                player.move(-1,  0, mappa)
            elif event.key == K_RIGHT:
                player.move( 1,  0, mappa)


    # Controllo degli eventi sulla mappa
    # TODO: aggiungere altri eventi
    if mappa.is_event([player.x, player.y]) is True:
        file_name = mappa.new_event([player.x, player.y])
        initial_pos = mappa.new_map(file_name)
        player.set_pos(initial_pos[0], initial_pos[1])

    screen.fill((0, 0, 0))
    # La mappa e' centrate nel personaggio
    mappa.draw(screen, player.x, player.y)
    player.draw(screen)
    pygame.display.update()
    

pygame.quit()

