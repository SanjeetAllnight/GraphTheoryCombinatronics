def run():
    import networkx as nx
    import matplotlib.pyplot as plt

    # Create original graph
    G = nx.Graph()
    edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)]
    G.add_edges_from(edges)

    # Generate line graph
    L = nx.line_graph(G)

    # Print output statistics
    print("Original Graph:")
    print("Vertices:", list(G.nodes()))
    print("Edges:", list(G.edges()))
    print("Number of Vertices:", G.number_of_nodes())
    print("Number of Edges:", G.number_of_edges())
    
    print("\nLine Graph L(G):")
    print("Vertices:", list(L.nodes()))
    print("Edges:", list(L.edges()))
    print("Number of Vertices:", L.number_of_nodes())
    print("Number of Edges:", L.number_of_edges())

    # Display side-by-side
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Draw Original Graph
    pos_G = nx.spring_layout(G, seed=42)
    nx.draw(
        G, pos_G,
        with_labels=True,
        node_color="skyblue",
        node_size=800,
        edge_color="gray",
        font_weight="bold",
        ax=ax[0]
    )
    ax[0].set_title("Original Graph", fontsize=15)

    # Draw Line Graph
    pos_L = nx.spring_layout(L, seed=42)
    nx.draw(
        L, pos_L,
        with_labels=True,
        node_color="lightgreen",
        node_size=800,
        edge_color="gray",
        font_weight="bold",
        ax=ax[1]
    )
    ax[1].set_title("Line Graph L(G)", fontsize=15)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run()
