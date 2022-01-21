from abc import ABC, abstractmethod

from svg_turtle import SvgTurtle


class BaseFigure(ABC):

    def __init__(self):
        self.color = 'black'
        self.x = 0
        self.y = 0

    @abstractmethod
    def draw(self, t: SvgTurtle):
        pass

    def resolve(self, t):
        c = t.clone()

        c.penup()
        c.goto(self.x, self.y)
        c.pendown()

        self.draw(c)
