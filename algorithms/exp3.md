# Algorithm

1. Create a base undirected graph $G$ and populate it with nodes (A to I) and a predefined set of edges.
2. Define a Spanning Subgraph by explicitly copying all nodes from $G$ but only adding a specific subset of its edges.
3. Generate an Induced Subgraph by selecting a specific subset of nodes ("C", "D", "E", "G", "I") and using `G.subgraph()` to preserve all existing edges between those nodes.
4. Generate an Edge-Induced Subgraph by selecting a specific subset of edges and using `G.edge_subgraph()` to include only those edges and their incident nodes.
5. Define manual coordinate positions for the nodes to ensure consistent visualization.
6. Plot the original graph alongside the spanning, induced, and edge-induced subgraphs in a 2x2 layout for visual comparison.