# from collections import deque
# from python.tests.test_graph_business_trip import graph
from Data_Structures.stacks_and_queues.stacks_and_queues import Queue, Stack


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
        # else: 
        #     return 'This value is not exist'

    def size(self):
        """ Returns the total number of nodes in the graph """
        return len(self._adjacency_list)

    def breadth_first_search(self, start_vertex=None, action=(lambda x: None)):
        """ Return a collection of nodes in the order of breadth-first traversal. """
        try:
            queue = Queue()
            visited = []

            queue.enqueue(start_vertex)
            visited.append(start_vertex)

            while not queue.is_empty():
                current_vertex = queue.dequeue()
                action(current_vertex)
                neighbors = self.get_neighbors(current_vertex)

                for edge in neighbors:
                    neighbor_vertex = edge[0]

                    if neighbor_vertex in visited:
                        continue
                    else:
                        visited.append(neighbor_vertex)
                    queue.enqueue(neighbor_vertex)

            return visited 
        except TypeError:
            return 'value not exist'

    def depth_first(self, start_vertex):
        """ Return A collection of nodes in their pre-order depth-first traversal order """
        try:
            visited = []
            def walk(vertex):
                visited.append(vertex)
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    if neighbor[0] not in visited:
                        walk(neighbor[0])

            walk(start_vertex)
            return visited
        except TypeError:
            return 'Start vertex is not found in the graph'

        # vertexes = []
        # visited = []
        # stack = Stack()
        # visited.append(start_vertex)
        # stack.push(start_vertex)
        # while not stack.is_empty():
        #     vertex = stack.pop()
        #     vertexes.append(vertex)
        #     vertex_neighbors = self.get_neighbors(vertex)
        #     for neighbor in vertex_neighbors:
        #         if neighbor[0] not in visited :
        #             visited.append(neighbor[0])
        #             stack.push(neighbor[0])
        # return vertexes
    

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
    print('-----------------')
    g.add_edge('A','C')
    g.add_edge('A','B')
    g.add_edge('C','D')
    g.add_edge('B','A')
    # print(g)
    # print(g.add_edge('B','6'))
    # print(g.get_nodes())
    # print(g.size())
    # print(g.get_neighbors('A'))
    # print(g.get_neighbors('B'))
    # print(g.get_neighbors('C'))
    # print(g.get_neighbors('v'))
    print('-----------------------')
    print(g.breadth_first_search('A'))
    print(g.depth_first('A'))

    graph = Graph()

    graph.add_node('Jordan')
    graph.add_node('Syria')
    graph.add_node('KSA')
    graph.add_node('Iraq')
    graph.add_node('Turkey')
    graph.add_edge('Jordan', 'KSA',35)
    graph.add_edge('KSA', 'Jordan',35)
    graph.add_edge('Jordan', 'Iraq',30)
    graph.add_edge('Iraq', 'Jordan',30)
    graph.add_edge('KSA', 'Iraq',40)
    graph.add_edge('Iraq', 'KSA',40)
    graph.add_edge('Turkey', 'Iraq',35)
    graph.add_edge('Iraq', 'Turkey',35)
    graph.add_edge('Iraq', 'Syria',25)
    graph.add_edge('Syria', 'Iraq',25)
    graph.add_edge('Syria', 'Turkey',40)
    graph.add_edge('Turkey', 'Syria',40)
    graph.add_edge('Jordan', 'Syria',20)
    graph.add_edge('Syria', 'Jordan',20)

    print(graph.breadth_first_search('Iraq'))
    print(graph.depth_first('Iraq'))




