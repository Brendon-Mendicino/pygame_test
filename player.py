
import pygame
import mappa

class Player():

    # Current img displayed
    img_f = 0
    img_r = 1
    img_l = 2
    img_b = 3

    def __init__(self, resize=1):
        self.x = 0
        self.y = 0
        self.resize = resize
        self.img_w = int(30*resize)
        self.img_h = int(30*resize)

        self.img_f = pygame.transform.scale(pygame.image.load('assets/player_main_front.png'),
                                          (self.img_w, self.img_h))
        self.img_r = pygame.transform.scale(pygame.image.load('assets/player_main_right.png'),
                                                (self.img_w, self.img_h))
        self.img_l = pygame.transform.scale(pygame.image.load('assets/player_main_left.png'),
                                                (self.img_w, self.img_h))
        self.img_b = pygame.transform.scale(pygame.image.load('assets/player_main_back.png'),
                                                (self.img_w, self.img_h))
        self.current_img = self.img_f

    def move(self, dx, dy, mappa):
        # La mappa serve a controllare se il movimento e' valido
        # Update current orientation
        if dx > 0:
            self.current_img = self.img_r
        elif dx < 0:
            self.current_img = self.img_l
        if dy > 0:
            self.current_img = self.img_f
        elif dy < 0:
            self.current_img = self.img_b

        new_x = self.x + dx
        new_y = self.y + dy
        if mappa.tiles[new_y][new_x] in mappa.allowed_movement():
            self.x = new_x
            self.y = new_y

    def set_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def draw(self, screen):
        # Disegna il player sempre al centro della schermo
        orien = self.current_img

        h = screen.get_height() >> 1
        w = screen.get_width() >> 1
        if orien == self.img_f:
            screen.blit(self.img_f, (w, h))
        elif orien == self.img_r:
            screen.blit(self.img_r, (w, h))
        elif orien == self.img_l:
            screen.blit(self.img_l, (w, h))
        elif orien == self.img_b:
            screen.blit(self.img_b, (w, h))
        #screen.blit(self.img, (self.x*self.img_w, self.y*self.img_h))

