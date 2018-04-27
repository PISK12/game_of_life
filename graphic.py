from sys import exit

import pygame


class Rect(object):
    blue = (0, 0, 255)
    white = (255, 255, 255)
    orange=(255,153,0)

    def __init__(self, screen, x, y, length, status=False):
        self.surface = screen


        self.x = x
        self.y = y
        self.length = length
        self.box = pygame.Rect(self.x, self.y, self.length, self.length)

        self.status = status
        self.last=None
        self.set_color()

    def change_status(self):
        if self.status:
            self.status = False
        elif not self.status:
            self.status = True

    def set_color(self):
        if self.status:
            self.color = self.blue
        elif not self.status:
            self.color = self.white


    def draw_it(self):
        self.rect = pygame.draw.rect(self.surface, self.color, self.box)

    def __str__(self):
        return str(self.status) + " " + str(self.box.x) + " " + str(self.box.y)




class Board(object):
    def __init__(self, rest=500):
        pygame.init()
        self.rest = rest
        self.screen = pygame.display.set_mode((self.rest, self.rest))
        self.listRect = []

    def initation_rect(self):
        self.lenght = 9
        ran = range(0, self.rest, 10)
        for x in ran:
            for y in ran:
                rect = Rect(self.screen, x, y, self.lenght)
                self.listRect.append(rect)

    def chack_change_status_in_rect(self, list):
        for position, element in enumerate(self.listRect):
            if list[position]==-1:
                element.color=Rect.orange
            elif list[position]==True or list[position] ==False:
                if list[position] != element.status:
                    element.change_status()
                    element.set_color()


    def draw(self):
        for rect in self.listRect:
            rect.draw_it()


if __name__ == '__main__':
    board = Board()
    surface = board.screen
    board.initation_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                exit()
        board.draw()
        pygame.display.flip()
        pygame.time.Clock().tick(20)
