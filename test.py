from random import randint
from time import sleep

import pygame

from graphic import Board
from logic import Logic
from run import Connector


class Test_Logic(Logic):
    def random_square(self):
        list_square = []
        for square in self.all_square:
            rand = randint(0, 10)
            if rand < self.density:
                list_square.append(True)
            else:
                list_square.append(False)
        self.all_square = list_square

    def test(self):
        list_square = self.all_square
        int_length_one_row=int(self.length_one_row)
        list_square[int_length_one_row + 2] = True
        list_square[int_length_one_row * 2 + 1] = True
        list_square[int_length_one_row * 3 + 1] = True
        list_square[int_length_one_row * 3 + 2] = True
        list_square[int_length_one_row * 3 + 3] = True
        self.all_square=list_square



class Test_Board(Board):
    pass


class Test_Connector(Connector):
    def __init__(self):
        self.length = 50
        # 1-10 poczatkawa gestosc losowo rozmieszczonych komorek
        self.density = 1

        self.board = Test_Board(self.length * 10)

        self.logic = Test_Logic(self.length ** 2, self.density)

    def before_draw_board(self):
        self.surface = self.board.screen
        self.board.initation_rect()
        self.logic.test()

    def play(self):
        time = 1
        while True:
            self.board.draw()
            self.board.chack_change_status_in_rect(self.logic.all_square)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    time += 1

            self.logic.next_population()
            pygame.display.flip()
            pygame.time.Clock().tick(time)


if __name__ == '__main__':
    conn = Test_Connector()
    conn.before_draw_board()
    sleep(5)
    conn.play()
