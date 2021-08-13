from numpy import exp, matrix
from path import PathFinder


class Heuristic:
    def __init__(self, arr, goal):
        self.arr = arr
        self.goal = goal
        self.matrix = []
        self.matrx_copy = []

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
    def getPaths(self, distance):
        paths = {}
        matrix_start = self.listToMatrix(self.arr, 3)
        self.matrix = matrix_start
        matrix_goal = self.listToMatrix(self.goal, 3)

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

    def blankTileSteps(self,target, matrix_copy):
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
            step_counter = self.swapTile(
                matrix_copy, index1, index2, step_counter)
        # for i in range(len(paths)):

        #     if not flage:

        #         flage = True

        #     for j in range(len(paths[i]) - 1):
        #         # start index
        #         index1 = paths[i][j]['coordinate']
        #         # end index
        #         index2 = paths[i][j+1]['coordinate']
        #         # move tile with blank space
        #         step_counter += self.swapTile(
        #             matrix_copy, index1, index2, step_counter)

        return step_counter

    def new_method(self, distance):
        step_counter = 0
        self.matrx_copy = self.matrix
        paths = self.getPaths(distance)
        distances = {}
        for tile in paths:
            array_copy = self.arr
            steps = []
            distances[str(tile)] = 0
            # sort based on len of path
            paths[tile].sort(key=lambda x: len(x))
            for index, item in enumerate(paths[tile][0]):
                # first cell
                if index == 0:
                    pass
                else:
                    # +1 is for last move
                    step_counter = self.blankTileSteps(
                        paths[tile][0][index]['coordinate'],self.matrx_copy) + 1
                    distances[str(tile)] = step_counter
                    step_counter = 0

            # for path in paths[tile]:
            #     for index, item in enumerate(path):
            #         # first cell
            #         if index == 0:
            #             pass
            #         else:
            #             # +1 is for last move
            #             step_counter = self.blankTileSteps(
            #                 path[index]['coordinate']) + 1
            #             distances[str(tile)] = step_counter
            #             step_counter = 0

                        # temp = self.findPaths(
                        #     blank_space_coordinate, path[index]['coordinate'], self.matrix)
                        # # find shortest path
                        # min = float('inf')
                        # for i in temp:
                        #     if len(i) < min:
                        #         min = len(i) - 1
                        # distances[tile] += min
                        # if len(paths[tile]) > 1:
                        #     steps.append(distances[str(tile)])
                        # blank_space_coordinate = path[0]['coordinate']

                # if len(paths[tile]) > 1:
                #     distances[tile] = min(steps)
                #     steps = []
                    # # last cell can't have +1 so blank should come to last cell
                    # try:
                    #     temp = self.findPaths(blank_space_coordinate,path[index+1]['coordinate'],self.matrix)
                    #     # find shortest path
                    #     min = float('inf')
                    #     for i in temp:
                    #         if len(i) < min:
                    #             min = len(i)

                    #     distances[str(tile)] = step_counter + min + 1
                    # except:
                    #     pass
                    #     # temp = self.findPaths(blank_space_coordinate,path[index]['coordinate'],self.matrix)
                    #     # # find shortest path
                    #     # for i in temp:
                    #     #     if len(i) < min:
                    #     #         min = len(i)

                    # # step_counter += min

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
