from graphics import Window
from cell import Cell

def main():
    win = Window(1800, 1600)
    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)
    
    c2 = Cell(win)
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)
    
    win.wait_for_close()

main()
