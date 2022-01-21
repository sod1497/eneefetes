from paintor.canvas import Canvas
import figures as f
import generators as g


if __name__ == '__main__':
    canvas = Canvas.new_canvas()

    canvas.add_background('white')
    canvas.add_figure(f.Circle(40, 40, 60, 'red'))
    canvas.add_figure(f.Rectangle(0, 0, 'blue', 20, 30))
    canvas.add_figure(g.Translation(f.Rectangle(0, 0, 'yellow', 3, 3), 5, 'D', 5))

    canvas.save('result.svg')
