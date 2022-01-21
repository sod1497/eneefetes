from svg_turtle import SvgTurtle
from figures.base import BaseFigure


class Rectangle(BaseFigure):

    # TODO: Add rotation

    def __init__(self, x: int, y: int, color: str, width: int, height: int):
        super().__init__()

        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    def draw(self, t: SvgTurtle):

        t.color(self.color)
        t.fillcolor(self.color)
        t.begin_fill()

        for i, side in enumerate(range(4)):
            if i % 2 == 0:
                size = self.width
            else:
                size = self.height

            t.forward(size)
            t.right(90)

        # fill color
        t.end_fill()
