from svg_turtle import SvgTurtle
import figures as f


class Canvas:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__t = SvgTurtle(width, height)
        self.__t.hideturtle()
        self.__actions = []

    @classmethod
    def new_canvas(cls, width: int = 80, height: int = 80):
        return Canvas(width, height)

    def add_background(self, color):
        self.__actions.append(f.Rectangle(
            x=-int(self.width/2),
            y=int(self.height/2),
            width=self.width,
            height=self.height,
            color=color
        ))

    def add_figure(self, figure):
        self.__actions.append(figure)

    def add_particles(self):
        pass

    def save(self, filename):

        for action in self.__actions:
            action.resolve(self.__t)

        self.__t.save_as(filename)

    def __str__(self):
        return f'Canvas components: {[x.__name__ for x in self.__actions]}'

