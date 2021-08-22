import numpy as np
from heuristic import Distance
from movements import Movements


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

