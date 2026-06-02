def run():
    import math
    import matplotlib.pyplot as plt
    import networkx as nx
    def create_graph(n, mat):
        G = nx.Graph()
        for i in range(n):
            G.add_node(i + 1)
        for i in range(n):
            for j in range(i + 1, n):
                if mat[i][j] != 0:
                    G.add_edge(i + 1, j + 1, weight=mat[i][j])
        return G
    def kruskal_steps(G):
        edges = sorted(G.edges(data=True), key=lambda x: x[2]["weight"])
        mst_edges = []
        steps = []
        cost = 0
        temp = nx.Graph()
        temp.add_nodes_from(G.nodes())
        for u, v, d in edges:
            temp.add_edge(u, v)
            if not nx.is_forest(temp):
                temp.remove_edge(u, v)
            else:
                mst_edges.append((u, v))
                cost += d["weight"]
                steps.append((mst_edges.copy(), cost))
            if len(mst_edges) == len(G.nodes()) - 1:
                break
        return steps, cost
    def draw_graph(ax, G, pos, mst_edges, step):
        nx.draw_networkx_nodes(
            G, pos,
            node_color="pink",
            edgecolors="black",
            node_size=800,
            ax=ax
        )
        nx.draw_networkx_edges(
            G, pos,
            edge_color="gray",
            ax=ax
        )
        nx.draw_networkx_edges(
            G, pos,
            edgelist=mst_edges,
            edge_color="red",
            width=2,
            ax=ax
        )
        nx.draw_networkx_labels(G, pos, ax=ax)
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
        ax.set_title("Step " + str(step))
        ax.axis("off")
    def show_steps(G, steps, cost):
        pos = nx.circular_layout(G)
        total = len(steps)
        cols = math.ceil(math.sqrt(total))
        rows = math.ceil(total / cols)
        fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
        if total == 1:
            axes = [axes]
        elif hasattr(axes, "flat"):
            axes = list(axes.flat)
        for i in range(total):
            draw_graph(axes[i], G, pos, steps[i][0], i + 1)
        for i in range(total, len(axes)):
            axes[i].remove()
        plt.suptitle("Total MST Cost = " + str(cost))
        plt.tight_layout()
        plt.show()
    n = int(input("Enter number of vertices: "))
    print("Enter weighted adjacency matrix:")
    mat = []
    for i in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    G = create_graph(n, mat)
    steps, cost = kruskal_steps(G)
    show_steps(G, steps, cost)
    print("Total MST cost =", cost)
