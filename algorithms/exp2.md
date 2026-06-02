# Algorithm

1. Manually construct Graph 1 (`G1`) and Graph 2 (`G2`) by defining their edge connections.
2. Compute the shortest-path length distribution for both graphs by calculating the shortest path from every node to every other node.
3. Count the number of 4-cycles and 5-cycles in both graphs by iterating through all node combinations of size $k$ and checking if the induced subgraph is connected and has exactly $k$ edges.
4. Use `nx.isomorphism.GraphMatcher(G1, G2)` to verify if the two graphs are structurally isomorphic.
5. If isomorphic, extract the specific node-to-node mapping.
6. Format the path lengths and cycle counts into comparison tables.
7. Render both graphs visually side-by-side alongside the statistical tables and the isomorphism result.