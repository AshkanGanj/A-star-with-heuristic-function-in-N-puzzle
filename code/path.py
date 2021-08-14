import networkx as nx

class PathFinder:
    def __init__(self, start, end, matrix):
        self.start = start
        self.end = end
        self.matrix = matrix
        # self.path = []
        # self.paths = []
        
    def findPath(self,path_type,tile_lock):     
        G = nx.grid_2d_graph(2,3)

        pos = {(x,y):(y,-x) for x,y in G.nodes()}
        nx.draw(G, pos=pos, 
                node_color='lightgreen', 
                with_labels=True,
                node_size=600)

        coor1 = self.start 
        coor2 = self.end

        if path_type == "all":
            return ([p for p in nx.all_simple_paths(G, source=coor1,target=coor2)])

        elif path_type == "short":
            return ([p for p in nx.all_shortest_paths(G, source=coor1,target=coor2)])

#     # def findPath(self, i, j,tile_lock):
#     #     # get target file to not change it
#     #     for i, x in enumerate(self.matrix):
#     #         if tile_lock in x:
#     #             tile_lock_coordinate =  (i, x.index(int(tile_lock)))
        
#     #     (M, N) = (len(self.matrix), len(self.matrix[0]))

#     #     if self.matrix[i][j] == self.matrix[self.end[0]][self.end[1]]:
#     #         self.paths.append(self.path + [{'value':self.matrix[i][j],'coordinate':(i,j)}])
#     #         return
            
#     #     # include the current cell in the path
#     #     cell = {'value':self.matrix[i][j],'coordinate':(i,j)}
#     #     self.path.append(cell)

#     #     if self.start[0] > self.end[0] and self.start[1] > self.end[1]:
#     #         # move left
#     #         if 0 <= i < M and 0 <= j - 1 < N:
#     #             if self.matrix[i][j-1] == int(tile_lock) and (tile_lock != -1):
#     #                 self.findPath(i - 1, j,tile_lock)
#     #             else:
#     #                 self.findPath(i, j - 1,tile_lock)
#     #         # move up
#     #         if 0 <= i - 1 < M and 0 <= j < N:
#     #             if self.matrix[i-1][j] == int(tile_lock) and (tile_lock != -1):
#     #                 self.findPath(i, j - 1,tile_lock)
#     #             else:
#     #                 self.findPath(i - 1, j,tile_lock)

#     #     elif self.start[0] < self.end[0] and self.start[1] < self.end[1]:
#     #         #move right
#     #         if 0 <= i < M and 0 <= j + 1 < N:
#     #             if self.matrix[i][j+1] == int(tile_lock)  and (tile_lock != -1):
#     #                 self.findPath(i + 1, j,tile_lock)
#     #             else:
#     #                 self.findPath(i, j + 1,tile_lock)
                
#     #         # move down
#     #         if 0 <= i + 1 < M and 0 <= j < N:
#     #             if self.matrix[i+1][j] == int(tile_lock) and (tile_lock != -1):
#     #                 self.findPath(i, j + 1,tile_lock)
#     #             else:
#     #                 self.findPath(i + 1, j,tile_lock)
                
#     #     elif self.start[0] < self.end[0] and self.start[1] > self.end[1]:
#     #         # move left
#     #         if 0 <= i < M and 0 <= j - 1 < N:
#     #             if self.matrix[i][j-1] == int(tile_lock) and (tile_lock != -1):
#     #                 self.findPath(i + 1, j,tile_lock)
#     #             else:
#     #                 self.findPath(i, j - 1,tile_lock)
#     #         # move down
#     #         if 0 <= i + 1 < M and 0 <= j < N:
#     #             if self.matrix[i+1][j] == int(tile_lock) and (tile_lock != -1):
#     #                 self.findPath(i, j - 1,tile_lock)
#     #             else:
#     #                 self.findPath(i + 1, j,tile_lock)
#     #     elif self.start[0] > self.end[0] and self.start[1] < self.end[1]:
#     #         # move left
#     #         if 0 <= i < M and 0 <= j + 1 < N:
#     #             if self.matrix[i][j+1] == int(tile_lock) and (tile_lock != -1):
#     #                 self.findPath(i-1,j,tile_lock)
#     #             else:
#     #                 self.findPath(i, j + 1,tile_lock)
#     #         # move down
#     #         if 0 <= i - 1 < M and 0 <= j < N:
#     #             if self.matrix[i-1][j] == int(tile_lock) and (tile_lock != -1):
#     #                 self.findPath(i, j + 1,tile_lock)
#     #             else:
#     #                 self.findPath(i - 1, j,tile_lock)
#     #     elif self.start[0] == self.end[0] and self.start[1] < self.end[1]:
#     #         # move right
#     #         if 0 <= i< M and 0 <= j+1 < N:
#     #             self.findPath(i, j+1,tile_lock)
#     #     elif self.start[0] == self.end[0] and self.start[1] > self.end[1]:
#     #         # move left
#     #         if 0 <= i < M and 0 <= j - 1 < N:
#     #             self.findPath(i, j - 1,tile_lock)
#     #     elif self.start[0] > self.end[0] and self.start[1] == self.end[1]:
#     #         # move up
#     #         if 0 <= i-1< M and 0 <= j < N:
#     #             self.findPath(i-1, j,tile_lock)
#     #     elif self.start[0] < self.end[0] and self.start[1] == self.end[1]:
#     #         # move down
#     #         if 0 <= i+1< M and 0 <= j < N:
#     #             self.findPath(i+1, j,tile_lock)

#     #     # backtrack: remove the current cell from the path
#     #     self.path.pop()


# if __name__ == '__main__':
#     import os
#     os.system('clear')

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
    
#     # obj.findPath(x, y)
#     obj.search()
#     print(obj.paths)
