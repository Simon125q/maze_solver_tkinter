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

    def draw(self, color: str) -> None:
        if self.walls.top:
            top_line = Line(self._p1, Point(self._p2.x, self._p1.y))
            self._win.draw_line(top_line, color)
        if self.walls.right:
            right_line = Line(Point(self._p2.x, self._p1.y), self._p2)
            self._win.draw_line(right_line, color)
        if self.walls.bottom:
            bottom_line = Line(Point(self._p1.x, self._p2.y), self._p2)
            self._win.draw_line(bottom_line, color)
        if self.walls.left:
            left_line = Line(self._p1, Point(self._p1.x, self._p2.y))
            self._win.draw_line(left_line, color)