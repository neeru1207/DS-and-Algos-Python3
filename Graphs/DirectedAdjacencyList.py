from queue import Queue, LifoQueue
import sys


class Node:
    def __init__(self, data, weight):
        self.data = data
        self.next = None
        self.weight = weight


class AdjacencyList:
    def __init__(self, i):
        self.head = Node(i, 0)

    def add_node(self, i, weight):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(i, weight)

    def print_list(self):
        temp = self.head
        print("[", end="")
        while temp.next is not None:
            print("{0}".format(temp.data), end=",")
            temp = temp.next
        print("{0}]".format(temp.data))


class Graph:
    def __init__(self, num_of_vertices, num_of_edges, isweighted):
        self.num_of_vertices = num_of_vertices
        self.graphlist = [AdjacencyList(i) for i in range(num_of_vertices)]
        self.isweighted = isweighted
        self.num_of_edges = num_of_edges

    def addEdge(self, start, end, weight):
        self.graphlist[start].add_node(end, weight)
    def create_graph(self):
        for i in range(self.num_of_edges):
            if not self.isweighted:
                st, end = map(int, input("Enter the start and end of edge " + str(i) + " as space seperated integers\n").split())
                self.addEdge(st, end, 1)
            else:
                st, end, weight = map(int, input("Enter the start, end and weight of edge " + str(i) + " as space seperated integers\n").split())
                self.addEdge(st, end, weight)

    def bfs(self, start_vertex):
        vertq = Queue()
        vertq.put(start_vertex)
        visited = [False for _ in range(self.num_of_vertices)]
        while not vertq.empty():
            presvtx = vertq.get()
            visited[presvtx] = True
            print("{0}".format(presvtx), end=" ")
            temp = self.graphlist[presvtx].head
            while temp is not None:
                if not visited[temp.data]:
                    vertq.put(temp.data)
                temp = temp.next
        print("")

    def print_graph(self):
        for i in self.graphlist:
            i.print_list()

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
            temp = self.graphlist[presvrtx].head
            while temp is not None:
                if not visited[temp.data]:
                    verts.put(temp.data)
                temp = temp.next

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
        while False in shortest_path_set:
            pickdvrtx = self.djikstra_minselect_util(distance, shortest_path_set)
            print(pickdvrtx)
            shortest_path_set[pickdvrtx] = True
            temp = self.graphlist[pickdvrtx].head.next
            while temp is not None:
                if distance[temp.data] > distance[pickdvrtx] + temp.weight:
                    distance[temp.data] = distance[pickdvrtx] + temp.weight
                temp = temp.next
        print(*distance)
