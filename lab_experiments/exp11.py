def run():
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.MultiGraph()
    edges = [
        (1,2),
        (1,3),
        (2,3),
        (2,4),
        (3,4),
        (2,5),
        (4,5),
        (3,6),
        (4,6),
        (5,6),
        (5,7),
        (6,7),
        (7,8),
        (7,9),
        (7,10),
        (8,9),
        (8,9),
        (9,10),
        (9,10)
    ]
    G.add_edges_from(edges)
    colors = nx.coloring.greedy_color(
        G,
        strategy="saturation_largest_first"
    )
    color_map = {
        0:"red",1:"green",2:"blue",3:"yellow",4:"orange",5:"purple"
    }
    node_colors = [
        color_map[colors[node]]
        for node in G.nodes()
    ]
    pos = {
        1:(-6,0),
        2:(-4,1),
        3:(-4,-1),
        4:(-2,0),
        5:(0,1),
        6:(0,-1),
        7:(2,0),
        8:(5,1.5),
        9:(5,0),
        10:(5,-1.5)
    }
    plt.figure(figsize=(12,6))
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        node_size=1200,
        edgecolors="black"
    )
    nx.draw_networkx_labels(
        G,
        pos,
        font_size=14,
        font_weight="bold",
        font_color="white"
    )
    normal_edges=[]
    parallel_89=[]
    parallel_910=[]
    for u,v,key in G.edges(keys=True):
        if (u,v)==(8,9) or (u,v)==(9,8):
            parallel_89.append((u,v))
        elif (u,v)==(9,10) or (u,v)==(10,9):
            parallel_910.append((u,v))
        else:
            normal_edges.append((u,v))
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=normal_edges,
        width=2
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=[(8,9)],
        width=2,
        connectionstyle="arc3,rad=.2"
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=[(8,9)],
        width=2,
        connectionstyle="arc3,rad=-.2"
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=[(9,10)],
        width=2,
        connectionstyle="arc3,rad=.2"
    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=[(9,10)],
        width=2,
        connectionstyle="arc3,rad=-.2"
    )
    print("\nVertex Colouring:\n")
    for node in G.nodes():
        print(
            "Vertex",
            node,
            "→",
            color_map[colors[node]].upper()
        )
    print("\nChromatic Number =",len(set(colors.values())))
    plt.title("Greedy Graph Colouring using DSATUR")
    plt.axis("off")
    plt.show()
