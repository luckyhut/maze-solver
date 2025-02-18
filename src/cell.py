from graphics import Line

class Cell:
    def __init__(self, win=None, wall_left=True, wall_right=True, wall_top=True, wall_bottom=True):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y1 = None
        self.win = win
        self.visited = False

        self.wall_left = wall_left
        self.wall_right = wall_right
        self.wall_top = wall_top
        self.wall_bottom = wall_bottom

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        line_left = Line(x1, y1, x1, y2)
        line_right = Line(x2, y1, x2, y2)
        line_top = Line(x1, y1, x2, y1)    
        line_bottom = Line(x1, y2, x2, y2)
        
        if self.wall_left:
            self.win.draw_line(line_left, "black")
        else:
            self.win.draw_line(line_left, "white")
        if self.wall_right:
            self.win.draw_line(line_right, "black")
        else:
            self.win.draw_line(line_right, "white")
        if self.wall_top:
            self.win.draw_line(line_top, "black")
        else:
            self.win.draw_line(line_top, "white")
        if self.wall_bottom:
            self.win.draw_line(line_bottom, "black")
        else:
            self.win.draw_line(line_bottom, "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        # starting point
        from_midpoint_x = abs(self._x1 + self._x2) // 2
        from_midpoint_y = abs(self._y1 + self._y2) // 2

        # ending point
        to_midpoint_x = abs(to_cell._x1 + to_cell._x2) // 2
        to_midpoint_y = abs(to_cell._y1 + to_cell._y2) // 2

        line = Line(from_midpoint_x, from_midpoint_y, to_midpoint_x, to_midpoint_y)
        line.draw(self.win.canvas, color)
