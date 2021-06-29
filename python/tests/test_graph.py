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
    actual = [n for n in graph_test.get_nodes()]
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
    expected = None
    assert actual == expected

def test_size(graph_test):
    """ The proper size is returned, representing the number of nodes in the graph """
    actual = graph_test.size()
    expected = 4
    assert actual == expected


def test_breadth_first_search(graph_test):
    actual = graph_test.breadth_first_search('B')
    expected = ['B', 'D']
    assert actual == expected

    graph_test.add_edge('D','A')
    actual2 = graph_test.breadth_first_search('B')
    expected2 = ['B', 'D', 'A', 'C']
    assert actual2 == expected2

    actual3 = graph_test.breadth_first_search('n')
    expected3 = 'value not exist'
    assert actual3 == expected3

def test_depth_first(graph_test2):
    actual = graph_test2.depth_first('Jordan')
    expected = ['Jordan', 'KSA', 'Iraq', 'Turkey', 'Syria']
    assert actual == expected

    actual2 = graph_test2.depth_first('KSA')
    expected2 = ['KSA', 'Jordan', 'Iraq', 'Turkey', 'Syria']
    assert actual2 == expected2

    actual3 = graph_test2.depth_first('n')
    expected3 = 'Start vertex is not found in the graph'
    assert actual3 == expected3

@pytest.fixture
def graph_test():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_edge('A','B',9)
    g.add_edge('A','C')
    g.add_edge('B','D')
    return g

@pytest.fixture
def graph_test2():

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
    return graph