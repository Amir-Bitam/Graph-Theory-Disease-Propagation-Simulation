# utils.py
def compter_etats(G):
    stats = {"sain": 0, "infecté": 0, "guéri": 0}
    for node in G.nodes:
        etat = G.nodes[node].get("etat", "sain")
        if etat in stats:
            stats[etat] += 1
    return stats


def get_couleurs(G):
    couleurs = []
    for node in G.nodes():
        etat = G.nodes[node].get("etat", "sain")
        if etat == "sain":
            couleurs.append("green")
        elif etat == "infecté":
            couleurs.append("red")
        else:
            couleurs.append("blue")
    return couleurs
