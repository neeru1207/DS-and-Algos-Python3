from queue import Queue
from queue import LifoQueue
import sys

class Graph:

    # Numbering of vertices and edges starts from 0
    def __init__(self, num_of_vertices, num_of_edges, isweighted):
        self.num_of_vertices = num_of_vertices
        self.num_of_edges = num_of_edges
        self.isweighted = isweighted
        self.adjmat = [[0 for _ in range(self.num_of_vertices)] for _ in range(self.num_of_vertices)]

    def add_edge(self, start, end, weight):
        self.adjmat[start][end] = weight

    def create_graph(self):
        for i in range(self.num_of_edges):
            if not self.isweighted:
                st, end = map(int, input("Enter the start and end of edge " + str(i) + " as space seperated integers\n").split())
                self.add_edge(st, end, 1)
            else:
                st, end, weight = map(int, input("Enter the start, end and weight of edge " + str(i) + " as space seperated integers\n").split())
                self.add_edge(st, end, weight)

    def bfs(self, start_vertex):
        vertq = Queue()
        vertq.put(start_vertex)
        visited = [False for i in range(self.num_of_vertices)]
        while not vertq.empty():
            presvtx = vertq.get()
            visited[presvtx] = True
            print("{0}".format(presvtx), end=" ")
            for i in range(self.num_of_vertices):
                if self.adjmat[presvtx][i] >= 1 and i != presvtx and not visited[i]:
                    vertq.put(i)
        print("")

    def dfs(self):
        visited = [False for i in range(self.num_of_vertices)]
        for i in range(self.num_of_vertices):
            if not visited[i]:
                self.dfsutil(i, visited)

    def dfsutil(self, vertex, visited):
        verts = LifoQueue()
        verts.put(vertex)
        while not verts.empty():
            presvrtx = verts.get()
            visited[presvrtx] = True
            print("{0}".format(presvrtx), end=" ")
            for i in range(self.num_of_vertices):
                if self.adjmat[presvrtx][i] >= 1 and i != presvrtx and not visited[i]:
                    verts.put(i)

    def djikstra_minselect_util(self, distance, spt_set):
        mindist = sys.maxsize
        minindex = -1
        for i in range(self.num_of_vertices):
            if distance[i] < mindist and not spt_set[i]:
                mindist = distance[i]
                minindex = i
        return minindex

    def djikstra(self, start_vertex):
        distance = [sys.maxsize for i in range(self.num_of_vertices)]
        distance[start_vertex] = 0
        shortest_path_set = [False for i in range(self.num_of_vertices)]
        #while False in shortest_path_set:
        for i in range(self.num_of_vertices):
            pickdvrtx = self.djikstra_minselect_util(distance, shortest_path_set)
            shortest_path_set[pickdvrtx] = True
            for i in range(self.num_of_vertices):
                if self.adjmat[pickdvrtx][i] != 0:
                    if distance[i] > distance[pickdvrtx] + self.adjmat[pickdvrtx][i]:
                        distance[i] = distance[pickdvrtx] + self.adjmat[pickdvrtx][i]
        print(*distance)





