def run():
    import networkx as nx
    import matplotlib.pyplot as plt
    from itertools import combinations
    from collections import Counter
    G1 = nx.Graph()
    G1.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0)])
    G1.add_edges_from([(5,6),(6,7),(7,8),(8,9),(9,5)])
    G1.add_edges_from([(0,5),(1,6),(2,7),(3,8),(4,9)])
    G2 = nx.Graph()
    G2.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0)])
    G2.add_edges_from([(0,5),(1,6),(2,7),(3,9),(4,8)])
    G2.add_edges_from([(5,6),(6,9),(9,8),(8,7),(7,5)])
    p1 = {
    0:(-2.8,2.8),1:(2.8,2.8),2:(4.2,0),3:(0,-3.2),4:(-4.2,0),
    5:(-1.8,1.4),6:(1.8,1.4),7:(2.2,-0.6),8:(0,-1.8),9:(-2.2,-0.6)
    }
    p2 = {
    0:(-2.8,2.8),1:(2.8,2.8),2:(4.2,0),3:(0,-3.2),4:(-4.2,0),
    5:(-1.8,1.4),6:(1.5,1.4),7:(2.2,-0.2),8:(-1.8,-0.2),9:(0,-2.0)
    }
    def path_len_hist(G):
        c = Counter()
        for n in G.nodes():
            d = nx.single_source_shortest_path_length(G,n)
            for v in d.values():
                c[v] += 1
        return dict(sorted(c.items()))
    def kcycles(G,k):
        x = 0
        for s in combinations(G.nodes(),k):
            H = G.subgraph(s)
            if nx.is_connected(H) and H.number_of_edges()==k:
                x += 1
        return x
    def format_comparison_table(title, rows):
        lines = [title, f"{'Metric':<12}{'Graph 1':>10}{'Graph 2':>10}", "-" * 32]
        for label, g1_value, g2_value in rows:
            lines.append(f"{label:<12}{g1_value:>10}{g2_value:>10}")
        return "\n".join(lines)
    L1 = path_len_hist(G1)
    L2 = path_len_hist(G2)
    t41 = kcycles(G1,4)
    t42 = kcycles(G2,4)
    t51 = kcycles(G1,5)
    t52 = kcycles(G2,5)
    m = nx.isomorphism.GraphMatcher(G1,G2)
    ok = m.is_isomorphic()
    mp = m.mapping if ok else {}
    r = "ISOMORPHIC" if ok else "NOT ISOMORPHIC"
    length_rows = [(f"Length {k}", L1.get(k,0), L2.get(k,0)) for k in sorted(set(L1) | set(L2))]
    cycle_rows = [("4-cycles", t41, t42), ("5-cycles", t51, t52)]
    fig = plt.figure(figsize=(12,8), facecolor="#f4f7f9")
    grid = fig.add_gridspec(2,2, height_ratios=[4.4,1.8], hspace=0.08, wspace=0.14)
    fig.subplots_adjust(top=0.86, bottom=0.07, left=0.06, right=0.94)
    ax1 = fig.add_subplot(grid[0,0])
    ax2 = fig.add_subplot(grid[0,1])
    ax_info = fig.add_subplot(grid[1,:])
    draw_style = dict(
        with_labels=True,
        node_size=850,
        node_color="#2f6ea7",
        edgecolors="white",
        linewidths=1.6,
        width=1.4,
        font_color="white",
        font_weight="bold"
    )
    nx.draw(G1,p1,ax=ax1,**draw_style)
    ax1.set_title("Graph 1", fontsize=17, fontweight="bold", pad=10)
    ax1.set_axis_off()
    nx.draw(G2,p2,ax=ax2,**draw_style)
    ax2.set_title("Graph 2", fontsize=17, fontweight="bold", pad=10)
    ax2.set_axis_off()
    ax_info.set_axis_off()
    panel_style = dict(boxstyle="round,pad=0.65", facecolor="white", edgecolor="#cbd5e1", linewidth=1.4)
    ax_info.text(
        0.03, 0.90,
        format_comparison_table("Shortest-path length counts", length_rows),
        transform=ax_info.transAxes,
        ha="left", va="top",
        family="monospace", fontsize=11.2, color="#1f2937",
        bbox=panel_style
    )
    ax_info.text(
        0.58, 0.90,
        format_comparison_table("Cycle counts", cycle_rows),
        transform=ax_info.transAxes,
        ha="left", va="top",
        family="monospace", fontsize=11.2, color="#1f2937",
        bbox=panel_style
    )
    mapping_text = f"Isomorphism map: {mp}" if ok else "No isomorphism mapping"
    ax_info.text(
        0.5, 0.12, mapping_text,
        transform=ax_info.transAxes,
        ha="center", va="bottom",
        fontsize=11.5, color="#334155"
    )
    fig.suptitle(r, fontsize=20, fontweight="bold", y=0.975, color="#0f172a")
    plt.show()
