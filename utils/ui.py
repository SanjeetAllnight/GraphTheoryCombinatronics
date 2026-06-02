import streamlit as st
import pandas as pd
import numpy as np

def get_adjacency_matrix_input(num_vertices):
    """
    Dynamically generates a grid for adjacency matrix input using st.data_editor.
    """
    st.write("Adjacency Matrix:")
    
    # Initialize dataframe with zeros
    node_names = [f"V{i+1}" for i in range(num_vertices)]
    df = pd.DataFrame(
        np.zeros((num_vertices, num_vertices), dtype=int),
        columns=node_names,
        index=node_names
    )
    
    # Render as an editable dataframe
    edited_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=False,
        key=f"matrix_input_{num_vertices}"
    )
    
    return edited_df.to_numpy()
