import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# --- 1. Création du graphe ---
nb_personnes = random.randint(100, 300)
p = round(random.uniform(0.01, 0.05), 3)
G = nx.erdos_renyi_graph(n=nb_personnes, p=p)

print(f"Taile de la population {nb_personnes}")

# --- Fonction 14 — Attribution des états (sain, infecté) ---

def attribuer_etats(G):
    """
    Attribue à chaque nœud l’état 'sain' au départ.
    Puis choisit un patient zéro au hasard et le passe à 'infecté'.
    """
    for node in G.nodes():
        G.nodes[node]['etat'] = 'sain'
        G.nodes[node]['jours'] = 0

    patient_zero = random.choice(list(G.nodes()))
    G.nodes[patient_zero]['etat'] = 'infecté'
    G.nodes[patient_zero]['jours'] = 1

    print(f"🧬 Patient zéro choisi : {patient_zero}")
    return patient_zero

# --- Attribution des états : sain/infecté ---
patient_zero = attribuer_etats(G)

# --- 4. Simulation jour par jour ---
jour = 1
prob_transmission = 0.2
jours_maladie = 5

# Position fixe pour dessiner le graphe toujours au même endroit
pos = nx.spring_layout(G, seed=42)

while True:
    print(f"\n Jour {jour}")
    nouveaux_infectés = []

    for node in G.nodes():
        if G.nodes[node]['etat'] == 'infecté':
            for voisin in G.neighbors(node):
                if G.nodes[voisin]['etat'] == 'sain':
                    if random.random() < prob_transmission:
                        nouveaux_infectés.append(voisin)

            G.nodes[node]['jours'] += 1
            if G.nodes[node]['jours'] >= jours_maladie:
                G.nodes[node]['etat'] = 'guéri'

    for node in nouveaux_infectés:
        G.nodes[node]['etat'] = 'infecté'
        G.nodes[node]['jours'] = 1

    #  Statistiques
    def compter_etats(G):
        etats = {"sain": 0, "infecté": 0, "guéri": 0}
        for node in G.nodes:
            etats[G.nodes[node]['etat']] += 1
        return etats

    stats = compter_etats(G)
    print("Statistiques :", stats)

    #  Visualisation du graphe
    couleurs = []
    for node in G.nodes():
        etat = G.nodes[node]['etat']
        if etat == "sain":
            couleurs.append("green")
        elif etat == "infecté":
            couleurs.append("red")
        else:  # guéri
            couleurs.append("blue")

    fig = plt.figure(figsize=(10, 8))
    
    def on_key(event):
        if event.key == 'escape':
            plt.close(fig)

    fig.canvas.mpl_connect('key_press_event', on_key)
        
    titre = f"Propagation avec {nb_personnes} personnes - Jour {jour}"
    if stats["infecté"] == 0:
        titre += " (dernier jour)"
    
    plt.suptitle(titre, fontsize=14, y=0.98)
    nx.draw(G, pos, node_color=couleurs, with_labels=False, node_size=20)
    # plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    
    #  Affichage des statistiques dans le coin inférieur droit
    texte_stats = f"Sains : {stats['sain']}  |  Infectés : {stats['infecté']}  |  Guéris : {stats['guéri']}"
    plt.text(0.95, 0.02, texte_stats, ha='right', va='bottom', transform=plt.gcf().transFigure, fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))

    
    plt.show()

    if stats["infecté"] == 0:
        print("\n Simulation terminée. Plus personne n’est infecté.")
        break

    jour += 1



# --- Fonction 12 — Déterminer combien d’interactions suffisent à propager le virus d’un individu à un autre ---
def interactions_minimales(G, source, cible):
    try:
        chemin = nx.shortest_path(G, source=source, target=cible)
        longueur = len(chemin) - 1
        print(f" Le virus mettra au **minimum {longueur} interaction(s)** pour atteindre le sommet {cible} depuis {source}.")
        print(f"Chemin suivi: {chemin}")
        return chemin, longueur
    except nx.NetworkXNoPath:
        print(f" Aucun chemin entre {source} et {cible} → l’infection ne peut pas atteindre ce sommet.")
        return None, []

# --- Test de la fonction 12 ---
print("\n Test de la Fonction 12 — nombre minimal d’interactions :")
source = patient_zero
cible = random.choice(list(G.nodes))
while cible == source:
    cible = random.choice(list(G.nodes))
    
print(f"\n Calcul du nombre minimal d’interactions entre {source} (patient zéro) et {cible} :")
interactions_minimales(G, source, cible)



# --- Fonction 13 — Super-contaminateur ---
# Étape 1 : extraire la plus grande composante connexe
composante = max(nx.connected_components(G), key=len)
G_connexe = G.subgraph(composante).copy()
n = G_connexe.number_of_nodes()

def contaminate_heuristique_max(G):
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

    print(f" Le super contaminateur approximatif est le sommet {meilleur_sommet}")
    print(f"🧪 Il peut atteindre {max_visites} personnes sans revenir.")
    print(f" Chemin : {meilleur_chemin}")


#  Test de la fonction 13 (super contaminateur)
print("\n Test de la Fonction 13 — super contaminateur :")
print("\n Recherche d’un super contaminateur:")
contaminate_heuristique_max(G_connexe)



