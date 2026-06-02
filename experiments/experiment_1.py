import streamlit as st
import time
import networkx as nx
from graphs.core import create_graph, draw_graph, validate_matrix, GraphError, display_matrix
from utils.ui import get_adjacency_matrix_input

def execute(matrix):
    """Core logic for Experiment 1."""
    validate_matrix(matrix, is_weighted=False)
    G = create_graph(matrix, is_directed=False)
    
    if G.number_of_edges() == 0:
        raise GraphError("Graph is empty (no edges).")
        
    if not nx.is_connected(G):
        raise GraphError("Graph is disconnected. This experiment requires a connected graph.")
        
    return G

def show_output(G):
    """Renders the output of Experiment 1."""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Graph Properties")
        st.write(f"**Vertices (N):** {G.number_of_nodes()}")
        st.write(f"**Edges (M):** {G.number_of_edges()}")
        st.write(f"**Average Degree:** {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")
        
        st.markdown("### Degree Sequence")
        degrees = [d for n, d in G.degree()]
        st.write(degrees)
        
    with col2:
        st.markdown("### Graph Visualization")
        fig = draw_graph(G)
        st.pyplot(fig)

def render():
    st.title("Graph Theory Laboratory")
    st.header("Experiment 1")
    st.subheader("Introduction to Graphs and Degree Calculation")
    st.markdown("**Aim:** To construct an unweighted undirected graph from an adjacency matrix and calculate its basic properties including node degrees.")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Theory", "Algorithm", "Code", "Run Experiment", "Output"])
    
    with tab1:
        st.markdown("### Theory")
        with st.container(height=400):
            st.markdown("""
            **Adjacency Matrix**
            An adjacency matrix is a square matrix used to represent a finite graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.
            
            **Degree of a Vertex**
            In an undirected graph, the degree of a vertex is the number of edges incident to it. A loop (if allowed) contributes 2 to the degree of the vertex.
            
            For a graph $G = (V, E)$, the degree of vertex $v \in V$ is denoted as $deg(v)$.
            
            By the Handshaking Lemma, the sum of all degrees is twice the number of edges:
            $\sum_{v \in V} deg(v) = 2|E|$
            """)
            
    with tab2:
        st.markdown("### Algorithm")
        st.markdown("""
        1. Start
        2. Accept the number of vertices $N$ from the user.
        3. Accept the $N \\times N$ adjacency matrix.
        4. Validate the matrix (check dimensions, verify diagonal is 0, verify entries are 0 or 1).
        5. Construct the graph using NetworkX.
        6. Compute the number of edges and the degree of each vertex.
        7. Plot the graph using Matplotlib.
        8. Stop
        """)
        
    with tab3:
        st.markdown("### Source Code")
        code = '''import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def calculate_graph_properties(matrix):
    # Construct Graph
    G = nx.from_numpy_array(np.array(matrix))
    
    # Calculate properties
    nodes = G.number_of_nodes()
    edges = G.number_of_edges()
    degrees = dict(G.degree())
    
    return G, nodes, edges, degrees
'''
        st.code(code, language='python')
        
    with tab4:
        st.markdown("### Run Experiment")
        num_vertices = st.number_input("Number of vertices:", min_value=2, max_value=15, value=4, step=1)
        matrix = get_adjacency_matrix_input(num_vertices)
        
        if st.button("Execute", type="primary"):
            with st.spinner("Executing Experiment..."):
                time.sleep(0.5) # Simulate execution time
                try:
                    # Execute logic and store result in session state
                    G = execute(matrix)
                    st.session_state['exp1_result'] = G
                    st.success("Execution completed! Check the Output tab.")
                except GraphError as e:
                    st.error(f"Error: {str(e)}")
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")
            
    with tab5:
        st.markdown("### Output")
        if 'exp1_result' in st.session_state:
            show_output(st.session_state['exp1_result'])
        else:
            st.info("Execute the experiment in the 'Run Experiment' tab to see the output here.")
