import numpy as np
import os
from node import Distance
from node import Node
from node import Puzzle

os.system('cls')

heuristic = input("Choose a Heuristic: \n 1. Misplaced Tiles \n 2. Manhattan Distance \n 3. new method \n Enter : ")
heuristic = int(heuristic)

"""
1 3 4
2 0 5
-----
1 2 3
4 5 0
"""

initial_state = [1, 3, 4, 2, 0, 5]
final_state = [1, 2, 3, 4, 5, 0]

initial_state = Node(initial_state) 
final_state = Node(final_state)
explored_nodes = []
fringe = [initial_state]
distance = Distance.calculate(initial_state.get_current_state(), final_state.get_current_state(), heuristic)
fringe[0].update_hn(distance)
count = 1

print("---------------Printing Solution Path---------------\n \n")

while not not fringe:
    # select minimum fn for expand
    minimum_fn_index = Puzzle.least_fn(fringe)
    current_node = fringe.pop(minimum_fn_index)
    g = current_node.get_gn() + 1
    goal_node = np.asarray(final_state.get_current_state())

    #check if we reached goal state or not
    if np.array_equal(np.asarray(current_node.get_current_state()), goal_node):
        distance = Distance.calculate(np.asarray(current_node.get_current_state()), goal_node, heuristic)
        explored_nodes.append(current_node)
        Puzzle.goal_reached(explored_nodes, count)
        fringe = []    
    elif not np.array_equal(current_node, goal_node):
        zero = np.where(np.asarray(current_node.get_current_state()) == 0)[0][0]
        count = Node.expand_node(fringe, explored_nodes, current_node, goal_node, zero, g, count, heuristic)
