import os

algos = {
    "exp1": """# Algorithm

1. Initialize a Matplotlib figure with a 2x3 grid of subplots.
2. Generate a Complete Graph with 6 nodes using `nx.complete_graph()` and draw it using `nx.circular_layout()`.
3. Generate a Cycle Graph with 8 nodes using `nx.cycle_graph()` and draw it using `nx.circular_layout()`.
4. Generate a Complete Bipartite Graph with partitions of size 3 and 4 using `nx.complete_bipartite_graph()` and draw it using `nx.bipartite_layout()`.
5. Generate a Wheel Graph with 6 nodes using `nx.wheel_graph()` and draw it by manually computing circular coordinates for the rim nodes around the central node.
6. Generate a Path Graph with 5 nodes using `nx.path_graph()` and draw it horizontally.
7. Generate a Null Graph with 5 nodes using `nx.empty_graph()` and draw it horizontally.
8. Render all subplots to the screen.""",

    "exp2": """# Algorithm

1. Manually construct Graph 1 (`G1`) and Graph 2 (`G2`) by defining their edge connections.
2. Compute the shortest-path length distribution for both graphs by calculating the shortest path from every node to every other node.
3. Count the number of 4-cycles and 5-cycles in both graphs by iterating through all node combinations of size $k$ and checking if the induced subgraph is connected and has exactly $k$ edges.
4. Use `nx.isomorphism.GraphMatcher(G1, G2)` to verify if the two graphs are structurally isomorphic.
5. If isomorphic, extract the specific node-to-node mapping.
6. Format the path lengths and cycle counts into comparison tables.
7. Render both graphs visually side-by-side alongside the statistical tables and the isomorphism result.""",

    "exp3": """# Algorithm

1. Create a base undirected graph $G$ and populate it with nodes (A to I) and a predefined set of edges.
2. Define a Spanning Subgraph by explicitly copying all nodes from $G$ but only adding a specific subset of its edges.
3. Generate an Induced Subgraph by selecting a specific subset of nodes ("C", "D", "E", "G", "I") and using `G.subgraph()` to preserve all existing edges between those nodes.
4. Generate an Edge-Induced Subgraph by selecting a specific subset of edges and using `G.edge_subgraph()` to include only those edges and their incident nodes.
5. Define manual coordinate positions for the nodes to ensure consistent visualization.
6. Plot the original graph alongside the spanning, induced, and edge-induced subgraphs in a 2x2 layout for visual comparison.""",

    "exp4": """# Algorithm

1. Read an input sequence of integers representing the target degree sequence of a graph.
2. Initialize an empty graph and a data structure to track nodes and their remaining required degrees.
3. Begin an iterative process: sort the current sequence in descending order of remaining degrees.
4. Check termination conditions: if all degrees are 0, construction is complete. If the highest degree exceeds the number of available nodes, or if any required degree becomes negative, the sequence is not graphical (halt).
5. Select the node with the highest degree $d$ and connect it to the next $d$ nodes in the sorted list.
6. Decrement the remaining degree requirement of those $d$ connected nodes by 1.
7. Record the current state of the graph and the remaining degree sequence.
8. Repeat the process until the graph is fully constructed or a violation is found.
9. Visually render the step-by-step construction of the graph, displaying the remaining sequence at each step.""",

    "exp5": """# Algorithm

1. The script currently contains an empty implementation (`def run(): pass`).
2. The intended algorithm is to generate a Line Graph of a given base graph using the `networkx.line_graph()` function.
3. (Implementation pending in source code).""",

    "exp6": """# Algorithm

1. Read the number of vertices and a weighted adjacency matrix from the user.
2. Construct an undirected graph from the matrix, assigning the provided weights to edges.
3. Extract all edges from the graph and sort them in ascending order based on their weight.
4. Initialize an empty list for the Minimum Spanning Tree (MST) edges and a tracking variable for the total cost.
5. Iterate through the sorted edges and tentatively add each edge to a temporary graph.
6. Use `nx.is_forest()` to check if the newly added edge creates a cycle.
7. If a cycle is formed, remove the edge. Otherwise, permanently add the edge to the MST list, add its weight to the total cost, and record the step.
8. Stop the process when the number of edges in the MST equals the number of vertices minus one.
9. Render the step-by-step addition of edges visually.""",

    "exp7": """# Algorithm

1. Construct a predefined weighted undirected graph with nodes ('s', 'a', 'b', 'c', 'd', 'f') and their connecting edges.
2. Initialize the tentative distance to all nodes as infinity, except for the source node ('s') which is set to 0.
3. Create an empty set to track visited nodes.
4. Iteratively select the unvisited node with the smallest known tentative distance.
5. Mark the selected node as visited.
6. Iterate through all unvisited neighbors of the current node.
7. Calculate the tentative distance to each neighbor through the current node. If this new distance is less than the neighbor's currently recorded distance, update the distance.
8. Record the current state of the graph, including visited nodes, current distances, and updated edges.
9. Repeat the process until all reachable nodes have been visited.
10. Render the step-by-step execution visually alongside a table of the final shortest paths.""",

    "exp8": """# Algorithm

1. Create a predefined undirected graph with 5 vertices and 8 specific edges.
2. Define a **Closed Walk** by explicitly specifying a sequence of edges `[(1, 2), (2, 3), (3, 1)]` (starts and ends at the same vertex, repetition allowed).
3. Define a **Closed Path** (Cycle) by explicitly specifying a sequence of edges `[(1, 2), (2, 5), (5, 4), (4, 1)]` (starts and ends at the same vertex, no vertices or edges repeated).
4. Define a **Closed Trail** by explicitly specifying a sequence of edges `[(1, 3), (3, 2), (2, 5), (5, 4), (4, 3), (3, 1)]` (starts and ends at the same vertex, vertices may repeat but no edges are repeated).
5. Plot the original graph alongside three highlighted subgraphs showing the explicit edges used in the Walk, Path, and Trail.""",

    "exp9": """# Algorithm

1. Create a predefined undirected graph with 7 nodes and a specific set of edges.
2. Check if the graph contains an Eulerian circuit by using the `nx.is_eulerian()` function (which verifies that all vertices have an even degree and all edges belong to a single connected component).
3. If the graph is Eulerian, compute the exact sequence of edges forming the circuit using `nx.eulerian_circuit()`.
4. Extract the ordered list of vertices traversed in the circuit to form the path string.
5. If the graph is not Eulerian, return an empty circuit.
6. Plot the original graph next to a highlighted version showing the Eulerian circuit path (if one exists).""",

    "exp10": """# Algorithm

1. Read the number of vertices and an adjacency matrix from the user.
2. Construct an unweighted undirected graph from the provided matrix.
3. Initiate a recursive backtracking algorithm (`backtrack()`) starting from the first node in the graph.
4. In the backtracking function, iterate through the neighbors of the current node.
5. If a neighbor has not been visited in the current path, append it to the path and recurse.
6. If the length of the path equals the total number of vertices in the graph, check if an edge exists between the last node in the path and the starting node.
7. If the closing edge exists, a Hamiltonian Circuit has been found; append it to the list of valid circuits.
8. Backtrack by removing the last node and exploring other branches.
9. Collect and print all discovered Hamiltonian Circuits, and visualize them sequentially.""",

    "exp11": """# Algorithm

1. Create a predefined `MultiGraph` with 10 vertices and 19 edges, including multiple parallel edges (between nodes 8 and 9, and 9 and 10).
2. Compute the vertex coloring using `nx.coloring.greedy_color()` with the `saturation_largest_first` strategy, which corresponds exactly to the DSATUR algorithm.
3. Map the resulting integer color indices to a predefined dictionary of string colors (red, green, blue, yellow, orange, purple).
4. Separate standard single edges from parallel edges to render them differently (using curved `connectionstyle` arcs for parallel edges).
5. Draw the graph, applying the mapped colors to the nodes.
6. Print the exact color assigned to each vertex.
7. Compute and print the Chromatic Number by calculating the number of unique colors assigned by the DSATUR algorithm."""
}

os.makedirs('algorithms', exist_ok=True)
for exp, text in algos.items():
    with open(f"algorithms/{exp}.md", "w", encoding="utf-8") as f:
        f.write(text)
print("Algorithm markdown files generated successfully.")
