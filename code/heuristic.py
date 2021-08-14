from path import PathFinder
from copy import deepcopy
from operator import sub

class Heuristic:
    def __init__(self, arr, goal):
        self.arr = arr
        self.goal = goal
        self.matrix = []
        self.blank_original = (1,2)

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
    def findPaths(self, start, end, matrix,tile_lock,search_type):
        x, y = start[0], start[1]
        pathfinder = PathFinder(start, end, matrix)
        
        paths = pathfinder.findPath(search_type,tile_lock)
        return paths

    # get paths for all missplaced tiles
    def getPaths(self, distance , matrix_start, matrix_goal):
        paths = {}
        missplaced_tiles_dict = self.missplaced_tiles(
            distance, missplaced_dict=True)
        for tile in missplaced_tiles_dict['list']:
            index_start = self.findTile(tile, matrix_start)
            index_end = self.findTile(tile, matrix_goal)
            paths[str(tile)] = self.findPaths(index_start, index_end, matrix_start,tile,"short")
        return paths
    # return index of blank space

    def findTargetTile(self,tile):
        for i, x in enumerate(self.matrix):
            if tile in x:
                return (i, x.index(tile))

    def swapTile(self, matrix, first, second):
        matrix[first[0]][first[1]], matrix[second[0]][second[1]
                                                      ] = matrix[second[0]][second[1]], matrix[first[0]][first[1]]

    # count steps for returing blank to it's own place
    def setBlankTile(self,tile,blank_index):
        if blank_index == (1,2):
            return 0
        paths = self.findPaths(blank_index, (1,2), self.matrix,int(tile),"all")
        paths.sort(key=len)
        step_counter = 0

        for i in range(1,len(paths[0])):
            target = paths[0][i]
            self.swapTile(self.matrix,blank_index,target)
            step_counter += 1
        return step_counter

    def blankTileSteps(self,matrix, target,tile):
        # store different paths steps
        step_counter = 0
        blank_index = self.findTargetTile(0)
        # if target is blank
        if blank_index == target:
            blank_index = self.findTargetTile(0)
            target = self.findTargetTile(int(tile))
            self.swapTile(matrix,blank_index,target)
            step_counter += 1
            return step_counter

        paths = self.findPaths(blank_index, target, matrix,int(tile),"all")
        paths.sort(key=len)
        i = 0
        for j in range(len(paths[i]) - 1):
            # start index
            index1 = paths[i][j]
            # end index
            index2 = paths[i][j+1]
            # move tile with blank space
            self.swapTile(matrix, index1, index2)
            step_counter += 1
            # if we reached last move
            if j == len(paths[i]) - 2:
                blank_index = self.findTargetTile(0)
                target = self.findTargetTile(int(tile))
                self.swapTile(matrix,blank_index,target)
                step_counter += 1
        return step_counter

    def new_method(self, distance):
        
        step_counter = 0
        matrix_start = self.listToMatrix(self.arr, 3)
        matrix_goal = self.listToMatrix(self.goal, 3)
        self.matrix = matrix_start.copy()
        paths = self.getPaths(distance,self.matrix,matrix_goal)
        distances = {}

        for tile in paths:
            distances[str(tile)] = 0
            step_counter = 0
            self.matrix = self.listToMatrix(self.arr, 3)

            # if tile == '0'
            if tile == '0':
                blank_index = self.findTargetTile(0)
                distances[str(tile)] = self.setBlankTile(tile,blank_index)
                continue
            
            #store steps for different paths
            steps = []
            for i,path in enumerate(paths[tile]):
                self.matrix = self.listToMatrix(self.arr, 3)
                for index in range(1,len(path)):
                    step_counter += self.blankTileSteps(self.matrix, path[index],tile)
                steps.append(step_counter)

            # return 0 to his original place
            target = self.findTargetTile(0)
            step_counter += self.setBlankTile(tile,target)
            distances[str(tile)] = min(steps)       
        return distances

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
            print(distance)
        # heuristic_calculator = Heuristic(heuristic, arr, goal,self.distance)
        # distance = heuristic_calculator
        return distance