# --- Fonction 15 — Détection des groupes isolés ---
def detecter_groupes_isolés(G):
    """
    Identifie les composantes connexes du graphe.
    Chaque composante est un groupe isolé.
    """
    composantes = list(nx.connected_components(G))
    print(f" {len(composantes)} groupe(s) isolé(s) détecté(s).")

    for i, comp in enumerate(composantes, 1):
        print(f"🧩 Groupe {i} ({len(comp)} personnes) : {sorted(comp)}")
    
    return composantes

# --- Test de la fonction 15 ---
print("\n Test de la Fonction 15 — Détection des groupes isolés :")
print("\n Détection des groupes isolés :")
detecter_groupes_isolés(G)



# --- Fonction 16 — Temps minimal pour atteindre une cible ---
def temps_minimal_infection(G, source, cible):
    chemin, longueur = interactions_minimales(G, source, cible)
    if chemin:
        print(f" Temps minimal pour atteindre {cible} depuis {source} : {longueur*5} jours ")
        return longueur, chemin
    else:
        print(f" Aucun chemin entre {source} et {cible}")
        return None, []

# --- Test de la fonction 16 ---
print("\n Test de la Fonction 16 — Temps minimal d'infection (via interactions_minimales) :")
source = patient_zero
cible = random.choice(list(G.nodes))
while cible == source:
    cible = random.choice(list(G.nodes))

temps_minimal_infection(G, source, cible)


# --- Fonction 18 — Optimisation d’un réseau de vaccination mobile à moindre coût. ---

def optimiser_reseau_vaccination(G):
    """
    Calcule et affiche l’arbre couvrant minimal (MST) basé sur les distances entre patients.
    Retourne aussi la distance totale parcourue.
    """
    #  Générer une position fixe pour chaque nœud (x, y)
    pos = nx.spring_layout(G, seed=42)

    # 🧮 Ajouter la vraie distance comme poids
    for u, v in G.edges():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
        G[u][v]['weight'] = round(distance, 3)

    #  Calcul du MST
    mst = nx.minimum_spanning_tree(G, weight='weight')

    #  Visualisation
    edge_labels = nx.get_edge_attributes(mst, 'weight')

    plt.figure(figsize=(10, 7))
    plt.title(" Réseau de vaccination optimal (MST)", fontsize=14)

    # Graphe original (gris)
    nx.draw(G, pos, with_labels=False, node_size=20, edge_color="lightgray")

    # MST en rouge
    nx.draw(mst, pos, with_labels=False, node_size=20, edge_color="red", width=2)

    # Affichage des poids
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_size=8)

    #  Affichage des arêtes retenues + distance totale
    distance_totale = 0
    print("\n Arêtes retenues dans le MST :")
    for u, v, d in mst.edges(data=True):
        print(f"{u} — {v}  (distance : {d['weight']} km)")
        distance_totale += d['weight']
        
    texte_distance = f"Distance totale parcourue : {round(distance_totale, 3)} km"
    plt.text(0.95, 0.02, texte_distance, ha='right', va='bottom', transform=plt.gcf().transFigure, fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))    
        
    plt.tight_layout()
    plt.show()    

    print(f"\n Distance totale parcourue : {round(distance_totale, 3)} km")

    return mst

# --- Test de la fonction 18 ---
print("\n Fonction 18 — Optimisation du réseau de vaccination :")
mst = optimiser_reseau_vaccination(G)


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
        print(f"\n Flot maximum de {source} vers {cible} : {flot}")

        # --- Obtenir les arêtes où le flot est actif (> 0)
        edges_actives = [(u, v) for u, voisins in flow_dict.items() for v, f in voisins.items() if f > 0]

        # --- Construire un graphe du flot utilisé
        G_flot = nx.DiGraph()
        G_flot.add_edges_from(edges_actives)

        # --- Trouver tous les chemins utilisés
        chemins_utilisés = []

        def dfs_chemins(actuel, chemin):
            if actuel == cible:
                chemins_utilisés.append(chemin[:])
                return
            for voisin in G_flot.successors(actuel):
                if voisin not in chemin:
                    chemin.append(voisin)
                    dfs_chemins(voisin, chemin)
                    chemin.pop()

        dfs_chemins(source, [source])

        print("\n Chemins utilisés pour transmettre le flot :")
        if chemins_utilisés:
            for i, chemin in enumerate(chemins_utilisés, 1):
                print(f"  Chemin {i}: {' → '.join(map(str, chemin))}")
        else:
            print("  Aucun chemin trouvé dans le graphe du flot actif.")

        # --- Visualisation
        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(10, 7))
        plt.title(f" Flot de {source} vers {cible} — Maximum = {flot}", fontsize=14)

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

        return flot

    except nx.NetworkXError:
        print(f" Aucun chemin entre {source} et {cible}")
        return 0


# --- Test de la fonction 17 ---
print("\n Fonction 17 — Simulation de flots de transmission :")
source = patient_zero
cible = random.choice(list(G.nodes))
while cible == source:
    cible = random.choice(list(G.nodes))

simuler_flot_transmission(G, source, cible)
