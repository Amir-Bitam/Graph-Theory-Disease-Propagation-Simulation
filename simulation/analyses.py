# analyses.py
import networkx as nx
from utils import afficher_chemin


def interactions_minimales(G, source, cible):
    try:
        chemin = nx.shortest_path(G, source=source, target=cible)
        longueur = len(chemin) - 1
        print(f"✅ Le virus mettra au **minimum {longueur} interaction(s)** pour atteindre {cible} depuis {source}.")
        print(f"Chemin suivi: {chemin}")
        return chemin, longueur
    except nx.NetworkXNoPath:
        print(f"❌ Aucun chemin entre {source} et {cible}")
        return None, []


def contaminate_heuristique_max(G):
    meilleur_sommet = None
    meilleur_chemin = []
    max_visites = 0

    for sommet in G.nodes():
        visites = set()
        chemin = [sommet]
        actuel = sommet
        visites.add(actuel)

        while True:
            voisins = [v for v in G.neighbors(actuel) if v not in visites]
            if not voisins:
                break
            suivant = voisins[0]
            chemin.append(suivant)
            visites.add(suivant)
            actuel = suivant

        if len(chemin) > max_visites:
            max_visites = len(chemin)
            meilleur_sommet = sommet
            meilleur_chemin = chemin

    print(f"🏆 Super contaminateur approximatif : {meilleur_sommet}")
    print(f"🧪 Peut atteindre {max_visites} personnes sans revenir")
    print(f"📍 Chemin : {meilleur_chemin}")
    return meilleur_sommet, meilleur_chemin


def detecter_groupes_isoles(G):
    composantes = list(nx.connected_components(G))
    print(f"🔍 {len(composantes)} groupe(s) isolé(s) détecté(s)")
    for i, comp in enumerate(composantes, 1):
        print(f"🧩 Groupe {i} ({len(comp)} sommets) : {sorted(comp)}")
    return composantes


def temps_minimal_infection(G, source, cible):
    chemin, longueur = interactions_minimales(G, source, cible)
    if chemin:
        print(f"🕒 Temps minimal pour atteindre {cible} depuis {source} : {longueur * 5} jours")
        return longueur * 5, chemin
    else:
        return None, []
