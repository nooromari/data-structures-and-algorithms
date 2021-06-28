from challenges.graph_business_trip.graph_business_trip import business_trip
from Data_Structures.graph.graph import Graph
import pytest

def test_business_trip(graph):
    cities_lists =[['Jordan', 'Syria', 'Turkey'],['Turkey','KSA','Jordan'],['Iraq', 'Syria'],['KSA','Turkey']]
    actual = [business_trip(graph, cities) for cities in cities_lists]
    expected = [(True,'$60'),(False,'$0'),(True,'$25'),(False,'$0')]
    assert actual == expected


@pytest.fixture
def graph():
    graph = Graph()
    graph.add_node('Jordan')
    graph.add_node('Syria')
    graph.add_node('KSA')
    graph.add_node('Iraq')
    graph.add_node('Turkey')
    graph.add_edge('Jordan', 'Iraq',30)
    graph.add_edge('Iraq', 'Jordan',30)
    graph.add_edge('Jordan', 'Syria',20)
    graph.add_edge('Syria', 'Jordan',20)
    graph.add_edge('Jordan', 'KSA',35)
    graph.add_edge('KSA', 'Jordan',35)
    graph.add_edge('Syria', 'Turkey',40)
    graph.add_edge('Turkey', 'Syria',40)
    graph.add_edge('Turkey', 'Iraq',35)
    graph.add_edge('Iraq', 'Turkey',35)
    graph.add_edge('Iraq', 'Syria',25)
    graph.add_edge('Syria', 'Iraq',25)
    graph.add_edge('KSA', 'Iraq',40)
    graph.add_edge('Iraq', 'KSA',40)
    return graph
