from svg_turtle import SvgTurtle
from figures.base import BaseFigure


class Rectangle(BaseFigure):

    def __init__(self, x: int, y: int, color: str, width: int, height: int, angle: int = 0):
        super().__init__()

        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.angle = angle

    def draw(self, t: SvgTurtle):

        t.color(self.color)
        t.fillcolor(self.color)  # TODO: fix
        t.begin_fill()

        t.setheading(to_angle=self.angle)

        for i, side in enumerate(range(4)):
            if i % 2 == 0:
                size = self.width
            else:
                size = self.height

            t.forward(size)
            t.right(90)

        # fill color
        t.end_fill()
