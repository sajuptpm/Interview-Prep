"""
@author: David Lei
@since: 21/08/2016
@modified:

Implementation of graph data structure using Adjacency List
Assuming directed graph
- O(e/v) find edge
- O(e/v) remove edge
- O(e/v) add edge
- O(e/v) enumerate edges for node

with space complexity O(v + e)
"""
from Algorithms_DataStructures.Graphs.Implementations.Structures import Vertex, Edge
#from Structures import Vertex, Edge

class Graph_List:
    def __init__(self, no_vertices):
        self.list = [Vertex() for _ in range(no_vertices)]     # initialize to an array of vertices

    def get_vertices(self):
        v = []
        for vertex in self.list:
            v.append(vertex)
        return v

    def add_vertex(self, v, rep):
        new_list = []                                           # creates a new linked list
        vertex = self.list[v]
        vertex.name = v                                         # set vertex name
        vertex.rep = rep                                        # string representation
        vertex.pointer = new_list                               # set vertex pointer
        return vertex

    def add_edge(self, origin_vertex, destination_vertex, edge_name=None):
        origin = origin_vertex.name
        destination = destination_vertex.name
        edge = Edge(origin_vertex, destination_vertex, edge_name)
        self.list[origin].pointer.append(edge)
        return edge

    def find_edge(self, origin_vertex, destination_vertex):
        origin = origin_vertex.name
        for edge in self.list[origin].pointer:
            if destination_vertex.name == edge.destination.name:
                return edge
        return False

    def get_adjacent_edges(self, origin_vertex):
        origin = origin_vertex.name
        edges = []
        for edge in self.list[origin].pointer:
            edges.append(edge)
        return edges

    def remove_edge(self, origin_vertex, destination_vertex):
        origin = origin_vertex.name
        destination = destination_vertex.name
        for i in range(len(self.list[origin].pointer)):
            if self.list[origin].pointer[i].destination.name == destination:
                del self.list[origin].pointer[i]
                break

    def print_graph(self):
        for vertex in self.list:
            print("Vertex: " + str(vertex.name), end =" -> ")
            edges_to = vertex.pointer
            if edges_to:
                for edge in edges_to:
                    print(str(edge.destination.rep) + " via " + str(edge.name), end=", ")
            else:
                print(" None", end="")
            print()

if __name__ == "__main__":
    print("Adjacency list")
    G = Graph_List(5)
    G.print_graph()
    A = G.add_vertex(0,"A")
    B = G.add_vertex(1,"B")
    C = G.add_vertex(2,"C")
    D = G.add_vertex(3,"D")
    E = G.add_vertex(4,"E")
    G.add_edge(A, C, "street a")
    G.add_edge(A, D, "street b")
    G.add_edge(A, E, "street c")
    G.add_edge(C, A, "street a")
    G.add_edge(C, E, "loopy loop")
    G.add_edge(D, A, "street b")
    G.add_edge(D, E, "sesame street")
    G.add_edge(E, A, "mi goreng road")
    G.add_edge(E, C, "eastlink")
    G.add_edge(E, D, "victory road")
    print("\nPrinting after adding vertices and edges\n")
    G.print_graph()
    G.remove_edge(A, C)
    print("\nRemoved A to C\n")
    G.print_graph()
    # implementation works :D