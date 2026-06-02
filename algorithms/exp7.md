# Algorithm

1. Construct a predefined weighted undirected graph with nodes ('s', 'a', 'b', 'c', 'd', 'f') and their connecting edges.
2. Initialize the tentative distance to all nodes as infinity, except for the source node ('s') which is set to 0.
3. Create an empty set to track visited nodes.
4. Iteratively select the unvisited node with the smallest known tentative distance.
5. Mark the selected node as visited.
6. Iterate through all unvisited neighbors of the current node.
7. Calculate the tentative distance to each neighbor through the current node. If this new distance is less than the neighbor's currently recorded distance, update the distance.
8. Record the current state of the graph, including visited nodes, current distances, and updated edges.
9. Repeat the process until all reachable nodes have been visited.
10. Render the step-by-step execution visually alongside a table of the final shortest paths.