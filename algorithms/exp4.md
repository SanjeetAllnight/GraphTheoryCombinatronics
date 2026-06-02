# Algorithm

1. Read an input sequence of integers representing the target degree sequence of a graph.
2. Initialize an empty graph and a data structure to track nodes and their remaining required degrees.
3. Begin an iterative process: sort the current sequence in descending order of remaining degrees.
4. Check termination conditions: if all degrees are 0, construction is complete. If the highest degree exceeds the number of available nodes, or if any required degree becomes negative, the sequence is not graphical (halt).
5. Select the node with the highest degree $d$ and connect it to the next $d$ nodes in the sorted list.
6. Decrement the remaining degree requirement of those $d$ connected nodes by 1.
7. Record the current state of the graph and the remaining degree sequence.
8. Repeat the process until the graph is fully constructed or a violation is found.
9. Visually render the step-by-step construction of the graph, displaying the remaining sequence at each step.