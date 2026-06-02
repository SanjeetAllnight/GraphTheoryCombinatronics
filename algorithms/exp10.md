# Algorithm

1. Read the number of vertices and an adjacency matrix from the user.
2. Construct an unweighted undirected graph from the provided matrix.
3. Initiate a recursive backtracking algorithm (`backtrack()`) starting from the first node in the graph.
4. In the backtracking function, iterate through the neighbors of the current node.
5. If a neighbor has not been visited in the current path, append it to the path and recurse.
6. If the length of the path equals the total number of vertices in the graph, check if an edge exists between the last node in the path and the starting node.
7. If the closing edge exists, a Hamiltonian Circuit has been found; append it to the list of valid circuits.
8. Backtrack by removing the last node and exploring other branches.
9. Collect and print all discovered Hamiltonian Circuits, and visualize them sequentially.