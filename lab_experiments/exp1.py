def run():
    import networkx as nx
    import matplotlib.pyplot as plt
    import math
    plt.figure()
    g1 = nx.complete_graph(6)
    plt.subplot(2,3,1)
    nx.draw(g1, nx.circular_layout(g1), with_labels=True, node_color="pink")
    plt.title("Complete Graph")
    g2 = nx.cycle_graph(8)
    plt.subplot(2,3,2)
    nx.draw(g2, nx.circular_layout(g2), with_labels=True, node_color="pink")
    plt.title("Cycle Graph")
    g3 = nx.complete_bipartite_graph(3,4)
    left = [0,1,2]
    plt.subplot(2,3,3)
    nx.draw(g3, nx.bipartite_layout(g3,left), with_labels=True, node_color="pink")
    plt.title("Complete Bipartite")
    g4 = nx.wheel_graph(6)
    rim_nodes = list(range(1, 6))
    pos4 = {0: (0, 0)}
    for i, node in enumerate(rim_nodes):
        theta = 2 * math.pi * i / len(rim_nodes)
        pos4[node] = (math.cos(theta), math.sin(theta))
    plt.subplot(2,3,4)
    nx.draw(g4, pos4, with_labels=True, node_color="pink")
    plt.title("Wheel Graph")
    g5 = nx.path_graph(5)
    pos5 = {i:(i,0) for i in range(5)}
    plt.subplot(2,3,5)
    nx.draw(g5, pos5, with_labels=True, node_color="pink")
    plt.title("Path Graph")
    g6 = nx.empty_graph(5)
    pos6 = {i:(i,0) for i in range(5)}
    plt.subplot(2,3,6)
    nx.draw(g6, pos6, with_labels=True, node_color="pink")
    plt.title("Null Graph")
    plt.show()
