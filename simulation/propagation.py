# propagation.py
import matplotlib.pyplot as plt
import networkx as nx
from utils import compter_etats, get_couleurs

def simuler_propagation(G, prob_transmission=0.2, jours_maladie=5):
    """
    Simule la propagation de l'infection jour par jour
    avec affichage graphique à chaque étape.
    """
    pos = nx.spring_layout(G, seed=42)
    jour = 1

    while True:
        print(f"\n🦠 Jour {jour}")
        nouveaux_infectes = []

        for node in G.nodes:
            if G.nodes[node]['etat'] == 'infecté':
                for voisin in G.neighbors(node):
                    if G.nodes[voisin]['etat'] == 'sain':
                        import random
                        if random.random() < prob_transmission:
                            nouveaux_infectes.append(voisin)

                G.nodes[node]['jours'] += 1
                if G.nodes[node]['jours'] >= jours_maladie:
                    G.nodes[node]['etat'] = 'guéri'

        for node in nouveaux_infectes:
            G.nodes[node]['etat'] = 'infecté'
            G.nodes[node]['jours'] = 1

        stats = compter_etats(G)
        print("Statistiques :", stats)

        couleurs = get_couleurs(G)
        fig = plt.figure(figsize=(10, 8))
        titre = f"Propagation - Jour {jour}"
        if stats['infecté'] == 0:
            titre += " (dernier jour)"

        plt.suptitle(titre, fontsize=14, y=0.98)
        nx.draw(G, pos, node_color=couleurs, with_labels=False, node_size=20)
        texte_stats = f"Sains : {stats['sain']}  |  Infectés : {stats['infecté']}  |  Guéris : {stats['guéri']}"
        plt.text(0.95, 0.02, texte_stats, ha='right', va='bottom', transform=plt.gcf().transFigure, fontsize=10,
                 bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))

        plt.tight_layout()
        plt.show()

        if stats['infecté'] == 0:
            print("\n✅ Simulation terminée. Plus personne n’est infecté.")
            break

        jour += 1
