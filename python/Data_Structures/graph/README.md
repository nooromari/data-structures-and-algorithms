# Graphs
<!-- Short summary or background information -->

A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.


| Term | Definition |
|--|--|
| Vertex | is a data object that can have zero or more adjacent vertices. Also called a â€œnodeâ€. |
| Edge | is a connection between two nodes. |
| Neighbor | The neighbors of a node are its adjacent nodes, i.e., are connected via an edge. |
| Degree | The degree of a vertex is the number of edges connected to that vertex. |

## Challenge
<!-- Description of the challenge -->

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

(**add node** , **add edge** , **get nodes** , **size** , **get neighbors**)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

- **add node**: Big O (1)
- **add edge**: Big O (1)
- **get nodes**: Big O (n)
- **get neighbors**: Big O (n)
- **size**: Big O (1)


## API
<!-- Description of each method publicly available in your Graph -->

`add_node`: 

- Arguments: value
- Returns: The added node
- Add a node to the graph

`add_edge`: 

- Arguments: 2 nodes to be connected by the edge, weight (optional)
- Returns: nothing
- Adds a new edge between two nodes in the graph
- If specified, assign a weight to the edge
- Both nodes should already be in the Graph

`get_nodes`:

- Arguments: none
- Returns: all of the nodes in the graph as a collection (set, list, or similar)

`get_neighbors`:

- Arguments: node
- Returns: a collection of edges connected to the given node
- Include the weight of the connection in the returned collection

`size`:

- Arguments: none.
- Returns: the total number of nodes in the graph.

[code](graph.py)