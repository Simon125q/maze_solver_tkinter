from window import Window
from cell import Cell
from shapes import Point

def main() -> None:
    win = Window(800, 600)
    c1 = Cell(Point(30, 10), Point(50, 100), win)
    c2 = Cell(Point(100, 120), Point(140, 160), win)
    c3 = Cell(Point(320, 360), Point(360, 400), win)
    c3.walls.top = False
    c3.walls.bottom = False
    c3.walls.left = False
    c3.walls.right = False
    c1.draw("black")
    c2.draw("black")
    c3.draw("black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
    
        
