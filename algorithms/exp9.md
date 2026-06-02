# Algorithm

1. Create a predefined undirected graph with 7 nodes and a specific set of edges.
2. Check if the graph contains an Eulerian circuit by using the `nx.is_eulerian()` function (which verifies that all vertices have an even degree and all edges belong to a single connected component).
3. If the graph is Eulerian, compute the exact sequence of edges forming the circuit using `nx.eulerian_circuit()`.
4. Extract the ordered list of vertices traversed in the circuit to form the path string.
5. If the graph is not Eulerian, return an empty circuit.
6. Plot the original graph next to a highlighted version showing the Eulerian circuit path (if one exists).