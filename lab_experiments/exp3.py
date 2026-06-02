def run():
    import matplotlib.pyplot as plt
    import networkx as nx
    G = nx.Graph()
    nodes = ["A","B","C","D","E","F","G","H","I"]
    G.add_nodes_from(nodes)
    edges = [
        ("A","B"),("A","C"),("A","D"),
        ("B","F"),("B","H"),
        ("C","D"),("C","G"),("C","I"),
        ("D","E"),("D","G"),
        ("E","F"),("E","G"),
        ("F","H"),
        ("G","I"),
        ("H","I")
    ]
    for e in edges:
        G.add_edge(e[0], e[1])
    pos = {}
    pos["A"] = (0.0,4.4)
    pos["B"] = (5.3,3.2)
    pos["C"] = (-3.2,0.8)
    pos["D"] = (-0.6,1.8)
    pos["E"] = (1.0,0.7)
    pos["F"] = (3.8,0.7)
    pos["G"] = (-0.6,-0.2)
    pos["H"] = (5.3,-2.8)
    pos["I"] = (-0.7,-3.6)
    spanning_subgraph = nx.Graph()
    spanning_subgraph.add_nodes_from(nodes)
    sp_edges = [
        ("A","B"),("A","C"),("A","D"),
        ("D","E"),("E","F"),
        ("F","H"),("H","I"),("I","G")
    ]
    for e in sp_edges:
        spanning_subgraph.add_edge(e[0], e[1])
    induced_nodes = ["C","D","E","G","I"]
    induced_subgraph = G.subgraph(induced_nodes).copy()
    edge_induced_edges = [
        ("A","D"),("C","D"),
        ("D","E"),("E","F"),
        ("F","H"),("G","I")
    ]
    edge_induced_subgraph = G.edge_subgraph(edge_induced_edges).copy()
    fig, ax = plt.subplots(2,2, figsize=(13,10))
    nx.draw(G, pos,with_labels=True,node_size=180,node_color="#a7b8c9",edge_color="#5a5a5a",font_size=16,font_weight="bold",width=1.6,ax=ax[0,0])
    ax[0,0].set_title("Original graph")
    ax[0,0].axis("off")
    nx.draw(spanning_subgraph, pos,with_labels=True,node_size=180,node_color="#b8d8b8",edge_color="#2f6f2f",font_size=16,font_weight="bold",width=1.8,ax=ax[0,1])
    ax[0,1].set_title("Spanning subgraph")
    ax[0,1].axis("off")
    nx.draw(induced_subgraph, pos,with_labels=True,node_size=180,node_color="#d7c9a2",edge_color="#6f5a2f",font_size=16,font_weight="bold",width=1.8,ax=ax[1,0])
    ax[1,0].set_title("Induced subgraph")
    ax[1,0].axis("off")
    nx.draw(edge_induced_subgraph, pos,
            with_labels=True,
            node_size=180,
            node_color="#d1b5d8",
            edge_color="#5b2f6f",
            font_size=16,
            font_weight="bold",
            width=1.8,
            ax=ax[1,1])
    ax[1,1].set_title("Edge-induced subgraph")
    ax[1,1].axis("off")
    plt.tight_layout()
    plt.show()