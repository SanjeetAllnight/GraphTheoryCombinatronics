def run():
    import math
    import networkx as nx
    import matplotlib.pyplot as plt
    def create_graph(n, mat):
        G = nx.Graph()
        for i in range(n):
            G.add_node(i + 1)
        for i in range(n):
            for j in range(i + 1, n):
                if mat[i][j] == 1:
                    G.add_edge(i + 1, j + 1)
        return G
    def find_hamiltonian_circuits(G):
        n = len(G.nodes())
        circuits = []
        def backtrack(path):
            current = path[-1]
            if len(path) == n:
                if G.has_edge(path[-1], path[0]):
                    circuits.append(path + [path[0]])
                return
            for neighbor in G.neighbors(current):
                if neighbor not in path:
                    backtrack(path + [neighbor])
        start = list(G.nodes())[0]
        backtrack([start])
        return circuits
    def draw_circuit(ax, G, pos, circuit, step):
        nx.draw_networkx_nodes(
            G,
            pos,
            node_color="lightblue",
            edgecolors="black",
            node_size=800,
            ax=ax
        )
        nx.draw_networkx_edges(
            G,
            pos,
            edge_color="lightgray",
            ax=ax
        )
        path_edges = []
        for i in range(len(circuit) - 1):
            path_edges.append((circuit[i], circuit[i + 1]))
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            edge_color="red",
            width=3,
            ax=ax
        )
        nx.draw_networkx_labels(
            G,
            pos,
            font_weight="bold",
            ax=ax
        )
        title = " → ".join(map(str, circuit))
        ax.set_title(
            "Circuit " + str(step) + "\n" + title,
            fontsize=10
        )
        ax.axis("off")
    def show_circuits(G, circuits):
        if len(circuits) == 0:
            print("No Hamiltonian Circuit exists")
            return
        pos = nx.spring_layout(G, seed=42)
        total = len(circuits)
        cols = math.ceil(math.sqrt(total))
        rows = math.ceil(total / cols)
        fig, ax = plt.subplots(
            rows,
            cols,
            figsize=(5 * cols, 5 * rows)
        )
        if total == 1:
            ax = [ax]
        elif hasattr(ax, "flat"):
            ax = list(ax.flat)
        for i in range(total):
            draw_circuit(
                ax[i],
                G,
                pos,
                circuits[i],
                i + 1
            )
        for i in range(total, len(ax)):
            ax[i].remove()
        plt.tight_layout()
        plt.show()
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix:")
    mat = []
    for i in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    G = create_graph(n, mat)
    circuits = find_hamiltonian_circuits(G)
    if len(circuits) == 0:
        print("No Hamiltonian Circuit exists")
    else:
        print("\nHamiltonian Circuits:\n")
        for i, c in enumerate(circuits, start=1):
            print(
                "Circuit",
                i,
                ":",
                " -> ".join(map(str, c))
            )
        show_circuits(G, circuits)
