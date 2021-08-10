import os,time

class PathFinder:
    def __init__(self, start, end, matrix):
        self.start = start
        self.end = end
        self.matrix = matrix
        self.path = []

    def findPaths(self, i, j):
        (M, N) = (len(self.matrix), len(self.matrix[0]))

        if self.matrix[i][j] == self.matrix[self.end[0]][self.end[1]]:
            print(self.path + [self.matrix[i][j]])
            return
        # # if the last cell is reached, print the route
        # if i == M - 1 and j == N - 1:
        #     print(path + [mat[i][j]])
        #     return

        # include the current cell in the path
        self.path.append(self.matrix[i][j])

        if self.start[0] > self.end[0] and self.start[1] > self.end[1]:
            # move left
            if 0 <= i < M and 0 <= j - 1 < N:
                self.findPaths(i, j - 1)
            # move up
            if 0 <= i - 1 < M and 0 <= j < N:
                self.findPaths(i - 1, j)
        elif self.start[0] < self.end[0] and self.start[1] < self.end[1]:
            if 0 <= i < M and 0 <= j + 1 < N:
                self.findPaths(i, j + 1)
            # move down
            if 0 <= i + 1 < M and 0 <= j < N:
                self.findPaths(i + 1, j)
        elif self.start[0] < self.end[0] and self.start[1] > self.end[1]:
            # move left
            if 0 <= i < M and 0 <= j - 1 < N:
                self.findPaths(i, j - 1)

            # move down
            if 0 <= i + 1 < M and 0 <= j < N:
                self.findPaths(i + 1, j)
        elif self.start[0] > self.end[0] and self.start[1] < self.end[1]:
            # move left
            if 0 <= i < M and 0 <= j + 1 < N:
                self.findPaths(i, j + 1)

            # move down
            if 0 <= i - 1 < M and 0 <= j < N:
                self.findPaths(i - 1, j)

        # backtrack: remove the current cell from the path
        self.path.pop()


if __name__ == '__main__':
    os.system('cls')
    # starting time
    timer_start = time.time()
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    start = [0, 1]
    end = [2, 2]
    x = start[0]
    y = start[1]

    obj = PathFinder(start, end, mat)

    obj.findPaths(x, y)
    timer_end = time.time()
    print("Execution time:",timer_end - timer_start)