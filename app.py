from window import Window
from maze import Maze
from cell import Cell
from shapes import Point

def main() -> None:
    win = Window(800, 600)
    maze = Maze(Point(0, 0), (6, 6), (20, 20), win)
    maze.draw_cells()
    win.wait_for_close()

if __name__ == "__main__":
    main()
    
        
