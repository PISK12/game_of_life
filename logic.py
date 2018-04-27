from math import sqrt
from random import randint


class Logic(object):
    def __init__(self, length, density):
        self.length = length
        self.length_one_row = int(sqrt(self.length))
        self.density = density
        self.all_square = [False for x in range(self.length)]
        self.stan_creative_mode = False
        self.select_number_rect = 0
        self.select_number_rect_last = self.select_number_rect
        self.last_all_square = None

    def change_creative_mode(self):
        if self.stan_creative_mode:
            self.stan_creative_mode = False
        elif not self.stan_creative_mode:
            self.stan_creative_mode = True
            self.last_all_square = self.all_square

    def random_square(self):
        list_square = []
        for square in self.all_square:
            rand = randint(0, 10)
            if rand < self.density:
                list_square.append(True)
            else:
                list_square.append(False)
        self.all_square = list_square

    def change_select_number_rect(self, side):
        if side == "UP":
            self.select_number_rect -= 1
        elif side == "DOWN":
            self.select_number_rect += 1
        elif side == "LEFT":
            self.select_number_rect -= self.length_one_row
        elif side == "RIGHT":
            self.select_number_rect += self.length_one_row

    def check_neighbour(self, number):
        if number not in range(self.length):
            return False
        elif self.all_square[number]:
            return True
        else:
            return False


    def mode_creative(self):
        for position, square in enumerate(self.all_square):
            if square == -1:
                self.all_square[position] = self.last_all_square[position]
        self.last_all_square = self.all_square
        if self.select_number_rect<=self.length:

            self.all_square[self.select_number_rect] = -1
        else:
            self.select_number_rect=self.select_number_rect-self.length_one_row

    def clear(self):
        self.all_square = [False for x in range(self.length)]

    def list_neighbour(self,number):
        list_neighbour = [number - self.length_one_row - 1, number - self.length_one_row,
                          number - self.length_one_row + 1,
                          number - 1, number + 1, number + self.length_one_row - 1, number + self.length_one_row,
                          number + self.length_one_row + 1]

        list_neighbour = list(
            filter(lambda x: x % self.length_one_row != 1 and x % self.length_one_row != 0, list_neighbour))
        list_neighbour=list(filter(lambda x: x in range(self.length+1,list_neighbour)))
        return list_neighbour



    def next_population(self):
        list_square = []
        for number, square in enumerate(self.all_square):
            list_neighbour=self.list_neighbour(number)

            how_many_life = []
            for element in list_neighbour:
                result = self.check_neighbour(element)
                how_many_life.append(result)
            how_many_life = how_many_life.count(True)

            if square:
                if how_many_life < 2 or how_many_life > 4:
                    list_square.append(False)
                else:
                    list_square.append(True)
            elif not square:
                if how_many_life == 3:
                    list_square.append(True)
                else:
                    list_square.append(False)

        self.all_square = list_square
        print(how_many_life)
        print(list_neighbour)
        print(list_square)
        exit()
