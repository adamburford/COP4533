#Adam Burford
#COP4533
#Section 3594
#Program A - Shortest Path
#Dijkstra's Algorithm
#with Adjacency Matrix implementation

from sys import maxsize
from timeit import repeat

class Graph:
    def __init__(self, v, w):
        self.vertices = v
        self.weights = w
        self.vertex_count = len(self.vertices[0])
        self.visited = [False] * self.vertex_count
        self.distance = [0] + ([maxsize] * (self.vertex_count - 1))

    def visisted(self, index):
        return self.visisted[index]

    def next_node(self):

        v = -1

        for index in range(self.vertex_count):

            if not self.visited[index] and (v < 0 or self.distance[index] <= self.distance[v]):
                v = index

        return v

    def dijkstra(self, target):

        for vertex in range(self.vertex_count):

            next_visit = self.next_node()

            for neighbor in range(self.vertex_count):

                if self.vertices[next_visit][neighbor] == 1 and not self.visited[neighbor]:
                    new_distance = self.distance[next_visit] + self.weights[next_visit][neighbor]

                    if self.distance[neighbor] > new_distance:
                        self.distance[neighbor] = new_distance

            self.visited[next_visit] = True

        return self.distance[target]

def main():
    #            A,B,C,D,E,F,G,H,I  
    vertices = [[0,1,1,1,0,0,0,0,0], #A
                [1,0,1,0,0,1,0,1,0], #B
                [1,1,0,1,1,1,0,0,0], #C
                [1,0,1,0,1,0,0,0,1], #D
                [0,0,1,1,0,1,1,0,0], #E
                [0,1,1,0,1,0,1,1,0], #F
                [0,0,0,0,1,1,0,1,1], #G
                [0,1,0,0,0,1,1,0,1], #H
                [0,0,0,1,0,0,1,1,0]] #I

    #            A, B, C, D, E, F, G, H, I  
    weights = [[ 0,22, 9,12, 0, 0, 0, 0, 0], #A
               [22, 0,35, 0, 0,36, 0,34, 0], #B
               [ 9,35, 0, 4,65,42, 0, 0, 0], #C
               [12, 0, 4, 0,33, 0, 0, 0,30], #D
               [ 0, 0,65,33, 0,18,23, 0, 0], #E
               [ 0,36,42, 0,18, 0,39,24, 0], #F
               [ 0, 0, 0, 0,23,39, 0,25,21], #G
               [ 0,34, 0, 0, 0,24,25, 0,19], #H
               [ 0, 0, 0,30, 0, 0,21,19, 0]] #I


    g = Graph(vertices, weights)
    distance = g.dijkstra(len(vertices) - 1)
    print("Shortest distance: " + str(distance) + "\n\n")

    print("Dijkstra Test\n--------------------------------------------------------------------------------")
    
    times = repeat("g = Graph(vertices, weights)\ng.dijkstra(len(vertices) - 1)", globals={'vertices': vertices, 'weights': weights, 'Graph': globals().get('Graph')}, number=10000, repeat=10)
    i = 1
    for time in times: print("Run " + str(i) + ": " + "{0:0.8f}".format(time)); i += 1


if __name__ == "__main__":
    main()
