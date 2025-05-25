import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.lines as mlines



# --- Fonction 18 — Optimisation d’un réseau de vaccination mobile à moindre coût. ---
def optimiser_reseau_vaccination(G):
    """
    Calcule et affiche l’arbre couvrant minimal (MST) basé sur les distances entre patients.
    Retourne aussi la distance totale parcourue.
    """
    
    pos = nx.spring_layout(G, seed=42)
    # Ajouter la vraie distance comme poids
    for u, v in G.edges():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        G[u][v]['weight'] = round(dist, 3)

    # Calcul du MST
    mst = nx.minimum_spanning_tree(G, weight='weight')

    # Visualisation
    edge_labels = nx.get_edge_attributes(mst, 'weight')
    
    fig = plt.figure(figsize=(10, 7))
    
    def on_key(event):
        if event.key == 'escape':
            plt.close(fig)
            
    fig.canvas.mpl_connect('key_press_event', on_key)
    
    plt.title("Réseau de vaccination optimal (MST)", fontsize=14)
    
    # Graphe original (gris)
    nx.draw(G, pos, with_labels=False, node_size=20, edge_color="lightgray")
    
    # MST en rouge
    nx.draw(mst, pos, with_labels=False, node_size=20, edge_color="red", width=2)
    
    # Affichage des poids
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_size=8)

    # 📊 Affichage des arêtes retenues + distance totale
    distance_totale = 0
    print("\nArêtes retenues dans le MST :")
    for u, v, d in mst.edges(data=True):
        print(f"{u} — {v}  (distance : {d['weight']} km)")
        distance_totale += d['weight']
        
    texte_distance = f"Distance totale parcourue : {round(distance_totale, 3)} km"
    plt.text(0.95, 0.02, texte_distance, ha='right', va='bottom', transform=plt.gcf().transFigure, fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))    
        
    plt.tight_layout()
    plt.show()  

    print(f"Distance totale parcourue : {round(distance_totale, 3)} km")
    return mst, distance_totale


# --- Fonction 17 — Simuler les flots de transmission. ---
def simuler_flot_transmission(G, source, cible):
    """
    Calcule, visualise et affiche les chemins utilisés pour le flot maximum.
    Chaque arête a une capacité de 1.
    """
    # Graphe dirigé avec capacité = 1
    G_dirigé = nx.DiGraph()
    for u, v in G.edges():
        G_dirigé.add_edge(u, v, capacity=1)
        G_dirigé.add_edge(v, u, capacity=1)

    try:
        flot, flow_dict = nx.maximum_flow(G_dirigé, source, cible)
        print(f"\nFlot maximum de {source} vers {cible} : {flot}")

        # --- Obtenir les arêtes où le flot est actif (> 0)
        edges_actives = [(u, v) for u, voisins in flow_dict.items() for v, f in voisins.items() if f > 0]

        # --- Construire un graphe du flot utilisé
        G_flot = nx.DiGraph()
        G_flot.add_edges_from(edges_actives)

        # --- Trouver tous les chemins utilisés
        chemins_utilisés = []

        # Obtenir les chemins disjoints en arêtes
        chemins_disjoints = list(nx.edge_disjoint_paths(G_flot, source, cible))

        print("Chemins disjoints utilisés pour transmettre le flot :")
        if chemins_disjoints:
            for i, chemin in enumerate(chemins_disjoints, 1):
                print(f"  Chemin {i}: {' → '.join(map(str, chemin))}")
        else:
            print("  Aucun chemin disjoint trouvé dans le graphe du flot actif.")


        # --- Visualisation
        pos = nx.spring_layout(G, seed=42)
        
        fig = plt.figure(figsize=(10, 7))
        def on_key(event):
            if event.key == 'escape':
                plt.close(fig)
                
        fig.canvas.mpl_connect('key_press_event', on_key)
        
        plt.title(f"Flot de {source} vers {cible} — Maximum = {flot}", fontsize=14)

        nx.draw(G, pos, with_labels=False, node_size=20, edge_color="lightgray")
        nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color="orange", node_size=100)
        nx.draw_networkx_nodes(G, pos, nodelist=[cible], node_color="blue", node_size=100)
        nx.draw_networkx_edges(G, pos, edgelist=edges_actives, edge_color="red", width=2)
        
        leg_source = mlines.Line2D([], [], color='orange', marker='o', linestyle='None', markersize=10, label='Source')
        leg_cible = mlines.Line2D([], [], color='blue', marker='o', linestyle='None', markersize=10, label='Cible')
        leg_flot = mlines.Line2D([], [], color='red', linewidth=2, label='Flot actif')

        plt.legend(handles=[leg_source, leg_cible, leg_flot], loc="lower right")
        plt.tight_layout()
        plt.show()

        return flot, chemins_disjoints

    except nx.NetworkXError:
        print(f"Aucun chemin entre {source} et {cible}")
        return 0