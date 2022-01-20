import pygame as pg
import re


class Event:
    def __init__(self, pos=[], new_file_name=''):
        # Pos = (x, y)
        self.pos = pos
        self.new_file_name = new_file_name

    def clear(self):
        self.pos.clear()
        self.new_file_name = ''


class Map:
    """
    Ogni riga e' una stringa di caratteri
    """
    # Tiles types
    grass = '*'
    rocks = '#'
    cave_entr = 'C'

    def __init__(self, resize=1):
        self.tiles = []
        self.events = []
        self.w = 0
        self.h = 0
        self.resize = resize
        self.tile_w = int(30*self.resize)
        self.tile_h = int(30*self.resize)
        self.rocks_img = pg.transform.scale(pg.image.load("assets/rocks.png"),
                                            (self.tile_w, self.tile_h))
        self.grass_img = pg.transform.scale(pg.image.load("assets/grass.png"),
                                            (self.tile_w, self.tile_h))


    def allowed_movement(self):
        return list( [self.grass, self.cave_entr])


    def new_map(self, file_name):
        self.tiles.clear()
        self.events.clear()
        self.w = 0
        self.h = 0

        initial_pos = [] 
        event_count = 0

        # Leggo la mappa da file
        with open(file_name+'.txt', 'r') as f_in:
            for line in f_in:
                line = line.replace( '\n', '')
                if len(line) > self.w:
                    self.w = len(line)
                self.tiles.append(line)
                self.h += 1
        # Leggo gli eventi della mappa
        with open(file_name+'_info.txt', 'r') as f_in:
            for line in f_in:
                if line[0] == '#':
                    continue
                line = line.replace('\n', '')

                # Leggo la posizione iniziale
                if initial_pos == []:
                    initial_pos = line.split()
                    initial_pos = [int(i) for i in initial_pos]
                else:
                    ev_pos = line.split()
                    ev_file_name = ev_pos.pop()
                    ev_pos = [int(i) for i in ev_pos]
                    self.events.append(Event(ev_pos, ev_file_name))
        return initial_pos


    def draw(self, screen, x_center, y_center):
        # Usati per degub
        '''
        print( self.w, "x", self.h, "\n")
        for i in range(self.h):
            print( self.tiles[i], sep="")
        '''
        WIDTH  = (screen.get_width()//self.tile_w) >> 1
        HEIGHT = (screen.get_height()//self.tile_h) >> 1
        # Poco efficente, devo creare la mappa mentre la carico
        # Disegno solo i blocchi all'interno della schermo

        # Range della y
        if y_center-HEIGHT < 0:
            y_min_range = 0
        else:
            y_min_range = y_center-HEIGHT
        if y_center+HEIGHT > self.h:
            y_max_range = self.h
        else:
            y_max_range = y_center+HEIGHT

        for i in range(y_min_range, y_max_range):
            # Range della x
            if x_center-WIDTH < 0:
                x_min_range = 0
            else:
                x_min_range = x_center-WIDTH
            if x_center+WIDTH > len(self.tiles[i]):
                x_max_range = len(self.tiles[i])
            else:
                x_max_range = x_center+WIDTH

            for j in range(x_min_range, x_max_range):
                if   self.tiles[i][j] == self.rocks:
                    screen.blit(self.rocks_img,
                                (self.tile_w * (j-x_center+WIDTH), self.tile_h * (i-y_center+HEIGHT)))
                elif self.tiles[i][j] == self.grass:
                    screen.blit(self.grass_img,
                                (self.tile_w * (j-x_center+WIDTH), self.tile_h * (i-y_center+HEIGHT)))



    # Implementare altri eventi oltre a nuove mappe
    def new_event(self, pos=[]):
        for a in self.events:
            if a.pos == pos:
                return a.new_file_name


    def is_event(self, pos=[]):
        # Implementare altri eventi oltre a nuove mappe
        for a in self.events:
            if a.pos == pos:
                return True
        return False


