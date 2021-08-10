import numpy as np
from path import PathFinder
from itertools import islice


class Movements:
    def __init__(self, node_copy, current_node_array, blank_space):
        self.current_node_array = current_node_array
        self.node = node_copy
        self.blank_space = blank_space

    def move(self, direction):
        if direction == "up":
            self.up()
        if direction == "down":
            self.down()
        if direction == "right":
            self.right()
        if direction == "left":
            self.left()

    # movements
    def right(self):
        self.node[self.blank_space - 1], self.node[self.blank_space] = self.current_node_array[self.blank_space], self.node[
            self.blank_space - 1]
        return "successfully moved"

    def left(self):
        self.node[self.blank_space + 1], self.node[self.blank_space] = self.current_node_array[
            self.blank_space], self.node[
            self.blank_space + 1]
        return "successfully moved"

    def up(self):
        self.node[self.blank_space - 3], self.node[self.blank_space] = self.current_node_array[
            self.blank_space], self.node[
            self.blank_space - 3]
        return "successfully moved"

    def down(self):
        self.node[self.blank_space + 3], self.node[self.blank_space] = self.current_node_array[
            self.blank_space], self.node[
            self.blank_space + 3]
        return "successfully moved"


class Node:
    # initialize the node with the board config
    def __init__(self, s):
        self.child = s
        self.parent = None
        self.gn = 0  # cost
        self.hn = 0  # heuristic
        self.fn = 0  # evaluator

    def get_parent(self):
        return self.parent

    def get_hn(self):
        return self.hn

    def get_gn(self):
        return self.gn

    def get_fn(self):
        return self.gn + self.hn

    def get_current_state(self):
        return self.child

    def update_gn(self, gn):
        self.gn = gn

    def update_hn(self, hn):
        self.hn = hn

    def update_parent(self, parent):
        self.parent = parent

    # exploring the next states
    def expand_node(fringe, explored_nodes, current_node, goal_node, blank_space, g, count, heuristic):
        a = [list(item.get_current_state()) for item in explored_nodes]
        explored_nodes.append(current_node)
        current_node_array = np.asarray(current_node.get_current_state())
        # since the left tile cannot be moved left
        # edge case for moving the left tile
        if blank_space != 0 and blank_space != 3:
            node_copy = current_node_array.copy()
            move = Movements(node_copy, current_node_array, blank_space)
            # move move current right
            move.move("right")
            # node_copy[blank_space - 1], node_copy[blank_space] = current_node_array[blank_space], node_copy[blank_space - 1]
            distance = Distance.calculate(node_copy, goal_node, heuristic)
            count = count + 1

            if not list(node_copy) in a:
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)
                fringe.append(node_copy)

        # since the bottom tile cannot be moved down
        # edge case for moving the bottom tile
        if blank_space != 3 and blank_space != 4 and blank_space != 5:
            node_copy = current_node_array.copy()
            move = Movements(node_copy, current_node_array, blank_space)
            # move current node down
            move.move("down")
            # node_copy[blank_space + 3], node_copy[blank_space] = current_node_array[blank_space], node_copy[
            #     blank_space + 3]
            distance = Distance.calculate(node_copy, goal_node, heuristic)
            count = count + 1
            if not list(node_copy) in a:
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)
                fringe.append(node_copy)

        # since the top tiles cannot be moved up
        # edge case for moving the top tile
        if blank_space != 0 and blank_space != 1 and blank_space != 2:
            node_copy = current_node_array.copy()
            move = Movements(node_copy, current_node_array, blank_space)
            # move current node up
            move.move("up")
            # node_copy[blank_space - 3], node_copy[blank_space] = current_node_array[blank_space], node_copy[
            #     blank_space - 3]
            distance = Distance.calculate(node_copy, goal_node, heuristic)
            count = count + 1
            if not list(node_copy) in a:
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)
                fringe.append(node_copy)

        # since the right tiles cannot be moved right
        # edge case for moving the right tiles
        if blank_space != 2 and blank_space != 5:
            node_copy = current_node_array.copy()
            move = Movements(node_copy, current_node_array, blank_space)
            # move current node left
            # node_copy[blank_space + 1], node_copy[blank_space] = current_node_array[blank_space], node_copy[
            #     blank_space + 1]
            move.move("left")
            distance = Distance.calculate(node_copy, goal_node, heuristic)
            count = count + 1
            if not list(node_copy) in a:
                node_copy = Node(node_copy)
                node_copy.update_gn(g)
                node_copy.update_hn(distance)
                node_copy.update_parent(current_node)
                fringe.append(node_copy)
        return count


