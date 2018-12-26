from life import *
from graphics import *

class GraphicLife(Life):
    """ Class that overrides methods of Life class 
    in order to work on a graphic display """

    def __init__(self, height, width, initial_living):
        super().__init__(height, width, initial_living)
        self.window = GraphWin("game of life", self.width * 20 + 55, self.height * 20 + 55, autoflush = False)
        self.outline = Rectangle(Point(27, 27), Point(self.width * 20 + 33, self.height * 20 + 33))
        self.generation_text = Text(Point(105, 15), 'generation: ' + str(self.generation))
        self.living_text = Text(Point(self.width * 20 - 45, 15), 'live cells: ' + str(len(self.living)))
        self._board_preset()
        self.rectangles = []

    def _board_preset(self):
        self.outline.setOutline('black')
        self.outline.setWidth(5)
        self.outline.draw(self.window)
        self.generation_text.setFace('courier')
        self.generation_text.setStyle('bold')
        self.generation_text.setSize(15)
        self.generation_text.setTextColor('black')
        self.generation_text.draw(self.window)
        self.living_text.setFace('courier')
        self.living_text.setStyle('bold')
        self.living_text.setSize(15)
        self.living_text.setTextColor('black')
        self.living_text.draw(self.window)

    def big_plot(self, x, y):
        big_point = Rectangle(Point(x + 9, y + 9), Point(x - 9, y - 9))
        self.rectangles.append(big_point)
        big_point.setOutline('red4')
        big_point.setFill('red4')
        big_point.draw(self.window)


    def show(self):
        self.living_points = []
        for (y, x) in self.living:
            t = x * 20 + 40
            s = y * 20 + 40
            self.big_plot(t, s)
        self.generation_text.setText('generation: ' + str(self.generation))
        self.living_text.setText('live cells: ' + str(len(self.living)))
        update()

    def unshow(self):
        for rect in self.rectangles:
            rect.undraw()
        self.rectangles = []
        update()
