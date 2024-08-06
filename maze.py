from window import Window
from shapes import Point
from cell import Cell
from time import sleep
import random

class Maze:
    def __init__(self, origin: Point, grid_size: tuple[int, int], cell_size: tuple[int, int],
                 win: Window | None = None, *, seed: int | None = None) -> None:
        self._origin = origin
        self._grid_size = grid_size
        self._cell_size = cell_size
        self._cells: list[list[Cell]] = []
        self._win= win
        if seed != None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self) -> None:
        for row in range(self._grid_size[0]):
            self._cells.append([])
            for col in range(self._grid_size[1]):
                p1 = Point(self._origin.x + col * self._cell_size[0],
                           self._origin.y + row * self._cell_size[1])
                p2 = Point(self._origin.x + (col + 1) * self._cell_size[0],
                           self._origin.y + (row + 1) * self._cell_size[1])
                new_cell = Cell(p1, p2, self._win)
                self._cells[row].append(new_cell)
        if self._win != None:
            self.draw_cells()
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)

    def draw_cells(self) -> None:
        for row in range(self._grid_size[0]):
            for col in range(self._grid_size[1]):
                self._draw_cell(row, col)

    def _draw_cell(self, row_i: int, col_i: int) -> None:
        self._cells[row_i][col_i].draw("black")
        self._animate()

    def _animate(self) -> None:
        if self._win != None:
            self._win.redraw()
        sleep(0.005)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].walls.top = False
        self._draw_cell(0, 0)
        self._cells[self._grid_size[0] - 1][self._grid_size[1] - 1].walls.bottom = False
        self._draw_cell(self._grid_size[0] - 1, self._grid_size[1] - 1)

    def _break_connecting_wall(self, cell1: tuple[int, int], cell2: tuple[int, int]) -> None:
        if cell1 == cell2 or abs(cell1[0] - cell2[0]) > 1 or abs(cell1[1] - cell2[1]) > 1:
            raise Exception("Break connecting walls: Wrong cell coordinates")
        if cell1[0] > cell2[0]:
            self._cells[cell1[0]][cell1[1]].walls.top = False
            self._cells[cell2[0]][cell2[1]].walls.bottom = False
        elif cell1[0] < cell2[0]:
            self._cells[cell1[0]][cell1[1]].walls.bottom = False
            self._cells[cell2[0]][cell2[1]].walls.top = False
        elif cell1[1] < cell2[1]:
            self._cells[cell1[0]][cell1[1]].walls.right = False
            self._cells[cell2[0]][cell2[1]].walls.left = False
        elif cell1[1] > cell2[1]:
            self._cells[cell1[0]][cell1[1]].walls.left = False
            self._cells[cell2[0]][cell2[1]].walls.right = False

    def _get_unvisted_adjacent_cells(self, row, col) -> list[tuple[int, int]]:
        result = []
        if row > 0 and not self._cells[row - 1][col].visited:
            result.append((row - 1, col))
        if row + 1 < self._grid_size[0] and not self._cells[row + 1][col].visited:
            result.append((row + 1, col))
        if col > 0 and not self._cells[row][col - 1].visited:
            result.append((row, col - 1))
        if col + 1 < self._grid_size[1] and not self._cells[row][col + 1].visited:
            result.append((row, col + 1))
        return result

    def _break_walls_r(self, row, col) -> None:
        self._cells[row][col].visited = True
        to_visit = self._get_unvisted_adjacent_cells(row, col)
        while len(to_visit) > 0:
            rand_index = random.randint(0, len(to_visit) - 1)
            visit_row, visit_col = to_visit.pop(rand_index)
            if not self._cells[visit_row][visit_col].visited:
                self._break_connecting_wall((row, col), (visit_row, visit_col))
                self._break_walls_r(visit_row, visit_col)

        self._draw_cell(row, col)
        return





        
