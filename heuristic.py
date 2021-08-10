from path import PathFinder

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
