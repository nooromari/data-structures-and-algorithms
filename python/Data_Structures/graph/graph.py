# from collections import deque
from Data_Structures.stacks_and_queues.stacks_and_queues import Queue


class Vertex:
    def __init__(self, value=None):
        self.value = value

class Edge:
    def __init__(self, vertex, wight):
        self.vertex = vertex
        self.wight = wight

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        """ Add a node to the graph and return the value """
        v = Vertex(value)
        self._adjacency_list[v.value] = []
        return v.value


    def add_edge(self, start_v , end_v, wight=0):
        """ Adds a new edge between two nodes in the graph """
        if start_v in self._adjacency_list and end_v in self._adjacency_list :
            self._adjacency_list[start_v].append(Edge(end_v, wight))
        else:
            return 'value/values not exist'

    def get_nodes(self):
        """ Returns all of the nodes in the graph as a collection """
        # nodes = [v for v in self._adjacency_list]
        return self._adjacency_list.keys()

    def get_neighbors(self , vertex):
        """ Returns a collection of edges connected to the given node """
        if vertex in self._adjacency_list :
            n = [(v.vertex, v.wight) for v in self._adjacency_list[vertex]]
            return n
        else: 
            return 'This value is not exist'

    def size(self):
        """ Returns the total number of nodes in the graph """
        return len(self._adjacency_list)

    def __str__(self) :
        if self._adjacency_list:
            result = ''
            for v in self._adjacency_list:
                result += f"{v}:{self.get_neighbors(v)}, "
            return result
        else:
            return 'null'

        

if __name__ == "__main__":
    g = Graph()
    print(g)
    print( g.add_node('A'))
    print(g)
    print( g.add_node('B'))
    print( g.add_node('C'))
    print( g.add_node('D'))
    print( g.add_node('A'))
    print('-----------------')
    g.add_edge('A','B')
    g.add_edge('A','C')
    g.add_edge('B','D')
    print(g)
    print(g.add_edge('B','6'))
    print(g.get_nodes())
    print(g.size())
    print(g.get_neighbors('A'))
    print(g.get_neighbors('B'))
    print(g.get_neighbors('C'))
    print(g.get_neighbors('v'))




