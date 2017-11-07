import math


class Cell:
    """A cell that is part of a maze keep track of verious state information.

    It consists of the following:
        * 4 walls
        * 4 neighbour cells
        * Coordinates
    Also contains helper functions for maze and path generation.

    Args:
        coords (tuple): The coordinates on the cell.

    """

    def __init__(self, coords):

        # Pointers to other cells or 'edge' cells
        self.north_cell = None
        self.east_cell = None
        self.south_cell = None
        self.west_cell = None

        # Every cell are walled off initially
        self.north_wall = True
        self.east_wall = True
        self.south_wall = True
        self.west_wall = True

        self.neighbours = []
        self.tmp_path = False
        self.parent = None
        self.ucs_cost = math.inf
        self.astar_cost = math.inf

        # store the co-ords as a tuple
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]

    def __lt__(self, other):
        """Compare function for heapq - use coordinates"""
        return self.coords < other.coords

    def add_north(self, neighbour):
        self.north_cell = neighbour

    def add_east(self, neighbour):
        self.east_cell = neighbour

    def add_south(self, neighbour):
        self.south_cell = neighbour

    def add_west(self, neighbour):
        self.west_cell = neighbour

    def wall_neighbours(self):
        """Return a list of neighbour cells that have a wall between the current cell"""
        w = []
        if self.north_wall and self.north_cell:
            w.append(self.north_cell)
        if self.east_wall and self.east_cell:
            w.append(self.east_cell)
        if self.south_wall and self.south_cell:
            w.append(self.south_cell)
        if self.west_wall and self.west_cell:
            w.append(self.west_cell)
        return w

    def path_neighbours(self):
        """Retrieve a list of neighbours which a path/link exists"""
        neighbours = []
        if self.north_cell and not self.north_wall:
            neighbours.append(self.north_cell)
        if self.east_cell and not self.east_wall:
            neighbours.append(self.east_cell)
        if self.south_cell and not self.south_wall:
            neighbours.append(self.south_cell)
        if self.west_cell and not self.west_wall:
            neighbours.append(self.west_cell)
        return neighbours

    def get_neighbours(self):
        """Retrieve a list of neighbours; regardless whether a wall exists"""
        neighbours = []
        if self.north_cell:
            neighbours.append(self.north_cell)
        if self.east_cell:
            neighbours.append(self.east_cell)
        if self.south_cell:
            neighbours.append(self.south_cell)
        if self.west_cell:
            neighbours.append(self.west_cell)
        return neighbours
