from path import PathFinder
from copy import deepcopy

class Heuristic:
    def __init__(self, arr, goal):
        self.arr = arr
        self.goal = goal
        self.matrix = []
        self.orginal_matrix = []

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

    # find each missplaced tiles in matrix
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
    def getPaths(self, distance , matrix_start, matrix_goal):
        paths = {}
        missplaced_tiles_dict = self.missplaced_tiles(
            distance, missplaced_dict=True)
        for tile in missplaced_tiles_dict['list']:
            index_start = self.findTile(tile, matrix_start)
            index_end = self.findTile(tile, matrix_goal)
            paths[str(tile)] = self.findPaths(
                index_start, index_end, matrix_start)
        return paths
    # return index of blank space

    def findblank(self):
        for i, x in enumerate(self.matrix):
            if 0 in x:
                return (i, x.index(0))

    def swapTile(self, matrix, first, second, counter):
        matrix[first[0]][first[1]], matrix[second[0]][second[1]
                                                      ] = matrix[second[0]][second[1]], matrix[first[0]][first[1]]

        counter += 1
        return counter

    def blankTileSteps(self, target):
        # store different paths steps
        step_counter = 0
        blank_index = self.findblank()
        paths = self.findPaths(blank_index, target, self.matrix)
        # sort paths by len
        paths.sort(key=lambda x: len(x))
        #  select shortest path
        i = 0
        for j in range(len(paths[i]) - 1):
            # start index
            index1 = paths[i][j]['coordinate']
            # end index
            index2 = paths[i][j+1]['coordinate']
            # move tile with blank space
            step_counter = self.swapTile(self.matrix, index1, index2, step_counter)
            

        return step_counter

    def new_method(self, distance):
        
        step_counter = 0
        matrix_start = self.listToMatrix(self.arr, 3)
        matrix_goal = self.listToMatrix(self.goal, 3)
        
        self.matrix = deepcopy(matrix_start)

        paths = self.getPaths(distance,self.matrix,matrix_goal)
        distances = {}
        for tile in paths:
            distances[str(tile)] = 0
            step_counter = 0

            for i,path in enumerate(paths[tile]):
                for index in range(len(path)):
                    # list of zeros for store steps of paths
                    temp = []
                    # first cell
                    if index == 0:
                        pass
                    else:
                        # +1 is for last move
                        step_counter += self.blankTileSteps(
                            paths[tile][0][index]['coordinate']) + 1
                        temp.append(step_counter)
                distances[str(tile)] = step_counter        
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
