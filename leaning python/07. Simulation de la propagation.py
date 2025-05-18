import networkx as nx
import random
import matplotlib.pyplot as plt

# ----------------------
# 1. Créer le graphe
nb_personnes = random.randint(100, 300)
p = round(random.uniform(0.01, 0.05), 3)
G = nx.erdos_renyi_graph(n=nb_personnes, p=p)

# ----------------------
# 2. Initialiser les personnes
for node in G.nodes():
    G.nodes[node]['etat'] = 'sain'
    G.nodes[node]['jours'] = 0

# ----------------------
# 3. Choisir le patient zéro
patient_zero = random.choice(list(G.nodes()))
G.nodes[patient_zero]['etat'] = 'infecté'
G.nodes[patient_zero]['jours'] = 1

# ----------------------
# 4. Simulation jour par jour
jour = 1
prob_transmission = 0.2   # 20% de chance d'infecter un voisin
jours_maladie = 5         # après 5 jours, on guérit

while True:
    print(f"\n🦠 Jour {jour}")
    nouveaux_infectés = []

    for node in G.nodes():
        if G.nodes[node]['etat'] == 'infecté':
            # contaminer les voisins sains
            for voisin in G.neighbors(node):
                if G.nodes[voisin]['etat'] == 'sain':
                    if random.random() < prob_transmission:
                        nouveaux_infectés.append(voisin)

            # augmenter le nombre de jours infecté
            G.nodes[node]['jours'] += 1
            if G.nodes[node]['jours'] >= jours_maladie:
                G.nodes[node]['etat'] = 'guéri'

    # mettre à jour les nouveaux infectés
    for node in nouveaux_infectés:
        G.nodes[node]['etat'] = 'infecté'
        G.nodes[node]['jours'] = 1

    # affichage des stats
    def compter_etats(G):
        etats = {"sain": 0, "infecté": 0, "guéri": 0}
        for node in G.nodes:
            etats[G.nodes[node]['etat']] += 1
        return etats

    stats = compter_etats(G)
    print("Statistiques :", stats)

    if stats["infecté"] == 0:
        print("\n✅ Simulation terminée. Plus personne n’est infecté.")
        break

    jour += 1
