[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Brief history
A* was created as part of the Shakey project, which had the aim of building a mobile robot that could plan its own actions. Nils Nilsson originally proposed using the Graph Traverser algorithm for Shakey's path planning. Graph Traverser is guided by a heuristic function h(n), the estimated distance from node n to the goal node: it entirely ignores g(n), the distance from the start node to n. Bertram Raphael suggested using the sum, g(n) + h(n). Peter Hart invented the concepts we now call admissibility and consistency of heuristic functions. A* was originally designed for finding least-cost paths when the cost of a path is the sum of its costs, but it has been shown that A* can be used to find optimal paths for any problem satisfying the conditions of a cost algebra.

The original 1968 A* paper contained a theorem stating that no A*-like algorithm could expand fewer nodes than A* if the heuristic function is consistent and A*’s tie-breaking rule is suitably chosen. A ″correction″ was published a few years later claiming that consistency was not required, but this was shown to be false in Dechter and Pearl's definitive study of A*'s optimality (now called optimal efficiency), which gave an example of A* with a heuristic that was admissible but not consistent expanding arbitrarily more nodes than an alternative A*-like algorithm.

# Description for A* Algorithm
A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied.

At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes
```math
f(n)=g(n)+h(n)}f(n)=g(n)+h(n)
```
where n is the next node on the path, g(n) is the cost of the path from the start node to n, and h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal. A* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be extended. The heuristic function is problem-specific. If the heuristic function is admissible, meaning that it never overestimates the actual cost to get to the goal, A* is guaranteed to return a least-cost path from start to goal.

Typical implementations of A* use a priority queue to perform the repeated selection of minimum (estimated) cost nodes to expand. This priority queue is known as the open set or fringe. At each step of the algorithm, the node with the lowest f(x) value is removed from the queue, the f and g values of its neighbors are updated accordingly, and these neighbors are added to the queue. The algorithm continues until a removed node (thus the node with the lowest f value out of all fringe nodes) is a goal node.[b] The f value of that goal is then also the cost of the shortest path, since h at the goal is zero in an admissible heuristic.

The algorithm described so far gives us only the length of the shortest path. To find the actual sequence of steps, the algorithm can be easily revised so that each node on the path keeps track of its predecessor. After this algorithm is run, the ending node will point to its predecessor, and so on, until some node's predecessor is the start node.
# Brief Description for project

In this project, I have Two main goal:
> *  find a new function to improve algorithm

> * Avoid high-order functions that take a lot of time to execute.

I first move the empty space in all the possible directions in the start state and calculate the f-score for each state. This is called expanding the current state.
After expanding the current state, it is pushed into the closed list and the newly generated states are pushed into the open list. A state with the least f-score is selected and expanded again. This process continues until the goal state occurs as the current state. Basically, here we are providing the algorithm a measure to choose its actions. The algorithm chooses the best possible action and proceeds in that path.
This solves the issue of generating redundant child states, as the algorithm will expand the node with the least f-score.

# Implementation

I have used six classes in my code: Node, Puzzle, Movements, pathFinder, Distance, and Heuristic.
Node class defines the structure of the state(configuration) and provides functions to expand states and generate child states from the current state. Movement class allows us to do movements in our puzzles. Puzzle class checks if we reach our goal state or not and, Also, print our states. PathFinder class plays an essential role. It finds different paths in our puzzle with a graph search algorithm. Distance and Heuristic are responsible for return distance for each state.

# New Heuristic

In the new method, At first, we need to find all misplaced tiles and then calculate the number of steps that are needed for each tile to reach its actual place, and at the end, the number of steps for blank space to reach its place is added to the sum of distance. These steps should be done for all out of placed tiles, and at the end, the algorithm chooses the maximum number as h_score.

# Result comparing
### A figure to show the difference and improvements between the new method and other heuristics.
<p>
  <img src="https://user-images.githubusercontent.com/55941654/130363646-3e2767d0-2cc1-4d07-b816-73f236f195cd.png">
</p>

### each distance's state frequency.

<p>
  <img src="https://user-images.githubusercontent.com/55941654/130363661-4604924c-d8bc-4d8a-ad08-36b6b3a9f9b6.png">
</p>
