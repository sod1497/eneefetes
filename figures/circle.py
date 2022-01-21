from svg_turtle import SvgTurtle
from figures.base import BaseFigure


class Circle(BaseFigure):

    def __init__(self, x: int, y: int, r: int, color: str):
        super().__init__()

        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def draw(self, t: SvgTurtle):
        t.color(self.color)
        t.dot(self.r)
