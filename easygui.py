
import random
import Tkinter as tk
from Tkinter import *
import sys

class Application(tk.Frame):

    def __init__(self, width=21, height=21, size=10):
        tk.Frame.__init__(self)
        self.maze = Maze(width, height)
        self.size = size
        self.steps = 0
        self.grid()
        self.create_widgets()
        self.draw_maze()
        self.create_events()

    def create_widgets(self):
        width = self.maze.width * self.size
        height = self.maze.height * self.size
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.grid()
        self.status = tk.Label(self)
        self.status.grid()

    def draw_maze(self):
        for i, row in enumerate(self.maze.maze):
            for j, col in enumerate(row):
                x0 = j * self.size
                y0 = i * self.size
                x1 = x0 + self.size
                y1 = y0 + self.size
                color = self.get_color(x=j, y=i)
                id = self.canvas.create_rectangle(x0, y0, x1, y1, width=0, fill=color)
                if self.maze.start_cell == (j, i):
                    self.cell = id

        self.canvas.tag_raise(self.cell) # bring to front
        self.status.config(text='game')

    def create_events(self):
        self.canvas.bind_all('<KeyPress-Up>', self.move_cell)
        self.canvas.bind_all('<KeyPress-Down>', self.move_cell)
        self.canvas.bind_all('<KeyPress-Left>', self.move_cell)
        self.canvas.bind_all('<KeyPress-Right>', self.move_cell)

    def move_cell(self, event):
        if event.keysym == 'Up':
            if self.check_move(0, -1):
                self.canvas.move(self.cell, 0, -self.size)
                self.steps += 1
        if event.keysym == 'Down':
            if self.check_move(0, 1):
                self.canvas.move(self.cell, 0, self.size)
                self.steps += 1
        if event.keysym == 'Left':
            if self.check_move(-1, 0):
                self.canvas.move(self.cell, -self.size, 0)
                self.steps += 1
        if event.keysym == 'Right':
            if self.check_move(1, 0):
                self.canvas.move(self.cell, self.size, 0)
                self.steps += 1

        args = (self.steps, self.maze.steps)
        self.status.config(text='Movidas: %d/%d' % args)
        self.check_status()

    def check_move(self, x, y):
        x0, y0 = self.get_cell_coords()
        x1 = x0 + x
        y1 = y0 + y
        return self.maze.maze[y1][x1] == 0

    def get_cell_coords(self):
        position = self.canvas.coords(self.cell)
        x = int(position[0] / self.size)
        y = int(position[1] / self.size)
        return (x, y)

    def check_status(self):
        if self.maze.exit_cell == self.get_cell_coords():
            args = (self.steps, self.maze.steps)
            self.status.config(text='Resuelto en %d/%d movidas!' % args)

    def get_color(self, x, y):
        if self.maze.start_cell == (x, y):
            return 'red'
        if self.maze.exit_cell == (x, y):
            return 'green'
        if self.maze.maze[y][x] == 1:
            return 'black'


class Maze(object): 

    def __init__(self, width=21, height=21, exit_cell=(1, 1)):
        self.width = width
        self.height = height
        self.exit_cell = exit_cell
        self.create()

    def create(self):
        self.maze = [[1] * self.width for _ in range(self.height)] # full of walls
        self.start_cell = None
        self.steps = None
        self.recursion_depth = None
        self._visited_cells = []
        self._visit_cell(self.exit_cell)

    def _visit_cell(self, cell, depth=0):
        x, y = cell
        self.maze[y][x] = 0 # remove wall
        self._visited_cells.append(cell)
        neighbors = self._get_neighbors(cell)
        random.shuffle(neighbors)
        for neighbor in neighbors:
            if not neighbor in self._visited_cells:
                self._remove_wall(cell, neighbor)
                self._visit_cell(neighbor, depth+1)
        self._update_start_cell(cell, depth)

    def _get_neighbors(self, cell):
        """
        Get the cells next to the cell
        Example:
          Given the following mazes
          The a neighbor's are b
          # # # # # # #     # # # # # # #
          # # # b # # #     # a # b # # #
          # # # # # # #     # # # # # # #
          # b # a # b #     # b # # # # #
          # # # # # # #     # # # # # # #
          # # # b # # #     # # # # # # #
          # # # # # # #     # # # # # # #
        """
        x, y = cell
        neighbors = []

        # Left
        if x - 2 > 0:
            neighbors.append((x-2, y))
        # Right
        if x + 2 < self.width:
            neighbors.append((x+2, y))
        # Up
        if y - 2 > 0:
            neighbors.append((x, y-2))
        # Down
        if y + 2 < self.height:
            neighbors.append((x, y+2))

        return neighbors

    def _remove_wall(self, cell, neighbor):
        """
        Remove the wall between two cells
        Example:
          Given the cells a and b
          The wall between them is w
          # # # # #
          # # # # #
          # a w b #
          # # # # #
          # # # # #
        """
        x0, y0 = cell
        x1, y1 = neighbor
        # Vertical
        if x0 == x1:
            x = x0
            y = (y0 + y1) / 2
        # Horizontal
        if y0 == y1:
            x = (x0 + x1) / 2
            y = y0
        self.maze[y][x] = 0 # remove wall

    def _update_start_cell(self, cell, depth):
        if depth > self.recursion_depth:
            self.recursion_depth = depth
            self.start_cell = cell
            self.steps = depth * 2 # wall + cell

    def show(self, verbose=False):
        MAP = {0: ' ', # path
               1: '#', # wall
               2: 'B', # exit
               3: 'A', # start
              }
        x0, y0 = self.exit_cell
        self.maze[y0][x0] = 2
        x1, y1 = self.start_cell
        self.maze[y1][x1] = 3
        for row in self.maze:
            print ' '.join([MAP[col] for col in row])
        if verbose:
            print "Steps from A to B:", self.steps

'''
if __name__ == '__main__':

    from optparse import OptionParser

    parser = OptionParser(description="Random maze game")
    parser.add_option('-W', '--width', type=int, default=21,
                      help="maze width (default 21)")
    parser.add_option('-H', '--height', type=int, default=21,
                      help="maze height (default 21)")
    parser.add_option('-s', '--size', type=int, default=10,
                      help="cell size (default 10)")
    args, _ = parser.parse_args()

    for arg in ('width', 'height'):
        if getattr(args, arg) % 2 == 0:
            setattr(args, arg, getattr(args, arg) + 1)
            print "Warning: %s must be odd, using %d instead" % \
                (arg, getattr(args, arg))
'''
sys.setrecursionlimit(5000)
app = Application(30,30,11)
app.master.title('Maze game') 
app.mainloop()
one=0
root =Tk()
label=Label(root,text='Infinite maze game')
label.pack(fill=X)
button=Button(root,text='easy',command=one+=1)
button.pack()
app = Application(30, 30,11)
app.master.title('Maze game') 
app.mainloop()

root.mainloop()
