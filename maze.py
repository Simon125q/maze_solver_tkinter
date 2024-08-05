from window import Window
from shapes import Point
from cell import Cell
from time import sleep

class Maze:
    def __init__(self, origin: Point, grid_size: tuple[int, int],
                 cell_size: tuple[int, int], win: Window) -> None:
        self._origin = origin
        self._grid_size = grid_size
        self._cell_size = cell_size
        self._win= win
        self._cells: list[list[Cell]] = []
        self._create_cells()

    def _create_cells(self) -> None:
        for row in range(self._grid_size[0]):
            self._cells.append([])
            for col in range(self._grid_size[1]):
                p1 = Point(self._origin.x + row * self._cell_size[0],
                           self._origin.y + col * self._cell_size[1])
                p2 = Point(self._origin.x + (row + 1) * self._cell_size[0],
                           self._origin.y + (col + 1) * self._cell_size[1])
                new_cell = Cell(p1, p2, self._win)
                self._cells[row].append(new_cell)
        self.draw_cells()

    def draw_cells(self) -> None:
        print("here")
        print(self._cells)
        for row in range(self._grid_size[0]):
            for col in range(self._grid_size[1]):
                self._draw_cell(row, col)

    def _draw_cell(self, row_i: int, col_i: int) -> None:
        self._cells[row_i][col_i].draw("black")
        self._animate()

    def _animate(self) -> None:
        self._win.redraw()
        sleep(0.005)
        
