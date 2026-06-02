def run():
    import math
    import matplotlib.pyplot as plt
    import networkx as nx

    def create_graph():
        G = nx.Graph()
        edges = [
            ('s', 'a', 18),
            ('s', 'c', 15),
            ('a', 'c', 6),
            ('a', 'b', 9),
            ('c', 'd', 7),
            ('b', 'd', 10),
            ('c', 'b', 14),
            ('b', 'f', 28),
            ('d', 'f', 36)
        ]
        G.add_weighted_edges_from(edges)
        return G

    def dijkstra_steps(G, source):
        dist = {node: float('inf') for node in G.nodes()}
        dist[source] = 0
        visited = set()
        steps = []

        while len(visited) < len(G.nodes()):
            u = None
            min_dist = float('inf')
            for node in G.nodes():
                if node not in visited and dist[node] < min_dist:
                    min_dist = dist[node]
                    u = node
            if u is None:
                break

            visited.add(u)
            changed_edges = []

            for v in G.neighbors(u):
                w = G[u][v]['weight']
                if v not in visited:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        changed_edges.append((u, v))

            steps.append((visited.copy(), dist.copy(), u, changed_edges))

        return steps, dist

    def draw_step(ax, G, pos, visited, dist, current, changed_edges, step):
        nx.draw_networkx_edges(G, pos, edge_color="gray", ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=changed_edges, edge_color="red", width=2, ax=ax)
        nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=800, ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color="orange", ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=[current], node_color="blue", ax=ax)
        nx.draw_networkx_labels(G, pos, ax=ax)

        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

        for node, (x, y) in pos.items():
            val = "∞" if dist[node] == float('inf') else str(dist[node])
            ax.text(x, y + 0.3, val, ha='center', color="green")

        ax.set_title("Step " + str(step) + " (" + str(current) + ")", fontsize=10)
        ax.axis("off")

    def show_steps(G, steps, dist, source):
        pos = {
            's': (0, 3),
            'c': (-2, 1),
            'a': (2, 1),
            'd': (-2, -1),
            'b': (2, -1),
            'f': (0, -3)
        }

        total = len(steps)
        cols = 3
        rows = math.ceil(total / cols)

        fig = plt.figure(figsize=(16, 10))

        # LEFT SIDE → GRAPHS
        for i in range(total):
            ax = plt.subplot2grid((rows, cols + 1), (i // cols, i % cols))
            visited, dist_step, current, changed_edges = steps[i]
            draw_step(ax, G, pos, visited, dist_step, current, changed_edges, i + 1)

        # RIGHT SIDE → TABLE (FULL HEIGHT)
        ax_table = plt.subplot2grid((rows, cols + 1), (0, cols), rowspan=rows)
        ax_table.axis('off')

        paths = nx.single_source_dijkstra_path(G, source)

        table_data = []
        for node in G.nodes():
            path = " → ".join(paths[node])
            cost = dist[node]
            table_data.append([f"{source} → {node}", path, cost])

        table = ax_table.table(
            cellText=table_data,
            colLabels=["From → To", "Path", "Cost"],
            loc='center'
        )

        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 2)

        ax_table.set_title("Shortest Paths (Dijkstra)", fontsize=12)

        plt.subplots_adjust(wspace=0.3, hspace=0.4)
        plt.show()

    G = create_graph()
    steps, final_dist = dijkstra_steps(G, 's')
    show_steps(G, steps, final_dist, 's')
