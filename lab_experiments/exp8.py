def run():
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()

    edges = [
        (1, 2), (2, 5), (5, 4), (4, 1),
        (1, 3), (2, 3), (4, 3), (5, 3)
    ]

    G.add_edges_from(edges)

    pos = {
        1: (-1, 1),
        2: (1, 1),
        4: (-1, -1),
        5: (1, -1),
        3: (0, 0)
    }

    closed_walk = [(1, 2), (2, 3), (3, 1)]
    closed_path = [(1, 2), (2, 5), (5, 4), (4, 1)]
    closed_trail = [(1, 3), (3, 2), (2, 5), (5, 4), (4, 3), (3, 1)]

    fig, ax = plt.subplots(2, 2, figsize=(10, 10))

    # Original Graph
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=800, ax=ax[0, 0])
    ax[0, 0].set_title("Original Graph")

    # Closed Walk (ONLY edges used)
    nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=800, ax=ax[0, 1])
    nx.draw_networkx_labels(G, pos, ax=ax[0, 1])
    nx.draw_networkx_edges(G, pos, edgelist=closed_walk, edge_color="red", width=2, ax=ax[0, 1])
    ax[0, 1].set_title("Closed Walk")

    # Closed Path (ONLY edges used)
    nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=800, ax=ax[1, 0])
    nx.draw_networkx_labels(G, pos, ax=ax[1, 0])
    nx.draw_networkx_edges(G, pos, edgelist=closed_path, edge_color="green", width=2, ax=ax[1, 0])
    ax[1, 0].set_title("Closed Path")

    # Closed Trail (ONLY edges used)
    nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=800, ax=ax[1, 1])
    nx.draw_networkx_labels(G, pos, ax=ax[1, 1])
    nx.draw_networkx_edges(G, pos, edgelist=closed_trail, edge_color="purple", width=2, ax=ax[1, 1])
    ax[1, 1].set_title("Closed Trail")

    for i in range(2):
        for j in range(2):
            ax[i, j].axis("off")

    plt.tight_layout()
    plt.show()
