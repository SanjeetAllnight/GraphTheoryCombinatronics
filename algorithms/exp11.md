# Algorithm

1. Create a predefined `MultiGraph` with 10 vertices and 19 edges, including multiple parallel edges (between nodes 8 and 9, and 9 and 10).
2. Compute the vertex coloring using `nx.coloring.greedy_color()` with the `saturation_largest_first` strategy, which corresponds exactly to the DSATUR algorithm.
3. Map the resulting integer color indices to a predefined dictionary of string colors (red, green, blue, yellow, orange, purple).
4. Separate standard single edges from parallel edges to render them differently (using curved `connectionstyle` arcs for parallel edges).
5. Draw the graph, applying the mapped colors to the nodes.
6. Print the exact color assigned to each vertex.
7. Compute and print the Chromatic Number by calculating the number of unique colors assigned by the DSATUR algorithm.