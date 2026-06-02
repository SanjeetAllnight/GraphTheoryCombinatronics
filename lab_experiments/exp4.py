def run():
    import math
    import textwrap
    import matplotlib.pyplot as plt
    import networkx as nx
    def make_graph(seq):
        names = []
        for i in range(len(seq)):
            names.append("V" + str(i + 1))
        G = nx.Graph()
        G.add_nodes_from(names)
        data = []
        for i in range(len(seq)):
            data.append([names[i], seq[i]])
        steps = []
        while True:
            data.sort(key=lambda x: x[1], reverse=True)
            done = True
            for x in data:
                if x[1] != 0:
                    done = False
                    break
            if done:
                break
            node = data[0][0]
            d = data[0][1]
            if d >= len(data):
                print("Degree sequence is not graphical")
                return None, None
            new_data = []
            new_data.append([node, 0])
            for i in range(1, len(data)):
                n = data[i][0]
                deg = data[i][1]
                if i <= d:
                    if deg == 0:
                        print("Degree sequence is not graphical")
                        return None, None
                    G.add_edge(node, n)
                    deg = deg - 1
                if deg < 0:
                    print("Degree sequence is not graphical")
                    return None, None
                new_data.append([n, deg])
            data = new_data
            rem = []
            for x in data:
                if x[1] > 0:
                    rem.append(x[1])
            if rem == []:
                rem = [0]
            steps.append([G.copy(), rem])
        return G, steps
    def draw_one(ax, G, pos, step, rem):
        nx.draw_networkx_nodes(
            G, pos,
            node_color="pink",
            edgecolors="black",
            node_size=900,
            ax=ax
        )
        nx.draw_networkx_edges(
            G, pos,
            edge_color="black",
            ax=ax
        )
        nx.draw_networkx_labels(
            G, pos,
            font_weight="bold",
            ax=ax
        )
        seq_text = "[" + ", ".join(str(x) for x in rem) + "]"
        rem_text = textwrap.fill(
            "Remaining sequence: " + seq_text,
            width=28,
            break_long_words=False
        )
        ax.set_title("Step " + str(step), fontsize=15, pad=26)
        ax.text(
            0.5,
            1.03,
            rem_text,
            transform=ax.transAxes,
            ha="center",
            va="bottom",
            fontsize=11,
            linespacing=1.25
        )
        ax.margins(x=0.18, y=0.22)
        ax.axis("off")
    def show_steps(G, steps):
        if steps is None:
            return
        pos = nx.circular_layout(G)
        total = len(steps)
        cols = math.ceil(math.sqrt(total))
        rows = math.ceil(total / cols)
        fig, ax = plt.subplots(
            rows,
            cols,
            figsize=(6 * cols, 5 * rows),
            constrained_layout=True
        )
        fig.set_constrained_layout_pads(
            w_pad=0.05,
            h_pad=0.08,
            wspace=0.08,
            hspace=0.12
        )
        if total == 1:
            ax = [ax]
        elif hasattr(ax, "flat"):
            ax = list(ax.flat)

        for i in range(total):
            draw_one(ax[i], steps[i][0], pos, i + 1, steps[i][1])

        for i in range(total, len(ax)):
            ax[i].remove()
        plt.show()
    seq = list(map(int, input("Enter degree sequence separated by space: ").split()))
    G, steps = make_graph(seq)
    show_steps(G, steps)

