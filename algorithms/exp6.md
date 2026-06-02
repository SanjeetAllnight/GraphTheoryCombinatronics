# Algorithm

1. Read the number of vertices and a weighted adjacency matrix from the user.
2. Construct an undirected graph from the matrix, assigning the provided weights to edges.
3. Extract all edges from the graph and sort them in ascending order based on their weight.
4. Initialize an empty list for the Minimum Spanning Tree (MST) edges and a tracking variable for the total cost.
5. Iterate through the sorted edges and tentatively add each edge to a temporary graph.
6. Use `nx.is_forest()` to check if the newly added edge creates a cycle.
7. If a cycle is formed, remove the edge. Otherwise, permanently add the edge to the MST list, add its weight to the total cost, and record the step.
8. Stop the process when the number of edges in the MST equals the number of vertices minus one.
9. Render the step-by-step addition of edges visually.