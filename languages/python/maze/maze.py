#!/usr/bin/env python3

import random
import searches
import collections
from cell import Cell
import logging
import argparse


description = """
              Maze generation with some different path search algorithms.
              If no options are specified, it will default to PRIM's with A* search.
              There are many options that you can configure, read carefully.
              """


class Maze:
    """This maze can be generated with a DFS or PRIMs algorithm.

    Args:
        rows (int):           The number of rows for the maze.
        cols (int):           The number of columns for the maze.
        start_coords (tuple): The coordinates of the start cell.
        exit_coords (tuple):  The coordinates of the exit cell.

    """

    def __init__(self, rows, cols, start_coords, exit_coords):
        def add_neighbour(curr, cell, dir):
            if dir == 'east':
                curr.add_east(cell)
                cell.add_west(curr)
            elif dir == 'south':
                curr.add_south(cell)
                cell.add_north(curr)

        # keep a 2D grid of the maze
        self.cell_list = []
        self.rows = rows
        self.cols = cols

        # rows loop
        for r in range(self.rows):
            row_list = []
            # cols loop
            for c in range(self.cols):
                new_cell = Cell((r, c))
                # NW corner
                if c == 0 and r == 0:
                    logging.debug('NW corner')
                # NE corner
                elif c == self.cols-1 and r == 0:
                    logging.debug('NE corner')
                    left_cell = row_list[c-1]
                    add_neighbour(left_cell, new_cell, 'east')
                # SW corner
                elif c == 0 and r == self.rows-1:
                    logging.debug('SW corner')
                    top_cell = self.cell_list[r-1][c]
                    add_neighbour(top_cell, new_cell, 'south')
                elif r == 0:
                    logging.debug("First row: {0}".format(c))
                    left_cell = row_list[c-1]
                    add_neighbour(left_cell, new_cell, 'east')
                # middle rows - first col
                elif r < self.rows-1 and c == 0:
                    logging.debug("Col 0: {0}".format(r))
                    top_cell = self.cell_list[r-1][c]
                    add_neighbour(top_cell, new_cell, 'south')
                # the rest of the rows
                else:
                    top_cell = self.cell_list[r-1][c]
                    top_cell.add_south(new_cell)
                    left_cell = row_list[c-1]
                    left_cell.add_east(new_cell)
                    new_cell.add_west(left_cell)
                    new_cell.add_north(top_cell)
                    if c == self.cols-1 and r == self.rows-1:
                        logging.debug('SE corner')
                    else:
                        logging.debug("(Row,Col): ({0}, {1})".format(r, c))

                row_list.append(new_cell)
            self.cell_list.append(row_list)

        # start and exit cells
        self.start_cell = self.cell_list[start_coords[0]][start_coords[1]]
        self.start_coords = start_coords
        self.exit_cell = self.cell_list[exit_coords[0]][exit_coords[1]]
        self.exit_coords = exit_coords

        # break walls for start and exit cells
        for coords, cell in zip([start_coords, exit_coords], [self.start_cell, self.exit_cell]):
            # check columns
            if coords[1] == 0:
                cell.west_wall = False
            elif coords[1] == self.cols-1:
                cell.east_wall = False
            # check rows
            elif coords[0] == 0:
                cell.north_wall = False
            elif coords[0] == self.rows-1:
                cell.south_wall = False

    def reset_visited(self):
        """Reset the path cell for printing"""
        for r in range(self.rows):
            for c in range(self.cols):
                self.cell_list[r][c].tmp_path = False

    def print_graph(self):
        """Printing maze with just coordinates - early debugging"""
        for r in range(self.rows):
            for c in range(self.cols):
                print(" {0} ".format(self.cell_list[r][c].coords), end='')
            print('')

    def print_maze(self):
        """A Cell is represented in 'three' rows:

        +--+ First row
        |  | Middle row
        +--+ Last row

        When printing the maze however, we only print the first row and the middle.
        This is to negate 'overlapping' walls between cells.
        """
        corner = "+"
        h_wall = "--"
        v_wall = "|"
        empty = "  "
        no_wall = " "

        long_filled = u"\u2588"
        # long_filled = "\u25ae"  # something wrong with my linux printing utf

        square_filled = u"\u25a0"
        square_filled = u"\u25a0"
        square_two = square_filled + square_filled
        square_one = square_filled

        long_one = long_filled
        long_two = long_one + long_one
        square_two = long_two
        square_one = long_one

        def print_first_cell_row(cell):

            # NW corner of cell
            print(corner, end='')
            if cell.north_wall:
                print(h_wall, end='')
            # link between north and current cell
            elif cell.north_cell and cell.north_cell.tmp_path and cell.tmp_path:
                print(long_two, end='')
            elif cell == self.start_cell and self.start_coords[0] == 0:
                print(square_two, end='')
            elif cell == self.exit_cell and self.exit_coords[0] == 0:
                print(square_two, end='')
            else:
                print(empty, end='')
            # NE corner of a cell
            if c == self.cols-1:
                print(corner, end='')

        def print_second_cell_row(cell):

            if cell.west_wall:
                print(v_wall, end='')
            # start cell is special
            elif cell == self.start_cell and self.start_coords[1] == 0:
                print(long_one, end='')
            elif cell == self.exit_cell and self.exit_coords[1] == 0:
                print(long_one, end='')

            # link between cells
            elif cell.west_cell and cell.west_cell.tmp_path and cell.tmp_path:
                print(square_one, end='')
            else:
                print(no_wall, end='')

            # path cell
            if cell.tmp_path:
                print(square_two, end='')
            else:
                print(empty, end='')

            # print east edge manually
            if c == self.cols-1:
                if cell.east_wall:
                    print(v_wall, end='')
                elif cell == self.exit_cell:
                    print(long_one + ' Exit', end='')
                elif cell == self.start_cell:
                    print(long_one + ' Start', end='')
                else:
                    print(no_wall, end='')

        for r in range(self.rows):
            # only print the first 'two' rows of a cell
            for cell_row in range(1, 3):
                for c in range(self.cols):
                    cell = self.cell_list[r][c]
                    # first 'row' of a cell
                    if cell_row == 1:
                        print_first_cell_row(cell)
                    # middle row
                    elif cell_row == 2:
                        print_second_cell_row(cell)
                print('')

        # print the south edge manually
        for c in range(self.cols):
            cell = self.cell_list[self.rows-1][c]
            print(corner, end='')
            if cell.south_wall:
                print(h_wall, end='')
            elif cell == self.start_cell or cell == self.exit_cell:
                print(square_two, end='')
            else:
                print(no_wall, end='')
            if c == self.cols-1:
                print(corner, end='')
        print('')

    def break_wall(self, c_cell, n_cell):
        """Breaks the wall between two cells"""
        if c_cell.north_cell == n_cell:
            c_cell.north_wall = False
            n_cell.south_wall = False
        elif c_cell.east_cell == n_cell:
            c_cell.east_wall = False
            n_cell.west_wall = False
        elif c_cell.south_cell == n_cell:
            c_cell.south_wall = False
            n_cell.north_wall = False
        elif c_cell.west_cell == n_cell:
            c_cell.west_wall = False
            n_cell.east_wall = False

    def gen_dfs_maze(self):
        """Generate maze based on the simple DFS algorithm with backtracking"""
        print("\n{0}\nGenerate DFS maze\n{1}".format(100*"-", 100*"-"))

        unvisited_stack = [self.start_cell]
        visited_stack = []

        while unvisited_stack:
            curr = unvisited_stack.pop()

            # mark it as visited
            visited_stack.append(curr)
            neighbours = [n for n in curr.get_neighbours() if n not in visited_stack]

            # if the current cell has neighbours(s), we add it back to the stack
            # this allows backtracking in case the cell has multiple neighbours
            if neighbours:
                cell = neighbours.pop(random.randint(0, len(neighbours)-1))
                self.break_wall(curr, cell)
                unvisited_stack.append(curr)
                unvisited_stack.append(cell)

    def gen_mod_prim_maze(self):
        """Generate maze based on the modified PRIMs algorithm.

        Maze are cells that are 'visited' and part of the final maze.
        Frontier are cells that are yet to have walls broken.
        """
        print("\n{0}\nGenerate modified PRIM maze\n{1}".format(100*"-", 100*"-"))

        maze = [self.start_cell]
        frontier = []

        # add neighbours to the frontier
        frontier += self.start_cell.get_neighbours()

        while frontier:
            # pick on from the frontier at random
            f = frontier.pop(random.randint(0, len(frontier)-1))

            # break the wall between a frontier cell and maze cell
            # if multiple exist - pick one at random
            neighbours = [n for n in f.get_neighbours() if n in maze]
            random.shuffle(neighbours)
            if neighbours:
                self.break_wall(neighbours[0], f)

            # mark the frontier cell to be a maze cell
            maze.append(f)

            # add the neighbours of that cell to the frontier
            for n in f.get_neighbours():
                if n not in frontier and n not in maze:
                    frontier.append(n)

    def remove_deadends_bfs(self, level=6):
        """Remove deadends (cells that have 3 walls) via a BFS path search.

        This should be the same as BFS now that once I find the exit node - don't break
        Level is used to set the aggression level of removing deadends
        """
        unvisited_fifo = collections.deque([self.start_cell])
        visited_fifo = set()
        broken = 1  # number of skipped deadends

        while len(unvisited_fifo):
            curr = unvisited_fifo.popleft()
            if curr == self.exit_cell:
                logging.debug("Removing deadends BFS: Exit found")

            # check if there are > 2 walls for a cell
            wall_list = curr.wall_neighbours()
            if len(wall_list) > 2:
                if broken % level == 0:
                    self.break_wall(curr, wall_list[0])
                    broken = 1
                else:
                    broken += 1
            # mark cell as visited and add neighbours to the fifo
            visited_fifo.add(curr)
            unvisited_fifo += [n for n in curr.path_neighbours() if n not in visited_fifo]

    def remove_deadends_dfs(self, level=6):
        """Remove deadends (cells that have 3 walls) via a DFS path search.

        This should be the same as BFS now that once I find the exit node - don't break
        Level is used to set the aggression level of removing deadends
        """
        unvisited_stack = [self.start_cell]
        visited_stack = set()
        broken = 1  # number of skipped deadends

        while unvisited_stack:
            curr = unvisited_stack.pop()
            if curr == self.exit_cell:
                logging.debug("Removing deadends DFS: Exit found")

            if curr not in visited_stack:
                wall_list = curr.wall_neighbours()
                if len(wall_list) > 2:
                    if broken % level == 0:
                        self.break_wall(curr, wall_list[0])
                        broken = 1
                    else:
                        broken += 1
                # mark cell as visited and add neighbours to stack
                visited_stack.add(curr)
                unvisited_stack += [n for n in curr.path_neighbours() if n not in visited_stack]


