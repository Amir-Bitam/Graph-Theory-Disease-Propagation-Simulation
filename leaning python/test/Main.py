from graphe_generation import creer_graphe_etats
from propagation import simuler_propagation
from analyses import (
  interactions_minimales,
  super_contaminateur,
  detecter_groupes_isoles,
  temps_minimal_infection
)
import random
import networkx as nx
from strategies import (optimiser_reseau_vaccination,
  simuler_flot_transmission
)





# --- Création du graphe et définition des états ---
G, patient_zero = creer_graphe_etats()

# --- Simulation de propagation ---
simuler_propagation(G)

# --- Analyses ---
# --- Fonction 12 — Déterminer combien d’interactions suffisent à propager le virus d’un individu à un autre ---
print("\nAnalyse: interactions minimales")
source = patient_zero
cible = source
while cible == source:
    cible = random.choice(list(G.nodes))
interactions_minimales(G, source, cible)


# --- Fonction 13 — Super-contaminateur ---
print("\nAnalyse: super contaminateur")

#extraire la plus grande composante connexe
composante = max(nx.connected_components(G), key=len)
G_connexe = G.subgraph(composante).copy()
n = G_connexe.number_of_nodes()

print("\nRecherche d’un super contaminateur:")
super_contaminateur(G_connexe)


# --- Fonction 15 — Détection des groupes isolés ---
print("\nAnalyse: groupes isolés")
detecter_groupes_isoles(G)


# --- Fonction 16 — Temps minimal pour atteindre une cible ---
print("\nAnalyse: temps minimal")
temps_minimal_infection(G, source, cible)


# --- Stratégies ---
# --- Fonction 18 — Optimisation d’un réseau de vaccination mobile à moindre coût. ---
print("\nStratégie: optimisation vaccination")
optimiser_reseau_vaccination(G)


# --- Fonction 17 — Simuler les flots de transmission. ---
print("\nStratégie: simulation de flots")
simuler_flot_transmission(G, source, cible)