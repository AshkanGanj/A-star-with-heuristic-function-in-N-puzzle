import networkx as nx

class PathFinder:
    def __init__(self, start, end, matrix):
        self.start = start
        self.end = end
        self.matrix = matrix
        
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
            for i, x in enumerate(self.matrix):
                if tile_lock in x:
                    tile_lock_coordinate =  (i, x.index(int(tile_lock)))

            paths = [p for p in nx.all_simple_paths(G, source=coor1,target=coor2)]
            i = 0
            while i <= len(paths) -1:
                if tile_lock_coordinate in paths[i] and not(tile_lock == 0):
                    paths.remove(paths[i])
                    i = -1
                i +=1
            return paths

        elif path_type == "short":
            return ([p for p in nx.all_shortest_paths(G, source=coor1,target=coor2)])
