# strategies.py
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.lines as mlines

def optimiser_reseau_vaccination(G):
    pos = nx.spring_layout(G, seed=42)
    for u, v in G.edges():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        G[u][v]['weight'] = round(dist, 3)

    mst = nx.minimum_spanning_tree(G, weight='weight')

    edge_labels = nx.get_edge_attributes(mst, 'weight')
    plt.figure(figsize=(10, 7))
    plt.title("🧩 Réseau de vaccination optimal (MST)", fontsize=14)
    nx.draw(G, pos, with_labels=False, node_size=20, edge_color="lightgray")
    nx.draw(mst, pos, with_labels=False, node_size=20, edge_color="red", width=2)
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_size=8)

    total = sum(d['weight'] for _, _, d in mst.edges(data=True))
    plt.text(0.95, 0.02, f"Distance totale : {round(total,3)} km", ha='right', va='bottom',
             transform=plt.gcf().transFigure, fontsize=10,
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))
    plt.tight_layout()
    plt.show()

    print(f"\n📏 Distance totale parcourue : {round(total,3)} km")
    return mst


def simuler_flot_transmission(G, source, cible):
    Gd = nx.DiGraph()
    for u, v in G.edges():
        Gd.add_edge(u, v, capacity=1)
        Gd.add_edge(v, u, capacity=1)

    try:
        flot, flow_dict = nx.maximum_flow(Gd, source, cible)
        print(f"\n🚰 Flot maximum de {source} vers {cible} : {flot}")

        edges_actives = [(u, v) for u, voisins in flow_dict.items() for v, f in voisins.items() if f > 0]
        G_flot = nx.DiGraph()
        G_flot.add_edges_from(edges_actives)

        chemins = []
        def dfs(actuel, chemin):
            if actuel == cible:
                chemins.append(chemin[:])
                return
            for voisin in G_flot.successors(actuel):
                if voisin not in chemin:
                    chemin.append(voisin)
                    dfs(voisin, chemin)
                    chemin.pop()

        dfs(source, [source])

        for i, c in enumerate(chemins, 1):
            print(f"  Chemin {i}: {' → '.join(map(str, c))}")

        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(10, 7))
        plt.title(f"💧 Flot de {source} vers {cible} — Max = {flot}", fontsize=14)
        nx.draw(G, pos, with_labels=False, node_size=20, edge_color="lightgray")
        nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color="orange", node_size=100)
        nx.draw_networkx_nodes(G, pos, nodelist=[cible], node_color="blue", node_size=100)
        nx.draw_networkx_edges(G, pos, edgelist=edges_actives, edge_color="red", width=2)

        leg1 = mlines.Line2D([], [], color='orange', marker='o', linestyle='None', markersize=10, label='Source')
        leg2 = mlines.Line2D([], [], color='blue', marker='o', linestyle='None', markersize=10, label='Cible')
        leg3 = mlines.Line2D([], [], color='red', linewidth=2, label='Flot actif')
        plt.legend(handles=[leg1, leg2, leg3], loc="lower right")
        plt.tight_layout()
        plt.show()
        return flot

    except nx.NetworkXError:
        print(f"❌ Aucun chemin entre {source} et {cible}")
        return 0
