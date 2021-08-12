class PathFinder:
    def __init__(self, start, end, matrix):
        self.start = start
        self.end = end
        self.matrix = matrix
        self.path = []
        self.paths = []

    def findPath(self, i, j):
        
        (M, N) = (len(self.matrix), len(self.matrix[0]))

        if self.matrix[i][j] == self.matrix[self.end[0]][self.end[1]]:
            self.paths.append(self.path + [{'value':self.matrix[i][j],'coordinate':(i,j)}])
            return
            
        # include the current cell in the path
        cell = {'value':self.matrix[i][j],'coordinate':(i,j)}
        self.path.append(cell)

        if self.start[0] > self.end[0] and self.start[1] > self.end[1]:
            # move left
            if 0 <= i < M and 0 <= j - 1 < N:
                self.findPath(i, j - 1)
            # move up
            if 0 <= i - 1 < M and 0 <= j < N:
                self.findPath(i - 1, j)
        elif self.start[0] < self.end[0] and self.start[1] < self.end[1]:
            if 0 <= i < M and 0 <= j + 1 < N:
                self.findPath(i, j + 1)
            # move down
            if 0 <= i + 1 < M and 0 <= j < N:
                self.findPath(i + 1, j)
        elif self.start[0] < self.end[0] and self.start[1] > self.end[1]:
            # move left
            if 0 <= i < M and 0 <= j - 1 < N:
                self.findPath(i, j - 1)

            # move down
            if 0 <= i + 1 < M and 0 <= j < N:
                self.findPath(i + 1, j)
        elif self.start[0] > self.end[0] and self.start[1] < self.end[1]:
            # move left
            if 0 <= i < M and 0 <= j + 1 < N:
                self.findPath(i, j + 1)

            # move down
            if 0 <= i - 1 < M and 0 <= j < N:
                self.findPath(i - 1, j)
        elif self.start[0] == self.end[0] and self.start[1] < self.end[1]:
            # move right
            if 0 <= i< M and 0 <= j+1 < N:
                self.findPath(i, j+1)
        elif self.start[0] == self.end[0] and self.start[1] > self.end[1]:
            # move left
            if 0 <= i < M and 0 <= j - 1 < N:
                self.findPath(i, j - 1)
        elif self.start[0] > self.end[0] and self.start[1] == self.end[1]:
            # move up
            if 0 <= i-1< M and 0 <= j < N:
                self.findPath(i-1, j)
        elif self.start[0] < self.end[0] and self.start[1] == self.end[1]:
            # move down
            if 0 <= i+1< M and 0 <= j < N:
                self.findPath(i+1, j)

        # backtrack: remove the current cell from the path
        self.path.pop()


# if __name__ == '__main__':
#     import os
#     os.system('cls')

#     mat = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]

#     start = [0, 1]
#     end = [2, 1]
#     x = start[0]
#     y = start[1]

#     obj = PathFinder(start, end, mat)
#     obj.findPath(x, y)
#     print(obj.paths)
