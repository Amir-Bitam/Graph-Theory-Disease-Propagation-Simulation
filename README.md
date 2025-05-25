
# 🦠 Projet THG — Simulation de Propagation Virale

Ce projet a été réalisé dans le cadre du mini-projet de Théorie des Graphes (THG).  
L’objectif est de modéliser et simuler la propagation d’une maladie infectieuse à travers un réseau social, représenté sous forme de graphe.

## 🧪 Fonctionnalités principales

✅ **19 fonctions implémentées** couvrant :
- 🔧 Création et manipulation de graphes (matrice d’adjacence)
- 🧬 Simulation jour par jour de l’infection
- 📍 Analyse des points critiques : super-contaminateurs, interactions minimales, groupes isolés
- 💉 Optimisation des stratégies de vaccination (MST)
- 💧 Calcul de flots de transmission (maximum flow)
- 🖥️ Interface graphique avec `Tkinter` et visualisation avec `matplotlib`

## 🗂️ Structure du projet

```
Projet-THG/
├── simulation/
│   ├── Main.py                  # Exécution en console (tests)
│   ├── interface.py             # Interface utilisateur avec Tkinter
│   ├── graphe_generation.py     # Génération de graphe et patient zéro
│   ├── propagation.py           # Simulation de la propagation
│   ├── analyses.py              # Fonctions d’analyse : interactions, groupes, etc.
│   ├── strategies.py            # Fonctions avancées : flots, MST
│   ├── utils.py                 # Fonctions utilitaires (couleurs, états)
│   └── grippe_bg.png            # Image de fond de l’interface
├── FONCTIONS DE BASE SUR LES GRAPHES.py     # Fonctions 1 à 11 (matrice d’adjacence)
├── ANALYSE & SIMULATION AVANCÉE DE LA PROPAGATION.py  # Tests complets des fonctions 12 à 18
```

## 🛠️ Technologies utilisées

- `Python 3`
- `networkx` — manipulation de graphes
- `matplotlib` — visualisation
- `tkinter` — interface graphique
- `random` — génération aléatoire de réseaux


## 🚀 Lancer le projet

### ▶️ Interface graphique
```bash
python simulation/interface.py
```

### 🧪 Exécuter les tests
```bash
python simulation/Main.py
```

### Colaborateurs:
- Amir-Bitam
- rofaidaab

