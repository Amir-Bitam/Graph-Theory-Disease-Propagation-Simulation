import networkx as nx
import random
import matplotlib.pyplot as plt

# Étape 1 : Générer un nombre de personnes aléatoire
nb_personnes = random.randint(100, 1000)
print(f"Nombre de personnes dans le réseau : {nb_personnes}")

# Étape 2 : Créer un graphe social aléatoire
# p = probabilité de connexion entre deux personnes (entre 0.01 et 0.1)
p = round(random.uniform(0.01, 0.05), 3)
print(f"probabilité de connexion entre deux personnes : {p}")
G = nx.erdos_renyi_graph(n=nb_personnes, p=p)

# Étape 3 : Afficher le graphe avec le titre tout en haut
plt.figure(figsize=(12, 9))

# Titre principal en haut de toute la figure
plt.suptitle(f"Graphe social aléatoire avec {nb_personnes} personnes (p = {p})", fontsize=14, y=0.98)

# Dessiner le graphe
nx.draw(G, node_size=10, with_labels=False)

# Ajuster l'espace pour ne pas cacher le titre
plt.tight_layout()
plt.subplots_adjust(top=0.93)

plt.show()
