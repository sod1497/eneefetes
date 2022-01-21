from typing import Tuple

from svg_turtle import SvgTurtle
from figures.base import BaseFigure
import figures.figure_utils as fu

class Custom(BaseFigure):

    def __init__(self, x: int, y: int, points: [Tuple[int, int]], color: str, angle: int = 0):
        super().__init__()

        self.x = x
        self.y = y
        self.color = color
        self.points = points
        if len(points) == 0:
            raise Exception('A Custom figure needs at least one point')
        self.angle = angle

    def draw(self, t: SvgTurtle):

        t.color(self.color)
        # t.fillcolor(self.color)  # TODO: fix
        # t.begin_fill()

        xaux, yaux = self.points[0]

        t.penup()
        t.goto(self.x + xaux, self.y + yaux)
        t.pendown()

        for i in range(len(self.points)):
            current_point = self.points[i]
            next_point = self.points[(i + 1) % len(self.points)]

            side_len = fu.distance_between_points(current_point[0], current_point[1], next_point[0], next_point[1])
            side_angle = fu.angle_line_x(current_point[0], current_point[1], next_point[0], next_point[1])

            t.setheading(to_angle=self.angle + side_angle)
            t.forward(side_len)

        # fill color
        t.end_fill()
