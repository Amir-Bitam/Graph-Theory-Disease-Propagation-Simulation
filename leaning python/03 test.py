import tkinter as tk
import networkx as nx
import plotly.graph_objects as go
import random

# Création du graphe
G = nx.erdos_renyi_graph(n=20, p=0.2)  # 20 personnes, probabilité de lien 20%

# Tous les nœuds sont sains au début
for node in G.nodes:
    G.nodes[node]['state'] = 'healthy'

# Fonction pour choisir un patient zéro et propager l'infection
def propagate():
    # Réinitialiser les états
    for node in G.nodes:
        G.nodes[node]['state'] = 'healthy'

    patient_zero = random.choice(list(G.nodes))
    G.nodes[patient_zero]['state'] = 'infected'

    for neighbor in G.neighbors(patient_zero):
        if random.random() < 0.5:
            G.nodes[neighbor]['state'] = 'infected'

    show_graph()

# Affichage interactif avec Plotly
def show_graph():
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y = [], []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x, node_y = [], []
    node_color = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_color.append('red' if G.nodes[node]['state'] == 'infected' else 'green')

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color=node_color,
            size=20,
            line_width=2
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='Propagation de la maladie',
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40)
                    ))

    fig.show()

# Interface Tkinter
root = tk.Tk()
root.title("Propagation Maladie")

tk.Label(root, text="Mini Simulation de Propagation").pack(pady=10)
tk.Button(root, text="Simuler la propagation", command=propagate).pack(pady=10)

root.mainloop()