def set_start_exit(start_cell, exit_cell, maze_rows, maze_cols):
    """Start and exit cells are lists - move coordinates to west or east side of maze"""
    for cell in [start_cell, exit_cell]:
        # check row
        if cell[0] > maze_rows:
            cell[0] -= (cell[0] - maze_rows) + 1
        elif cell[0] == maze_rows:
            cell[0] -= 1
        # check col
        if cell[1] > maze_cols:
            cell[1] -= (cell[1] - maze_cols) + 1
        elif cell[1] == maze_cols:
            cell[1] -= 1
        if cell[0] != maze_rows-1 or cell[1] != maze_cols-1:
            if cell[1] != maze_cols-1 and cell[1] > maze_cols//2:
                cell[1] = maze_cols-1
            elif cell[1] != maze_cols-1 and cell[1] < maze_cols//2:
                cell[1] = 0
            # adjust row as last resort
            elif cell[0] != maze_rows-1 and cell[0] > maze_rows//2:
                cell[0] = maze_rows-1
            elif cell[0] != maze_rows-1 and cell[0] < maze_rows//2:
                cell[0] = 0
    logging.debug("new start: {0}".format(start_cell))
    logging.debug("new exit: {0}".format(exit_cell))
    return start_cell, exit_cell


def Main():
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-d", "--dimension",
                        nargs=2,
                        type=int,
                        default=[10, 30],
                        help="Maze dimension")
    parser.add_argument("--start-cell",
                        nargs=2,
                        type=int,
                        default=[0, 0],
                        help="Start cell - must be less than maze dimension")
    parser.add_argument("--exit-cell",
                        nargs=2,
                        type=int,
                        default=[29, 29],
                        help="Exit cell - must be less than maze dimension")
    parser.add_argument("-m", "--maze-type",
                        choices=['dfs', 'prim'],
                        default='prim',
                        help="Maze generation algorithms: depth-first, PRIM's")
    parser.add_argument("-s", "--search-type",
                        nargs='*',
                        choices=['dfs', 'bfs', 'ucs', 'a*', 'gs'],
                        default=['a*', 'dfs'],
                        help="Path search algorithms: depth-first, breadth-first, uniform-cost, A*")
    parser.add_argument("-b", "--break-type",
                        choices=['dfs', 'bfs'],
                        default='bfs',
                        help="Breaking deadends for imperfect maze: depth-first, breadth-first")
    parser.add_argument("-v", "--verbose",
                        choices=['warning', 'info', 'debug'],
                        default='warning',
                        help="Print debugging - warning, info, debug")
    args = parser.parse_args()

    # set logging level
    if args.verbose == 'warning':
        logging_level = logging.WARNING
    elif args.verbose == 'info':
        logging_level = logging.INFO
    else:
        logging_level = logging.DEBUG
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=logging_level)

    rows = args.dimension[0]
    cols = args.dimension[1]

    # check start and exit coords
    logging.debug("old start: {0}".format(args.start_cell))
    logging.debug("old exit: {0}".format(args.exit_cell))
    start_cell, exit_cell = set_start_exit(args.start_cell, args.exit_cell, rows, cols)

    # generate specified maze
    maze = Maze(rows, cols, start_cell, exit_cell)
    maze.gen_mod_prim_maze() if args.maze_type == "prim" else maze.gen_dfs_maze()

    # create an imperfect path by removing deadends - can tune with level
    maze.remove_deadends_bfs() if args.break_type == "bfs" else maze.remove_deadends_dfs()

    # create a dictionary for the path searches
    path_searches = {'dfs': searches.dfs,
                     'bfs': searches.bfs,
                     'ucs': searches.ucs,
                     'a*': searches.astar,
                     'gs': searches.gs}

    for s in args.search_type:
        path_searches[s](maze.start_cell,
                         maze.exit_cell,
                         maze.cell_list,
                         maze.rows,
                         maze.cols)
        maze.print_maze()
        maze.reset_visited()


if __name__ == "__main__":
    Main()
