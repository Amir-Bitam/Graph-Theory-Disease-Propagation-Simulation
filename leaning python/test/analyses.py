import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import random


# --- Fonction 12 — Déterminer combien d’interactions suffisent à propager le virus d’un individu à un autre ---
def interactions_minimales(G, source, cible):
    try:
        chemin = nx.shortest_path(G, source=source, target=cible)
        longueur = len(chemin) - 1
        print(f"\nLe virus mettra au **minimum {longueur} interaction(s)** pour atteindre {cible} depuis {source}.")
        print(f"Chemin suivi: {chemin}")
        
        # Visualisation du chemin
        pos = nx.spring_layout(G, seed=42)
        
        fig = plt.figure(figsize=(10, 7))
        def on_key(event):
            if event.key == 'escape':
                plt.close(fig)

        fig.canvas.mpl_connect('key_press_event', on_key)
        
        plt.title(f"Chemin minimal entre {source} et {cible} ({longueur} interaction(s))", fontsize=14)
        nx.draw(G, pos, with_labels=False, node_size=20, edge_color="lightgray")
        nx.draw_networkx_nodes(G, pos, nodelist=[source], node_color="orange", node_size=100, label="Source")
        nx.draw_networkx_nodes(G, pos, nodelist=[cible], node_color="blue", node_size=100, label="Cible")

        edges_chemin = list(zip(chemin, chemin[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_chemin, edge_color="red", width=2, label="Chemin")
        
        leg_source = mlines.Line2D([], [], color='orange', marker='o', linestyle='None', markersize=10, label='Source')
        leg_cible = mlines.Line2D([], [], color='blue', marker='o', linestyle='None', markersize=10, label='Cible')
        leg_chemin = mlines.Line2D([], [], color='red', linewidth=2, label='Chemin')

        plt.legend(handles=[leg_source, leg_cible, leg_chemin], loc="lower right")
        plt.tight_layout()
        plt.show()
        
        return chemin, longueur
    except nx.NetworkXNoPath:
        print(f"Aucun chemin entre {source} et {cible}")
        return None, []
    
    
# --- Fonction 13 — Super-contaminateur ---
def super_contaminateur(G):
    """
    Teste tous les sommets comme point de départ.
    Retourne celui qui permet de visiter le plus de sommets sans revenir.
    Affiche aussi graphiquement le chemin.
    """
    meilleur_sommet = None
    meilleur_chemin = []
    max_visites = 0

    for sommet in G.nodes():
        visités = set()
        chemin = [sommet]
        actuel = sommet
        visités.add(actuel)

        while True:
            voisins = [v for v in G.neighbors(actuel) if v not in visités]
            if not voisins:
                break
            suivant = random.choice(voisins)
            chemin.append(suivant)
            visités.add(suivant)
            actuel = suivant

        if len(chemin) > max_visites:
            max_visites = len(chemin)
            meilleur_sommet = sommet
            meilleur_chemin = chemin

    print(f"Le super contaminateur approximatif est le sommet {meilleur_sommet}")
    print(f"Peut atteindre {max_visites} personnes sans revenir")
    print(f"Chemin : {meilleur_chemin}")
    
    # Visualisation du chemin du super contaminateur
    pos = nx.spring_layout(G, seed=42)
    
    fig = plt.figure(figsize=(10, 7))
    def on_key(event):
        if event.key == 'escape':
            plt.close(fig)
            
    fig.canvas.mpl_connect('key_press_event', on_key)        
            
    plt.title(f"Chemin du super contaminateur {meilleur_sommet}", fontsize=14)
    nx.draw(G, pos, with_labels=False, node_size=20, edge_color="lightgray")
    nx.draw_networkx_nodes(G, pos, nodelist=[meilleur_sommet], node_color="orange", node_size=100, label="Départ")

    edges_chemin = list(zip(meilleur_chemin, meilleur_chemin[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges_chemin, edge_color="red", width=2, label="Propagation")

    leg_depart = mlines.Line2D([], [], color='orange', marker='o', linestyle='None', markersize=10, label='Départ')
    leg_chemin = mlines.Line2D([], [], color='red', linewidth=2, label='Propagation')

    plt.legend(handles=[leg_depart, leg_chemin], loc="lower right")
    plt.tight_layout()
    plt.show()

    return meilleur_sommet, max_visites, meilleur_chemin


# --- Fonction 15 — Détection des groupes isolés ---
def detecter_groupes_isoles(G):
    """
    Identifie les composantes connexes du graphe.
    Chaque composante est un groupe isolé.
    """
    composantes = list(nx.connected_components(G))
    print(f"\n{len(composantes)} groupe(s) isolé(s) détecté(s).")

    for i, comp in enumerate(composantes, 1):
        print(f"Groupe {i} ({len(comp)} personnes) : {sorted(comp)}")
    
    return composantes


# --- Fonction 16 — Temps minimal pour atteindre une cible ---
def temps_minimal_infection(G, source, cible):
    chemin, longueur = interactions_minimales(G, source, cible)
    if chemin:
        print(f"Temps minimal pour atteindre {cible} depuis {source} : {longueur} jours")
        return longueur, chemin
    else:
        print(f"Aucun chemin entre {source} et {cible}")
        return None, []