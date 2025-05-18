import networkx as nx
import random
import matplotlib.pyplot as plt

# Générer un graphe social aléatoire
nb_personnes = random.randint(100, 300)
print(f"Nombre de personnes dans le réseau : {nb_personnes}")
p = round(random.uniform(0.01, 0.05), 3)
print(f"probabilité de connexion entre deux personnes : {p}")
G = nx.erdos_renyi_graph(n=nb_personnes, p=p)

# Initialiser l'état de chaque personne (sain au départ)
for node in G.nodes():
    G.nodes[node]['etat'] = 'sain'

# Choisir un patient zéro au hasard
patient_zero = random.choice(list(G.nodes()))
G.nodes[patient_zero]['etat'] = 'infecté'

print(f"Le patient zéro est : {patient_zero}")
