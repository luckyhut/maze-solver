from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            cols = []
            for j in range(self.num_rows):
                cols.append(Cell(self.win))
            self._cells.append(cols)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        top_left_x = self.x1 + (i * self.cell_size_x)
        top_left_y = self.y1 + (j * self.cell_size_y)
        bottom_right_x = top_left_x + self.cell_size_x
        bottom_right_y = top_left_y + self.cell_size_y
        self._cells[i][j].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].wall_top = False
        self._cells[self.num_cols-1][self.num_rows-1].wall_bottom = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))
                
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            rand = random.randrange(len(to_visit))
            visit_next = to_visit[rand]
            if visit_next[0] == i - 1:
                self._cells[i][j].wall_left = False
                self._cells[i-1][j].wall_right = False
            if visit_next[0] == i + 1:
                self._cells[i][j].wall_right = False
                self._cells[i+1][j].wall_left = False
            if visit_next[1] == j + 1:
                self._cells[i][j].wall_bottom = False
                self._cells[i][j+1].wall_top = False
            if visit_next[1] == j - 1:
                self._cells[i][j].wall_top = False
                self._cells[i][j-1].wall_bottom = False

            self._break_walls_r(visit_next[0], visit_next[1])

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[j][i].visited =False
