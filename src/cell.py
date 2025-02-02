from graphics import Line

class Cell:
    def __init__(self, win, wall_left=True, wall_right=True, wall_top=True, wall_bottom=True):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y1 = None
        self.win = win

        self.wall_left = wall_left
        self.wall_right = wall_right
        self.wall_top = wall_top
        self.wall_bottom = wall_bottom

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.wall_left:
            line = Line(x1, y1, x1, y2)
            line.draw(self.win.canvas, "black")
        if self.wall_right:
            line = Line(x2, y1, x2, y2)
            line.draw(self.win.canvas, "red")
        if self.wall_top:
            line = Line(x1, y1, x2, y1)
            line.draw(self.win.canvas, "green")
        if self.wall_bottom:
            line = Line(x1, y2, x2, y2)
            line.draw(self.win.canvas, "blue")

            
