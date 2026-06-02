import streamlit as st
import time
import networkx as nx
from graphs.core import create_graph, draw_weighted_graph, validate_matrix, GraphError
from utils.ui import get_adjacency_matrix_input

def execute(matrix):
    """Core logic for Experiment 2 (Minimum Spanning Tree)."""
    # Validation allows weights > 1
    validate_matrix(matrix, is_weighted=True)
    
    # We treat 0 as 'no edge' in adjacency matrices for weighted graphs,
    # but networkx might treat 0 as an edge with weight 0 if we use from_numpy_array directly.
    # To be safe, let's build the graph manually or clean up zero-weight edges.
    G = create_graph(matrix, is_directed=False)
    
    # Remove edges with weight 0
    edges_to_remove = [(u, v) for u, v, d in G.edges(data=True) if d['weight'] == 0]
    G.remove_edges_from(edges_to_remove)
    
    if G.number_of_edges() == 0:
        raise GraphError("Graph is empty (no edges).")
        
    if not nx.is_connected(G):
        raise GraphError("Graph is disconnected. MST requires a connected graph.")
        
    # Calculate Minimum Spanning Tree
    MST = nx.minimum_spanning_tree(G, weight='weight')
    
    return G, MST

def show_output(G, MST):
    """Renders the output of Experiment 2."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Original Graph")
        fig1 = draw_weighted_graph(G)
        st.pyplot(fig1)
        
        total_weight_original = sum(d['weight'] for u, v, d in G.edges(data=True))
        st.write(f"**Total Edge Weight (Original):** {total_weight_original}")
        
    with col2:
        st.markdown("### Minimum Spanning Tree")
        fig2 = draw_weighted_graph(MST)
        st.pyplot(fig2)
        
        total_weight_mst = sum(d['weight'] for u, v, d in MST.edges(data=True))
        st.write(f"**Total Edge Weight (MST):** {total_weight_mst}")

def render():
    st.title("Graph Theory Laboratory")
    st.header("Experiment 2")
    st.subheader("Minimum Spanning Tree (Weighted Graphs)")
    st.markdown("**Aim:** To find the Minimum Spanning Tree (MST) of a weighted undirected graph and compare its total weight with the original graph.")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Theory", "Algorithm", "Code", "Run Experiment", "Output"])
    
    with tab1:
        st.markdown("### Theory")
        with st.container(height=400):
            st.markdown("""
            **Weighted Graphs**
            A weighted graph is a graph in which a number (the weight) is assigned to each edge. Such weights might represent costs, lengths, or capacities, depending on the problem.
            
            **Minimum Spanning Tree (MST)**
            A minimum spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
            
            Common algorithms to find the MST include Kruskal's algorithm and Prim's algorithm.
            """)
            
    with tab2:
        st.markdown("### Algorithm")
        st.markdown("""
        1. Start
        2. Accept the number of vertices $N$ from the user.
        3. Accept the $N \\times N$ weighted adjacency matrix (where 0 indicates no edge).
        4. Validate the matrix (check dimensions, verify diagonal is 0).
        5. Construct the weighted graph using NetworkX.
        6. Compute the Minimum Spanning Tree using `nx.minimum_spanning_tree`.
        7. Calculate the sum of weights for both the original graph and the MST.
        8. Plot both graphs using Matplotlib with edge labels.
        9. Stop
        """)
        
    with tab3:
        st.markdown("### Source Code")
        code = '''import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def calculate_mst(matrix):
    # Construct Graph
    G = nx.from_numpy_array(np.array(matrix))
    
    # Clean zero-weight edges (assuming 0 means no edge)
    edges_to_remove = [(u, v) for u, v, d in G.edges(data=True) if d['weight'] == 0]
    G.remove_edges_from(edges_to_remove)
    
    # Calculate MST
    MST = nx.minimum_spanning_tree(G, weight='weight')
    
    return G, MST
'''
        st.code(code, language='python')
        
    with tab4:
        st.markdown("### Run Experiment")
        num_vertices = st.number_input("Number of vertices:", min_value=2, max_value=15, value=4, step=1, key="exp2_vertices")
        st.info("Enter edge weights. Leave as 0 for no edge.")
        matrix = get_adjacency_matrix_input(num_vertices)
        
        if st.button("Execute", type="primary", key="exp2_execute"):
            with st.spinner("Executing Experiment..."):
                time.sleep(0.5) # Simulate execution time
                try:
                    # Execute logic and store result in session state
                    G, MST = execute(matrix)
                    st.session_state['exp2_result'] = (G, MST)
                    st.success("Execution completed! Check the Output tab.")
                except GraphError as e:
                    st.error(f"Error: {str(e)}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")
            
    with tab5:
        st.markdown("### Output")
        if 'exp2_result' in st.session_state:
            G, MST = st.session_state['exp2_result']
            show_output(G, MST)
        else:
            st.info("Execute the experiment in the 'Run Experiment' tab to see the output here.")
