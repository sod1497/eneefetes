import copy

from figures.base import BaseFigure
from generators.base import BaseGenerator

ONE_TURN = 1

VALID_DIRECTIONS = ['U', 'D', 'L', 'R']


class Translation(BaseGenerator):

    # TODO: Add starting point

    def __init__(self, figure: BaseFigure, distance: int, direction: str, iterations: int):
        super().__init__()
        self.figure = figure
        self.direction = direction
        self.distance = distance
        self.iterations = iterations

    def draw(self, t):

        aux_x = 0
        for i in range(self.iterations):

            aux_figure = copy.deepcopy(self.figure)

            if self.direction == 'U':
                aux_figure.y += aux_x
            elif self.direction == 'D':
                aux_figure.y -= aux_x
            elif self.direction == 'L':
                aux_figure.x -= aux_x
            elif self.direction == 'R':
                aux_figure.x += aux_x

            aux_figure.resolve(t)

            aux_x += self.distance




