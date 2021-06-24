from Data_Structures.graph.graph import Graph
import pytest


def test_graph():
    """
    An empty graph properly returns null
    """
    actual = str(Graph())
    expected = 'null'
    assert actual == expected


def test_add_graph():
    """ 
    Node can be successfully added to the graph 
    A graph with only one node and edge can be properly returned
    """
    g = Graph()
    actual = g.add_node('A')
    expected = 'A'
    assert actual == expected

    actual2 = str(g) 
    expected2 = 'A:[], '
    assert actual2 == expected2

    actual3 = g.add_node('A')
    expected3 = 'This value is already exist'
    assert actual3 == expected3

def test_add_edge(graph_test):
    """ An edge can be successfully added to the graph """
    actual = str(graph_test)
    expected = 'A:[(\'B\', 9), (\'C\', 0)], B:[(\'D\', 0)], C:[], D:[], '
    assert actual == expected

    actual2 = graph_test.add_edge('B','6')
    expected2 = 'value/values not exist'
    assert actual2 == expected2

def test_get_nodes(graph_test):
    """ A collection of all nodes can be properly retrieved from the graph """
    actual = graph_test.get_nodes()
    expected = ['A', 'B', 'C', 'D'] 
    assert actual == expected

def test_get_neighbors(graph_test):
    """ 
    All appropriate neighbors can be retrieved from the graph 
    Neighbors are returned with the weight between nodes included
    """
    actual = graph_test.get_neighbors('A')
    expected = [('B', 9), ('C', 0)]
    assert actual == expected

    actual = graph_test.get_neighbors('D')
    expected = []
    assert actual == expected

    actual = graph_test.get_neighbors('x')
    expected = 'This value is not exist'
    assert actual == expected

def test_size(graph_test):
    """ The proper size is returned, representing the number of nodes in the graph """
    actual = graph_test.size()
    expected = 4
    assert actual == expected


@pytest.fixture
def graph_test():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('A')
    g.add_edge('A','B',9)
    g.add_edge('A','C')
    g.add_edge('B','D')
    return g
