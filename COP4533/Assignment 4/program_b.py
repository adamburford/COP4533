#Adam Burford
#COP4533
#Section 3594
#Program B - Shortest Path
#Bellman Ford Algorithm

from sys import maxsize
from timeit import repeat

class Graph:
    def __init__(self, c, g):
        self.graph = g
        self.vertex_count = c

    def calculate_bellman_ford(self, source, destination):

        self.distance = [maxsize] * self.vertex_count

        self.distance[source] = 0

        for _ in range(self.vertex_count - 1):
            for a, b, weight in self.graph:
                if self.distance[a] != maxsize and self.distance[a] + weight < self.distance[b]:
                    self.distance[b] = self.distance[a] + weight

        return self.distance[destination]


def main():
    #            A, B, C, D, E, F, G, H, I 
    #            1, 2, 3, 4, 5, 6, 7, 8, 9 
    graph =    [[ 0,22, 9,12, 0, 0, 0, 0, 0], #A
               [22, 0,35, 0, 0,36, 0,34, 0], #B
               [ 9,35, 0, 4,65,42, 0, 0, 0], #C
               [12, 0, 4, 0,33, 0, 0, 0,30], #D
               [ 0, 0,65,33, 0,18,23, 0, 0], #E
               [ 0,36,42, 0,18, 0,39,24, 0], #F
               [ 0, 0, 0, 0,23,39, 0,25,21], #G
               [ 0,34, 0, 0, 0,24,25, 0,19], #H
               [ 0, 0, 0,30, 0, 0,21,19, 0]] #I


    edges = []
    #Make python build the edges for me since I already made this stupid graph array for the first program
    for i in range(len(graph[0])):
        for j in range(i,len(graph[0])):
            if graph[i][j] != 0:
                edges.append([i, j, graph[i][j]])

    g = Graph(9, edges)
    distance = g.calculate_bellman_ford(0,8)
    print("Shortest distance: " + str(distance) + "\n\n")

    print("Bellman Ford Algorithm Test\n--------------------------------------------------------------------------------")
    
    times = repeat("g = Graph(9,edges)\ndistance = g.calculate_bellman_ford(0,8)", globals={'edges': edges, 'Graph': globals().get('Graph')}, number=10000, repeat=10)
    i = 1
    for time in times: print("Run " + str(i) + ": " + "{0:0.8f}".format(time)); i += 1


if __name__ == "__main__":
    main()
