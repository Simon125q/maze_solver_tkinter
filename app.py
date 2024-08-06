from window import Window
from maze import Maze
from cell import Cell
from shapes import Point

def main() -> None:
    win = Window(610, 610)
    maze = Maze(Point(2, 2), (12, 12), (50, 50), win, seed = 69)
    win.wait_for_close()

if __name__ == "__main__":
    main()
    
        
