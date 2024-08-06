from dataclasses import dataclass
from shapes import Point, Line
from window import Window

@dataclass
class Walls:
    left: bool
    right: bool
    top: bool
    bottom: bool

class Cell:
    def __init__(self, p1: Point, p2: Point, win: Window) -> None:
        self._p1 = p1
        self._p2 = p2
        self._win = win
        self.walls = Walls(True, True, True, True) 
        self.visited = False

    def __repr__(self) -> str:
        return f"Cell at p1: {self._p1}, p2: {self._p2} with walls: {self.walls}"

    def draw(self, color: str) -> None:
        top_line = Line(self._p1, Point(self._p2.x, self._p1.y))
        right_line = Line(Point(self._p2.x, self._p1.y), self._p2)
        bottom_line = Line(Point(self._p1.x, self._p2.y), self._p2)
        left_line = Line(self._p1, Point(self._p1.x, self._p2.y))
        if self.walls.top:
            self._win.draw_line(top_line, color)
        else:
            self._win.draw_line(top_line, "#d9d9d9")
        if self.walls.right:
            self._win.draw_line(right_line, color)
        else:
            self._win.draw_line(right_line, "#d9d9d9")
        if self.walls.bottom:
            self._win.draw_line(bottom_line, color)
        else:
            self._win.draw_line(bottom_line, "#d9d9d9")
        if self.walls.left:
            self._win.draw_line(left_line, color)
        else:
            self._win.draw_line(left_line, "#d9d9d9")

    def draw_move(self, to_cell: 'Cell', undo: bool = False) -> None:
        p1x = self._p1.x + ((self._p2.x - self._p1.x) // 2)
        p1y = self._p1.y + ((self._p2.y - self._p1.y) // 2)
        p1 = Point(p1x, p1y)
        p2x = to_cell._p1.x + ((to_cell._p2.x - to_cell._p1.x) // 2)
        p2y = to_cell._p1.y + ((to_cell._p2.y - to_cell._p1.y) // 2)
        p2 = Point(p2x, p2y)
        connecting = Line(p1, p2)
        if not undo:
            self._win.draw_line(connecting, "red")
        else:
            self._win.draw_line(connecting, "gray")

