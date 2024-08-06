from window import Window
from maze import Maze
from cell import Cell
from shapes import Point

def main() -> None:
    win = Window(810, 810)
    maze = Maze(Point(2, 2), (26, 26), (30, 30), win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
    
        
