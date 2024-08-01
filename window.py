from tkinter import Tk, BOTH, Canvas
from shapes import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk() 
        self.__root.title("Maze solver")
        self.__root.geometry(f'{width}x{height}')
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(expand=True)
        self.__running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False
