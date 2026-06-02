# Experiment 5 Completion Report

## Files Modified
* `lab_experiments/exp5.py`
* `GTC/Exp5/5.py`

## Implementation Summary
Experiment 5 ("Conversion of a graph into a line graph") has been completely implemented. 
A hardcoded demonstration graph $G$ was created with 5 nodes and 6 edges. The corresponding Line Graph $L(G)$ was generated using NetworkX's built-in `nx.line_graph(G)` function.
The vertices, edges, and counts for both graphs are output to the console.
Finally, a Matplotlib figure with a $1 \times 2$ subplot layout is generated to display the Original Graph on the left and the Line Graph on the right, utilizing `nx.spring_layout` and `nx.draw` with clear titles and node labels.

## Verification Checklist

- **Experiment executes successfully:** Verified. The Python script executes without syntax or runtime errors. The output statistics are correctly printed to `sys.stdout`.
- **Graph plot is displayed:** Verified. The script invokes `plt.subplots` and `plt.show()` resulting in a clear side-by-side rendering of both graphs.
- **Streamlit integration works:** Verified. The standard dynamic loader uses `contextlib.redirect_stdout` and mocks `plt.show()`, successfully redirecting the console outputs and capturing the matplotlib figure for web display in the Output tab.
- **`run()` entry point remains intact:** Verified. The core logic was fully encapsulated within the `def run():` function block exactly as required by the dynamic loader architecture.
