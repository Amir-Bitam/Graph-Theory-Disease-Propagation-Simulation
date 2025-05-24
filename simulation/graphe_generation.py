# graphe_generation.py
import networkx as nx
import random

def creer_graphe_etats(nb_personnes=None, p=None):
    """
    Génère un graphe aléatoire Erdos-Renyi et attribue à chaque nœud un état initial
    ('sain' ou 'infecté') avec un patient zéro.
    """
    nb = nb_personnes or random.randint(100, 300)
    proba = p or round(random.uniform(0.01, 0.05), 3)
    G = nx.erdos_renyi_graph(nb, proba)

    for node in G.nodes:
        G.nodes[node]['etat'] = 'sain'
        G.nodes[node]['jours'] = 0

    patient_zero = random.choice(list(G.nodes))
    G.nodes[patient_zero]['etat'] = 'infecté'
    G.nodes[patient_zero]['jours'] = 1

    print(f"🧬 Graphe généré avec {nb} personnes, p = {proba}")
    print(f"🦠 Patient zéro : {patient_zero}")
    return G, patient_zero
