import unittest
from maze import Maze
from shapes import Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        grid_sizes = [(12, 10), (1, 30), (1, 1), (90, 2)]
        for num_rows, num_cols in grid_sizes:
            m1 = Maze(Point(0, 0), (num_rows, num_cols), (10, 10), None)
            self.assertEqual(len(m1._cells), num_rows)
            self.assertEqual(len(m1._cells[0]), num_cols)


if __name__ == "__main__":
    unittest.main()

