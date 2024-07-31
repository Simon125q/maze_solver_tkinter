from dataclasses import dataclass
from tkinter import Canvas

@dataclass
class Point:
    x: int = 0
    y: int = 0

class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y,
            fill=fill_color,
            width=2
        )


