import networkx as nx
import random
import plotly.graph_objects as go

# Étape 1 : Générer un nombre de personnes aléatoire
nb_personnes = random.randint(100, 1000)
print(f"Nombre de personnes dans le réseau : {nb_personnes}")

# Étape 2 : Créer un graphe social aléatoire
p = round(random.uniform(0.01, 0.05), 3)
G = nx.erdos_renyi_graph(n=nb_personnes, p=p)

# Étape 3 : Obtenir les positions des nœuds avec layout spring
pos = nx.spring_layout(G, seed=42)

# Extraction des coordonnées des arêtes
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

# Extraction des coordonnées des nœuds
node_x = []
node_y = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        reversescale=True,
        color=[len(list(G.neighbors(n))) for n in G.nodes()],
        size=6,
        colorbar=dict(
            thickness=10,
            title=dict(text='Degré du nœud'),
            xanchor='left',
            titleside='right'
        )
    ),
    text=[f'Nœud {n} : {len(list(G.neighbors(n)))} voisins' for n in G.nodes()]
)

# Création de la figure Plotly
fig = go.Figure(data=[edge_trace, node_trace],
         layout=go.Layout(
            title=f"Graphe social aléatoire avec {nb_personnes} personnes (p = {p})",
            titlefont_size=16,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False))
        )

fig.show()
