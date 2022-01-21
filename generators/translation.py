import copy

from figures.base import BaseFigure
from generators.base import BaseGenerator

VALID_DIRECTIONS = ['U', 'D', 'L', 'R']

# TODO: Chain generators


class Translation(BaseGenerator):

    # TODO: Add starting point

    def __init__(self, x: int, y: int, figure: BaseFigure, distance: int, direction: str, iterations: int):
        super().__init__()
        self.figure = figure
        if direction not in VALID_DIRECTIONS:
            raise Exception(f'Invalid direction {direction}. Should be one of: {VALID_DIRECTIONS}')
        self.direction = direction
        self.distance = distance
        self.iterations = iterations
        self.x = x
        self.y = y

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