class Puzzle:
    def least_fn(fringe):
        fn_fringe = []
        for i in range(len(fringe)):
            fn_fringe.append(fringe[i].get_fn())
        minimum_fn = min(fn_fringe)
        minimum_fn_index = fn_fringe.index(minimum_fn)
        return minimum_fn_index

    def print_state(node):
        print("g(n) = ", node.get_gn(), " h(n) = ",
              node.get_hn(), " f(n) = ", node.get_fn(), "\n")
        print(node.get_current_state()[0], " | ", node.get_current_state()[
              1], " | ", node.get_current_state()[2])
        print("--------------")
        print(node.get_current_state()[3], " | ", node.get_current_state()[
              4], " | ", node.get_current_state()[5])

        # print("--------------")
        # print(node.get_current_state()[6], " | ", node.get_current_state()[7], " | "
        #       , node.get_current_state()[8])
        print("----------------------------------------------------------\n")

    def goal_reached(explored_nodes, count):
        nodes_expanded = len(explored_nodes) - 1
        path = []
        init = explored_nodes[0]
        current = explored_nodes.pop()

        while init != current:
            path.append(current)
            current = current.get_parent()

        path.append(init)
        path.reverse()

        for i in path:
            Puzzle.print_state(i)

        print("Goal Reached \n")
        print("The number of nodes expanded: ", nodes_expanded, "\n")
        print("The number of nodes generated: ", count, "\n")
        print("Path Cost: ", len(path) - 1, "\n")

    def path(explored_nodes):
        explored_nodes.pop()


class Heuristic:
    def __init__(self, arr, goal):
        self.arr = arr
        self.goal = goal

    def manhattan(self, distance):
        distance = sum(abs((val - 1) % 3 - i % 3) + abs((val - 1) // 3 - i // 3)
                       for i, val in enumerate(self.arr) if val)
        return distance

    def missplaced_tiles(self, distance, missplaced_dict=False):
        tiles_dict = {'list': [], 'index': []}
        for i in range(len(self.arr)):
            if self.arr[i] != self.goal[i]:
                distance = distance + 1
                if missplaced_dict:
                    tiles_dict['list'].append(self.arr[i])
                    tiles_dict['index'].append(i)
        if missplaced_dict:
            return tiles_dict
        return distance - 1

    def listToMatrix(self, arr: list, size: int):
        return [arr[x:x+size] for x in range(0, len(arr), size)]

    def findTile(self, element, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == element:
                    return (i, j)
    # find path for given tile
    def findPaths(self, start, end, matrix):
        x, y = start[0], start[1]
        pathfinder = PathFinder(start, end, matrix)
        pathfinder.findPath(x, y)
        paths = pathfinder.paths
        return paths
    # get paths for all missplaced tiles
    def getPaths(self, distance):
        paths = {}
        matrix_start = self.listToMatrix(self.arr, 3)
        matrix_goal = self.listToMatrix(self.goal, 3)

        missplaced_tiles_dict = self.missplaced_tiles(
            distance, missplaced_dict=True)
        for tile in missplaced_tiles_dict['list']:
            index_start = self.findTile(tile, matrix_start)
            index_end = self.findTile(tile, matrix_goal)
            paths[str(tile)] = self.findPaths(
                index_start, index_end, matrix_start)
        return paths

    def new_method(self, distance):
        paths = self.getPaths(distance)
        print("")
        return distance

# Distance Class to Calculate the Manhattan and Misplaced Tiles and new Distance.


class Distance:
    def calculate(arr, goal, heuristic):
        distance = 0

        obj = Heuristic(arr, goal)

        if type == "missplaced" or heuristic == 1:
            distance = obj.missplaced_tiles(distance)
        elif type == "manhattan" or heuristic == 2:
            distance = obj.manhattan(distance)
        elif type == "new" or heuristic == 3:
            distance = obj.new_method(distance)

        # heuristic_calculator = Heuristic(heuristic, arr, goal,self.distance)
        # distance = heuristic_calculator
        return distance
