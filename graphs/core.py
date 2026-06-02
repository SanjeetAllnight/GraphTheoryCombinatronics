import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class GraphError(Exception):
    """Custom exception for graph-related errors."""
    pass

def validate_matrix(matrix, is_weighted=False):
    """
    Validates an adjacency matrix.
    Raises GraphError if invalid.
    """
    matrix = np.array(matrix)
    
    # 1. Check dimensions
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise GraphError("Invalid matrix: Matrix must be square.")
        
    n = matrix.shape[0]
    
    # 2. Check diagonal
    if not np.all(np.diag(matrix) == 0):
        raise GraphError("Invalid matrix: Diagonal values must be zero (no self-loops).")
        
    # 3. Check values for unweighted
    if not is_weighted:
        # Values should be 0 or 1
        if not np.all(np.isin(matrix, [0, 1])):
            raise GraphError("Invalid matrix: Unweighted graphs must only contain 0 or 1 in the matrix.")

def create_graph(matrix, is_directed=False):
    """
    Creates a NetworkX graph from a numpy adjacency matrix.
    """
    matrix = np.array(matrix)
    if is_directed:
        G = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
    else:
        G = nx.from_numpy_array(matrix, create_using=nx.Graph)
        
    return G

def draw_graph(G, ax=None):
    """
    Draws an unweighted static graph using Matplotlib.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    else:
        fig = ax.figure
        
    pos = nx.spring_layout(G, seed=42) # Fixed seed for stable layout
    
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=500, edgecolors='black')
    nx.draw_networkx_edges(G, pos, ax=ax, width=1.5, alpha=0.7)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_family='sans-serif')
    
    ax.set_axis_off()
    fig.tight_layout()
    return fig

def draw_weighted_graph(G, ax=None):
    """
    Draws a weighted static graph using Matplotlib, including edge labels.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 4))
    else:
        fig = ax.figure
        
    pos = nx.spring_layout(G, seed=42)
    
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightgreen', node_size=500, edgecolors='black')
    nx.draw_networkx_edges(G, pos, ax=ax, width=1.5, alpha=0.7)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=12, font_family='sans-serif')
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_size=10)
    
    ax.set_axis_off()
    fig.tight_layout()
    return fig

def display_matrix(matrix):
    """
    Returns a formatted string of the matrix for text output.
    """
    return str(np.array(matrix))
