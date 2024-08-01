from window import Window
from cell import Cell
from shapes import Point

def main() -> None:
    win = Window(800, 600)
    c1 = Cell(Point(30, 10), Point(50, 100), win)
    c2 = Cell(Point(400, 120), Point(440, 160), win)
    c3 = Cell(Point(320, 360), Point(360, 400), win)
    c1.walls.top = False
    c2.walls.bottom = False
    c3.walls.left = False
    c3.walls.right = False
    c1.draw("black")
    c2.draw("black")
    c3.draw("black")
    c1.draw_move(c3)
    c2.draw_move(c1, True)
    win.wait_for_close()

if __name__ == "__main__":
    main()
    
        
