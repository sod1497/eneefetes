from svg_turtle import SvgTurtle
from figures.base import BaseFigure
from figures.figure_utils import distance_between_points, angle_line_x, rotate


class Line(BaseFigure):

    def __init__(self, x1: int, y1: int, x2: int, y2: int, color: str, width: int = 1, angle: int = 0):
        super().__init__()

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.angle = angle
        self.color = color
        self.width = width

    def draw(self, t: SvgTurtle):
        t.color(self.color)
        t.pensize(self.width)

        self.x1, self.y1 = rotate(self.x1, self.y1, self.angle)
        self.x2, self.y2 = rotate(self.x2, self.y2, self.angle)

        line_len = distance_between_points(self.x1, self.y1, self.x2, self.y2)
        line_angle = angle_line_x(self.x1, self.y1, self.x2, self.y2)
        t.setheading(to_angle=line_angle)

        t.penup()
        t.goto(self.x + self.x1, self.y + self.y1)
        t.pendown()

        t.forward(line_len)

