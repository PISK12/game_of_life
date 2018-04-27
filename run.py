from sys import exit

import pygame

from graphic import Board
from logic import Logic


class Connector(object):
    def __init__(self):
        self.length = 50
        # 1-10 poczatkawa gestosc losowo rozmieszczonych komorek
        self.density = 1

        self.board = Board(self.length * 10)

        self.logic = Logic(self.length ** 2, self.density)

    def play(self):
        print(31)
        fps = 1
        while True:
            # print(32)
            self.board.draw()
            self.board.chack_change_status_in_rect(self.logic.all_square)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    print(33)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    fps += 1
                    print(34)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                    self.logic.change_creative_mode()
                    if self.logic.stan_creative_mode:
                        fps = 30
                    print(35)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    self.logic.clear()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    self.logic.random_square()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.logic.change_select_number_rect("UP")
            if self.logic.stan_creative_mode and keys[pygame.K_DOWN]:
                self.logic.change_select_number_rect("DOWN")
            if self.logic.stan_creative_mode and keys[pygame.K_LEFT]:
                self.logic.change_select_number_rect("LEFT")
            if self.logic.stan_creative_mode and keys[pygame.K_RIGHT]:
                self.logic.change_select_number_rect("RIGHT")


            if self.logic.stan_creative_mode:
                self.logic.mode_creative()
            else:
                self.logic.next_population()

            pygame.display.flip()
            pygame.time.Clock().tick(fps)

    def clean(self):
        self.board.initation_rect()

    def before_draw_board(self):
        self.surface = self.board.screen
        self.board.initation_rect()
        self.logic.random_square()


def main():
    print(1)
    conn = Connector()
    print(2)
    conn.before_draw_board()
    print(3)
    conn.play()
    print(4)


if __name__ == '__main__':
    main()
