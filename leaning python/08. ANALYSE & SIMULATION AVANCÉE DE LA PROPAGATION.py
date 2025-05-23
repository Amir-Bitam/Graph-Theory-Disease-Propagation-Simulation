import networkx as nx
import random
import matplotlib.pyplot as plt

# --- 1. Création du graphe ---
nb_personnes = random.randint(100, 300)
p = round(random.uniform(0.01, 0.05), 3)
G = nx.erdos_renyi_graph(n=nb_personnes, p=p)

print(f"taile de la population {nb_personnes}")

# --- 2. Initialisation des nœuds ---
for node in G.nodes():
    G.nodes[node]['etat'] = 'sain'
    G.nodes[node]['jours'] = 0


# --- 3. Patient zéro ---
patient_zero = random.choice(list(G.nodes()))
G.nodes[patient_zero]['etat'] = 'infecté'
G.nodes[patient_zero]['jours'] = 1

# --- 4. Simulation jour par jour ---
jour = 1
prob_transmission = 0.2
jours_maladie = 5

# Position fixe pour dessiner le graphe toujours au même endroit
pos = nx.spring_layout(G, seed=42)

while True:
    print(f"\n🦠 Jour {jour}")
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

    # 📊 Statistiques
    def compter_etats(G):
        etats = {"sain": 0, "infecté": 0, "guéri": 0}
        for node in G.nodes:
            etats[G.nodes[node]['etat']] += 1
        return etats

    stats = compter_etats(G)
    print("Statistiques :", stats)

    # 🎨 Visualisation du graphe
    couleurs = []
    for node in G.nodes():
        etat = G.nodes[node]['etat']
        if etat == "sain":
            couleurs.append("green")
        elif etat == "infecté":
            couleurs.append("red")
        else:  # guéri
            couleurs.append("blue")

    plt.figure(figsize=(10, 8))
    
    titre = f"Propagation avec {nb_personnes} personnes - Jour {jour}"
    if stats["infecté"] == 0:
        titre += " (dernier jour)"
    
    plt.suptitle(titre, fontsize=14, y=0.98)
    nx.draw(G, pos, node_color=couleurs, with_labels=False, node_size=20)
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    
    # 📉 Affichage des statistiques dans le coin inférieur droit
    texte_stats = f"Sains : {stats['sain']}  |  Infectés : {stats['infecté']}  |  Guéris : {stats['guéri']}"
    plt.text(0.95, 0.02, texte_stats, ha='right', va='bottom', transform=plt.gcf().transFigure, fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))

    
    plt.show()

    if stats["infecté"] == 0:
        print("\n✅ Simulation terminée. Plus personne n’est infecté.")
        break

    jour += 1



# --- Fonction 12 — Déterminer combien d’interactions suffisent à propager le virus d’un individu à un autre ---
def interactions_minimales(G, source, cible):
    try:
        chemin = nx.shortest_path(G, source=source, target=cible)
        longueur = len(chemin) - 1
        print(f"✅ Le virus mettra au **minimum {chemin} interaction(s)** pour atteindre le sommet {cible} depuis {source}.")
        print(f"Chemin suivi: {chemin}")
        return chemin, longueur
    except nx.NetworkXNoPath:
        print(f"❌ Aucun chemin entre {source} et {cible} → l’infection ne peut pas atteindre ce sommet.")
        return None, []

# --- Test de la fonction 12 ---
source = patient_zero
cible = random.choice(list(G.nodes))
while cible == source:
    cible = random.choice(list(G.nodes))

print(f"\n📌 Calcul du nombre minimal d’interactions entre {source} (patient zéro) et {cible} :")
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

    print(f"\n🏆 Le super contaminateur approximatif est le sommet {meilleur_sommet}")
    print(f"🧪 Il peut atteindre {max_visites} personnes sans revenir.")
    print(f"📍 Chemin : {meilleur_chemin}")


# 🔬 Test de la fonction 13 (super contaminateur)
print("\n🧪 Recherche d’un super contaminateur:")
contaminate_heuristique_max(G_connexe)

