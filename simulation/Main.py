# main.py
from graphe_generation import creer_graphe_etats
from propagation import simuler_propagation
from simulation.analyses import (
    interactions_minimales,
    contaminate_heuristique_max,
    detecter_groupes_isoles,
    temps_minimal_infection
)
from strategies import optimiser_reseau_vaccination, simuler_flot_transmission
import random

# --- Création du graphe et définition des états ---
G, patient_zero = creer_graphe_etats()

# --- Simulation de propagation ---
simuler_propagation(G)

# --- Analyses ---
print("\nAnalyse: interactions minimales")
source = patient_zero
cible = source
while cible == source:
    cible = random.choice(list(G.nodes))
interactions_minimales(G, source, cible)

print("\nAnalyse: super contaminateur")
contaminate_heuristique_max(G)

print("\nAnalyse: groupes isolés")
detecter_groupes_isoles(G)

print("\nAnalyse: temps minimal")
temps_minimal_infection(G, source, cible)

# --- Stratégies ---
print("\nStratégie: optimisation vaccination")
optimiser_reseau_vaccination(G)

print("\nStratégie: simulation de flots")
simuler_flot_transmission(G, source, cible)
