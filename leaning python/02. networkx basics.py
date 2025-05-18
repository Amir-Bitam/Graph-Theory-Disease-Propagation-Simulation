import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # on crée un graphe non orienté

# G.add_node("A")        # on ajoute un sommet
G.add_nodes_from(["Alger", "Oran", "Constantine"])  # plusieurs sommets

# G.add_edge("A", "B")         # une arête entre A et B
G.add_edges_from([("Alger", "Oran"), ("Oran", "Constantine"), ("Alger", "Constantine")])  # plusieurs arêtes


nx.draw(G, with_labels=True)  # dessiner le graphe avec les noms des sommets
plt.show()