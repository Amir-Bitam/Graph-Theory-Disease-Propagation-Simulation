import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random
import networkx as nx

# --- Importation des modules internes ---
from graphe_generation import creer_graphe_etats
from propagation import simuler_propagation
from analyses import interactions_minimales, super_contaminateur, detecter_groupes_isoles, temps_minimal_infection
from strategies import optimiser_reseau_vaccination, simuler_flot_transmission


class InterfaceSimulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulation - Propagation de Virus")
        self.geometry("900x600")
        self.resizable(False, False)

        # Fond d'écran
        image_path = os.path.join(os.path.dirname(__file__), "./grippe_bg.png")
        bg = Image.open(image_path).resize((900, 600))
        self.bg_photo = ImageTk.PhotoImage(bg)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Création des widgets
        self.create_widgets()

        # Variables du graphe et patient zero
        self.G = None
        self.patient_zero = None

    def create_widgets(self):
        bouton_infos = [
            ("Générer Graphe", self.generer_graphe),
            ("Simuler Propagation", self.lancer_propagation),
            ("Interactions Minimales", self.lancer_interactions_min),
            ("Super-Contaminateur", self.lancer_super_contaminateur),
            ("Groupes Isolés", self.lancer_groupes_isoles),
            ("Temps Minimal", self.lancer_temps_minimal),
            ("Optimiser Vaccination", self.lancer_optimisation),
            ("Flots Transmission", self.lancer_flots)
        ]

        for i, (texte, commande) in enumerate(bouton_infos):
            tk.Button(self, text=texte, command=commande, font=("Arial", 10, "bold"), width=25, bg="#d6f5f5").place(x=620, y=220 + i * 45)

    def verifier_graphe(self):
        if self.G is None:
            messagebox.showwarning("Erreur", "Veuillez d'abord générer un graphe.")
            return False
        return True

    def generer_graphe(self):
        self.G, self.patient_zero, self.nb = creer_graphe_etats()
        messagebox.showinfo("Succès", f"Graphe généré avec {self.nb} personnes patient zéro : {self.patient_zero}")

    def lancer_propagation(self):
        if self.verifier_graphe():
            self.jour, self.texte_stats = simuler_propagation(self.G, self.patient_zero)
            messagebox.showinfo("Succès", f"Simulation terminée en {self.jour} jour(s). Plus personne n’est infecté.\n{self.texte_stats}")

    def lancer_interactions_min(self):
        if self.verifier_graphe():
            source = self.patient_zero
            cible = source
            while cible == source:
                cible = random.choice(list(self.G.nodes))
            self.chemin, self.longueur = interactions_minimales(self.G, source, cible)
            if self.chemin == None:
                messagebox.showinfo("Echec", f"Aucun chemin entre {source} et {cible}")
            else:    
                messagebox.showinfo("Succès", f"Le virus mettra au **minimum {self.longueur} interaction(s)** pour atteindre {cible} depuis {source}.\nChemin suivi: {self.chemin}")

    def lancer_super_contaminateur(self):
        if self.verifier_graphe():
            composante = max(nx.connected_components(self.G), key=len)
            G_connexe = self.G.subgraph(composante).copy()
            self.meilleur_sommet, self.max_visites ,self.meilleur_chemin  = super_contaminateur(G_connexe)
            messagebox.showinfo("Succès", f"Le super contaminateur approximatif est le sommet {self.meilleur_sommet}.\nPeut atteindre {self.max_visites} personnes sans revenir")

    def lancer_groupes_isoles(self):
        if self.verifier_graphe():
            detecter_groupes_isoles(self.G)

    def lancer_temps_minimal(self):
        if self.verifier_graphe():
            source = self.patient_zero
            cible = source
            while cible == source:
                cible = random.choice(list(self.G.nodes))
            temps_minimal_infection(self.G, source, cible)

    def lancer_optimisation(self):
        if self.verifier_graphe():
            optimiser_reseau_vaccination(self.G)

    def lancer_flots(self):
        if self.verifier_graphe():
            source = self.patient_zero
            cible = source
            while cible == source:
                cible = random.choice(list(self.G.nodes))
            simuler_flot_transmission(self.G, source, cible)


if __name__ == "__main__":
    app = InterfaceSimulation()
    app.mainloop()
