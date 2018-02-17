#!/bin/python3


def timeConversion(s):
    print('\nConverting {0} to 24hr format'.format(s))
    time_split = s.split(':')
    hour = int(time_split[0])
    minute = int(time_split[1])
    seconds = int(time_split[2][:2])  # strip AM/PM

    # check if we need to add 12 hours
    add_hours = True if time_split[2][2:] == 'PM' else False
    if add_hours and hour < 12:
        hour += 12
    else:
        hour %= 12
    return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, seconds)


def dfs_possible_roads(city):
    """Basically just traverse through the group of cities.

    This is to see what other cities are connected to it
    instead of keeping track of the city groups.

    There are better ways for sure...
    """
    visited_stack = []
    unvisited_stack = set()
    roads_joined = 0

    unvisited_stack.add(city)
    while unvisited_stack:
        curr = unvisited_stack.pop()
        curr.group = True

        # find damaged roads
        nbs = curr.get_possible_roads()
        for n in nbs:
            # add neighbouring cities to the 'group'
            n.group = True
            if n not in visited_stack:
                unvisited_stack.add(n)
        # redundant
        if len(visited_stack) >= 1:
            roads_joined += 1
        visited_stack.append(curr)
    return roads_joined, len(visited_stack)


class City:
    def __init__(self, number):
        self.neighbours = set()  # for easy dup handling
        self.group = False

    # possible roads == damaged roads
    def add_possible_road(self, neighbour):
        self.neighbours.add(neighbour)

    def get_possible_roads(self):
        return self.neighbours


def roadsAndLibraries(n, c_lib, c_road, cities):
    city_dict = {}
    cost = 0

    # early exit for easy case
    if c_lib < c_road:
        return c_lib*n

    for path in cities:
        # always only two cities
        n1 = path[0]
        n2 = path[1]
        # remember new instances are not the same!
        if n1 not in city_dict:
            c1 = City(n1)
            city_dict[n1] = c1
        else:
            c1 = city_dict[n1]
        if n2 not in city_dict:
            c2 = City(n2)
            city_dict[n2] = c2
        else:
            c2 = city_dict[n2]
        # add neighbours to city
        c1.add_possible_road(c2)
        c2.add_possible_road(c1)

    num_road_cities = len(city_dict)  # cities with damaged roads
    num_no_road_cities = n-num_road_cities  # cities that are isolated!

    for c, ob in city_dict.items():
        # check if the group of cities hasn't been checked
        if ob.group is False:
            # set flag for checking this group of cities
            # REMEMBER: if a repairing roads for a group
            # of cities - add a single library!
            roads, num_visited = dfs_possible_roads(ob)
            roads_cost = (roads*c_road) + c_lib
            libs_cost = num_visited*c_lib
            assert(roads == num_visited-1)

            if roads_cost < libs_cost:
                cost += roads_cost
            else:
                cost += libs_cost
    # account for cities without roads!
    return cost + num_no_road_cities*c_lib


def main():
    with open('output.txt', 'r') as f:
        answers = [int(line) for line in f]

    with open('input.txt', 'r') as f:
        q = int(f.readline())
        for i in range(q):
            # IMPORTANT - not all cities have roads!
            # n = num cities
            # m = num roads
            n, m, c_lib, c_road = [int(x) for x in f.readline().strip().split(' ')]
            city_list = []
            for r in range(m):
                cities = [int(c) for c in f.readline().strip().split(' ')]
                city_list.append(cities)
            results = roadsAndLibraries(n, c_lib, c_road, city_list)
            print(results)
            assert(results == answers[i])


if __name__ == "__main__":
    main()

    print(timeConversion('12:45:54PM'))
