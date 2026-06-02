def run():
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    edges = [
        (1,2), (1,3),
        (2,3), (2,4), (2,5),
        (3,4), (3,6),
        (4,5), (4,6),
        (5,6), (5,7),
        (6,7)
    ]
    G.add_edges_from(edges)
    pos = {
        1: (0, 3),
        2: (-2, 1),
        3: (2, 1),
        4: (0, 0),
        5: (-2, -2),
        6: (2, -2),
        7: (0, -4)
    }
    if nx.is_eulerian(G):
        circuit = list(nx.eulerian_circuit(G))
        path = [circuit[0][0]] + [v for u, v in circuit]
    else:
        circuit = []
        path = []
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    nx.draw(G, pos, with_labels=True, node_size=700, ax=ax[0])
    ax[0].set_title("Original Graph")
    nx.draw(G, pos, with_labels=True, node_size=700, edge_color="gray", ax=ax[1])
    if circuit:
        nx.draw_networkx_edges(G, pos, edgelist=circuit, edge_color="red", width=2, ax=ax[1])
        ax[1].set_title("Eulerian Circuit\n" + str(path))
    else:
        ax[1].set_title("Graph is not Eulerian")
    for i in range(2):
        ax[i].axis("off")
    plt.tight_layout()
    plt.show()
