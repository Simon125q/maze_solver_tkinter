from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk() 
        self.__root.title("Maze solver")
        self.__root.geometry(f'{width}x{height}')
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(expand=True)
        self.__running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False

def main() -> None:
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()
    
        
