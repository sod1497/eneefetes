from generators.rotation import ONE_TURN
from paintor.canvas import Canvas
import figures as f
import generators as g


def test_1():
    canvas = Canvas.new_canvas()

    canvas.add_background('white')
    canvas.add_figure(f.Circle(40, 40, 60, 'red'))
    canvas.add_figure(f.Rectangle(0, 0, 'blue', 20, 30))
    canvas.add_figure(g.Translation(0, 0, f.Rectangle(0, 0, 'yellow', 3, 3), 5, 'D', 5))
    canvas.add_figure(g.Rotation(-5, 5, f.Rectangle(15, 5, 'green', 2, 2), 15, ONE_TURN))

    canvas.save('result.svg')


def test_2():
    canvas = Canvas.new_canvas()

    canvas.add_background('white')
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Circle(25, 0, 10, 'blue'), angle=15, offset=0))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Circle(20, 0, 6, 'black'), angle=15, offset=10))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Circle(15, 0, 3, 'red'), angle=15, offset=20))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Circle(10, 0, 2, 'green'), angle=15, offset=30))

    canvas.save('result.svg')


def test_3():
    canvas = Canvas.new_canvas()

    canvas.add_background('white')
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(20, 20, 80, 70, 'black', 1), angle=30, offset=-18))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(20, 20, 80, 75, 'black', 1), angle=30, offset=-10))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(10, 10, 50, 45, 'blue', 1), angle=30, offset=0))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(8, 8, 30, 25, 'red', 2), angle=30, offset=10))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(8, 8, 30, 25, 'white', 1), angle=30, offset=10))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(6, 6, 20, 15, 'black', 3), angle=30, offset=25))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(6, 6, 20, 15, 'white', 2), angle=30, offset=25))
    canvas.save('result.svg')


def test_4():
    canvas = Canvas.new_canvas()

    canvas.add_background('black')
    canvas.add_figure(f.Circle(0, 0, 40, 'white'))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Circle(27, 0, 10, 'blue'), angle=15, offset=0))
    canvas.add_figure(g.Rotation(x=0, y=0, figure=f.Line(22, 32, 32, 22, 'red', 2), angle=30, offset=15))
    canvas.add_figure(g.Rotation(0, 0, f.Rectangle(20, 20, 'black', 10, 10), 45, ONE_TURN))
    canvas.add_figure(g.Rotation(0, 0, f.Rectangle(21, 21, 'white', 8, 8), 45, ONE_TURN))
    canvas.add_figure(g.Rotation(0, 0, f.Rectangle(15, 5, 'blue', 2, 2), 15, ONE_TURN))
    canvas.add_figure(g.Rotation(0, 0, f.Rectangle(10, 5, 'red', 2, 2), 24, ONE_TURN))
    canvas.add_figure(g.Rotation(0, 0, f.Rectangle(4, 5, 'black', 2, 2), 45, ONE_TURN))
    canvas.save('result.svg')


if __name__ == '__main__':
    test_4()
