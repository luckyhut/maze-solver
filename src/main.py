from graphics import Window, Line

def main():
    win = Window(800, 600)
    line = Line(0, 0, 400, 400)
    win.draw_line(line, "red")
    win.wait_for_close()

main()
