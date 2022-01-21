import copy

from figures.base import BaseFigure
from generators.base import BaseGenerator
import figures.figure_utils as fu

ONE_TURN = 1


class Rotation(BaseGenerator):

    def __init__(self, x: int, y: int, figure: BaseFigure, angle: int, offset: int = 0, stop_on: int = ONE_TURN):
        super().__init__()
        self.x = x
        self.y = y
        self.figure = figure
        self.angle = angle
        self.stop_on = stop_on
        self.offset = offset

    def draw(self, t):

        if self.stop_on == ONE_TURN:
            aux_angle = self.offset

            while aux_angle < 360 + self.offset:
                c = t.clone()
                aux_figure = copy.deepcopy(self.figure)

                # Transformar coordenadas de la figura en base al ángulo
                x, y = fu.rotate(aux_figure.x, aux_figure.y, aux_angle)

                # Dibujar
                aux_figure.angle = aux_angle
                aux_figure.x = self.x + x
                aux_figure.y = self.y + y
                aux_figure.resolve(c)

                aux_angle += self.angle



