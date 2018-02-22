import collections
import heapq as h
import logging


def manhattan(curr, goal, dis=1):
    """Manhattan distance heuristic - tune dis"""
    dx = abs(curr.x - goal.x)
    dy = abs(curr.y - goal.y)
    return dis * (dx + dy)


def gen_path(cell):
    """Create a path for printing and calculate path length"""
    cell.tmp_path = True
    path_length = 0
    while cell.parent:
        cell = cell.parent
        cell.tmp_path = True
        path_length += 1
    return path_length


def bfs(start_cell, exit_cell, cell_list, rows, cols):
    """Breadth First Search - neighbours added in N, E, S, W order.

    Remember we can add the neighbours to the visited collections
    to avoid duplicate cells on the unvisited fifo deque!
    This differentiates it from DFS - it cannot mark them
    as visited!

    We use a deque since it's O(1) for inserting at the head and
    popping - compared to lists O(n)!
    """
    expanded = 0
    unvisited_fifo = collections.deque([start_cell])
    visited_fifo = set()

    while len(unvisited_fifo):
        curr = unvisited_fifo.popleft()
        expanded += 1

        if curr == exit_cell:
            logging.info("BFS path search: Exit found")
            break
        visited_fifo.add(curr)

        for neighbour in curr.path_neighbours():
            if neighbour not in visited_fifo:
                neighbour.parent = curr
                unvisited_fifo.append(neighbour)
                # this looks weird but is an actual optimisation
                # we mark them as 'visited' or 'seen' so we don't
                # expand many duplicate cells!
                # previously this would add all its other neighbours!
                visited_fifo.add(neighbour)

    path_length = gen_path(curr)
    print("BFS path search: Expanded {0} cells".format(expanded))
    print("BFS path search: Path length {0}".format(path_length))


def dfs(start_cell, exit_cell, cell_list, rows, cols):
    """Depth first search - neighbours added in N, E, S, W order.

    Compared to BFS - we cannot add the neighbours to the visited
    set it will no longer be a DFS!
    """
    unvisited_stack = [start_cell]
    visited_stack = set()
    expanded = 0

    while unvisited_stack:
        curr = unvisited_stack.pop()
        expanded += 1
        if curr == exit_cell:
            logging.info("DFS path search: Exit found")
            break

        if curr not in visited_stack:
            visited_stack.add(curr)

            for neighbour in curr.path_neighbours():
                if neighbour not in visited_stack:
                    neighbour.parent = curr
                    unvisited_stack.append(neighbour)

    # create a path for printing
    path_length = gen_path(curr)
    print("DFS path search: Expanded {0} cells".format(expanded))
    print("DFS path search: Path length {0}".format(path_length))


def ucs(start_cell, exit_cell, cell_list, rows, cols):
    """Uniform cost search - Diikjtra's algorithm

    Actually, because of the 4-movement maze,
    UCS will perform like BFS due to path cost == 1
    """
    start_cell.ucs_cost = 0
    expanded = 0

    total_cells = len(cell_list[0])*len(cell_list)
    visited = set()
    unvisited = [(0, start_cell)]

    while len(visited) < total_cells:
        ucs_cost, curr = h.heappop(unvisited)
        expanded += 1

        # break if we have found the exit
        # this will be always the shortest path to exit
        # due to the priority queue and checking only after
        # all neighbours have been pushed!
        if curr == exit_cell:
            logging.info("UCS path search: Exit found")
            break

        # get neighbours and calculate costs
        g_cost = curr.ucs_cost + 1
        for n in curr.path_neighbours():
            if n not in visited:
                # replace the larger of the accumulated path cost
                if n.ucs_cost > g_cost:
                    n.ucs_cost = g_cost
                n.parent = curr
                h.heappush(unvisited, (n.ucs_cost, n))

        # mark as visited
        visited.add(curr)

    # create a path for printing
    path_length = gen_path(curr)
    print("UCS path search: Expanded {0} cells".format(expanded))
    print("UCS path search: Path length {0}".format(path_length))


def gs(start_cell, exit_cell, cell_list, rows, cols):
    """Greedy search using manhattan distance

    Remember, A* deteriorates into Greedy search when g(n) = 0
    i.e. f(n) = h(n)
    """
    start_cell.ucs_cost = 0
    expanded = 0

    total_cells = len(cell_list[0])*len(cell_list)
    visited = set()
    unvisited = [(0, start_cell)]

    while len(visited) < total_cells:
        ucs_cost, curr = h.heappop(unvisited)
        expanded += 1

        # break if we have found the exit
        # this will be always the shortest path to exit
        # due to the priority queue and checking only after
        # all neighbours have been pushed!
        if curr == exit_cell:
            logging.info("Greedy path search: Exit found")
            break

        # get neighbours and calculate costs
        for n in curr.path_neighbours():
            if n not in visited:
                n.parent = curr
                h_cost = manhattan(n, exit_cell)
                h.heappush(unvisited, (h_cost, n))

        # mark as visited
        visited.add(curr)

    # create a path for printing
    path_length = gen_path(curr)
    print("Greedy path search: Expanded {0} cells".format(expanded))
    print("Greedy path search: Path length {0}".format(path_length))


def astar(start_cell, exit_cell, cell_list, rows, cols, tiebreak=False):
    """A* search with Manhattan distance due to maze restriction

    f(n) = g(n) + h(h)

    g(n): path cost
    h(n): heuristic approximation

    Tiebreak is implemented to create bias for current picked path if there are equal paths
    """
    start_cell.ucs_cost = 0
    expanded = 0

    total_cells = len(cell_list[0])*len(cell_list)
    visited = set()
    unvisited = [(0, start_cell)]

    while len(visited) < total_cells:
        astar_cost, curr = h.heappop(unvisited)
        expanded += 1

        # break if we have found the exit
        # this will be always the shortest path to exit
        # due to the priority queue and checking only after
        # all neighbours have been pushed!
        if curr == exit_cell:
            logging.info("A* path search: Exit found")
            break

        # f(n) = g(n) + h(n) == f_cost
        g_cost = curr.ucs_cost + 1
        h_cost = manhattan(curr, exit_cell)
        h_cost *= (1.0 + 1/1000) if tiebreak else h_cost
        f_cost = g_cost + h_cost

        for n in curr.path_neighbours():
            if n not in visited:
                # replace the larger of the accumulated path cost
                if n.ucs_cost > g_cost:
                    n.ucs_cost = g_cost
                n.parent = curr
                # we use the f(n) cost for sorting in the priority queue
                h.heappush(unvisited, (f_cost, n))
        logging.debug([(n[0], n[1].coords) for n in unvisited])

        # mark as visited
        visited.add(curr)

    # create a path for printing
    path_length = gen_path(curr)
    print("A* path search: Expanded {0} cells".format(expanded))
    print("A* path search: Path length {0}".format(path_length))


def binary_search(l, item):
    """Searches the list for item if found"""
    mid = len(l)//2
    first = 0
    last = len(l)-1
    found = False
    index = -1
    while first <= last and not found:
        if item == l[mid]:
            found = True
            index = mid
        elif item < l[mid]:
            last = mid-1
            mid = (first+last)//2
        else:
            first = mid+1
            mid = (first+last)//2
    return found, index
