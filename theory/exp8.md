# Experiment 08

# Aim
To implement generation of closed walks, trails and paths in a connected graph.

# Theory
A graph is a mathematical structure used to represent relationships between different objects. It consists of a set of vertices (also called nodes) and a set of edges which connect these vertices. Graphs are widely used in real life to represent systems such as road maps, communication networks, and social connections. In this experiment, we are working with a connected graph, which means that every vertex in the graph can be reached from any other vertex through some path.
In graph theory, there are different ways to traverse or move through a graph. The main concepts studied in this experiment are walk, closed walk, path, and trail. These concepts help us understand how movement happens inside a graph and what restrictions are applied in each case.
A walk is the most basic type of traversal. It is simply a sequence of vertices where each consecutive pair of vertices is connected by an edge. In a walk, there are no restrictions, which means both vertices and edges can be repeated any number of times. Because of this flexibility, a walk can be of any form as long as it follows the connections of the graph.
A closed walk is a special type of walk in which the starting and ending vertices are the same. This means we begin at a vertex, move through a series of edges, and finally return to the same starting point. Closed walks are useful for understanding cycles or loops present in a graph.
A path is a more restricted form of a walk. In a path, no vertex is repeated. This means once a vertex is visited, it cannot be visited again. Because of this restriction, a path represents a simple and non-repeating route through the graph. Paths are important in many applications where revisiting the same location is not allowed or not required.
A trail is another variation of a walk. In a trail, edges are not allowed to repeat, but vertices can be repeated. This means we cannot travel along the same edge more than once, but we are allowed to pass through the same vertex again using different edges. Trails are useful in situations where connections cannot be reused, but locations can be revisited.
In the program, the graph is defined using a set of vertices and edges. Each vertex is assigned a fixed position so that the structure of the graph remains clear and consistent in all outputs. The edges are drawn between the corresponding vertices to form the complete graph.
To demonstrate the different concepts, specific sequences are chosen carefully. For the closed walk, a sequence of vertices is selected such that the starting and ending vertex is the same. For the path, the sequence is chosen such that no vertex is repeated. For the trail, the sequence is selected such that no edge is repeated, even though some vertices may appear more than once.
The graph is first drawn in its complete form to show all vertices and edges. Then, for each case (closed walk, path, and trail), the selected edges are highlighted clearly so that the traversal can be easily identified. This helps in visually comparing the different types of traversals and understanding their properties.
Finally, all four graphs are displayed together in a grid format, showing the original graph along with the closed walk, path, and trail. This side-by-side comparison makes it easy to observe the differences between them and understand how each concept works in practice.
Thus, through this experiment, we gain a clear understanding of walk, closed walk, path, and trail, and how these concepts are applied in graph traversal. The visual representation further helps in strengthening the understanding of these important graph theory concepts.

# Conclusion
Generation of closed walks, trails and paths in a connected graph was successfully implemented.
