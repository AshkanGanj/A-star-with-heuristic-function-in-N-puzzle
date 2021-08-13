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
