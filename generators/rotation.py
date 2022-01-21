import copy

from figures.base import BaseFigure
from generators.base import BaseGenerator

ONE_TURN = 1


class Rotation(BaseGenerator):

    # TODO: WIP. Angle not available in basic forms yet

    def __init__(self, figure: BaseFigure, angle, stop_on: int):
        super().__init__()
        self.figure = figure
        self.angle = angle
        self.stop_on = stop_on

    def draw(self, t):

        if self.stop_on == ONE_TURN:
            aux_angle = 0
            while aux_angle < 360:

                aux_figure = copy.deepcopy(self.figure)
                aux_figure.angle = aux_angle
                aux_figure.resolve(t)

                aux_angle += self.angle

        return self.__figures



