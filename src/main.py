from graphics import Window
from cell import Cell

def main():
    win = Window(1800, 1600)
    cell_1 = Cell(win)
    cell_1.draw(25, 25, 50, 50)
    cell_2 = Cell(win, False, False, False)
    cell_2.draw(80, 80, 120, 120)
    cell_3 = Cell(win, False, False)
    cell_3.draw(270, 270, 300, 300)
    win.wait_for_close()

main()
