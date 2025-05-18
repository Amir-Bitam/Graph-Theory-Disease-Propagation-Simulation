# --------- Crée une matrice d’adjacence vide pour un graphe non orienté avec n sommets. ---------
# ---------         Chaque case MA[i][j] vaut 0 : il n'y a pas encore d’arêtes.          ---------
    
def creer_matrice(n):
  return [[0 for _ in range(n)] for _ in range(n)]



# --------- Ajoute une arête entre les sommets i et j dans la matrice d'adjacence MA.
# --------- Le graphe est non orienté → MA[i][j] = MA[j][i] = 1

def ajouter_arete(MA, i, j):
  # Vérification que les indices sont valides (dans la matrice)
  n = len(MA)  # nombre de sommets dans le graphe

  if i >= n or j >= n or i < 0 or j < 0:
      print(f"Erreur : sommet {i} ou {j} hors limites (0 à {n-1})")
      return

  # Mettre 1 dans la case [i][j] → arête de i vers j
  MA[i][j] = 1

  # Mettre aussi 1 dans la case [j][i] → arête de j vers i (graphe non orienté)
  MA[j][i] = 1
    
    

# --------- Supprime l’arête entre les sommets i et j dans la matrice d’adjacence MA.
# --------- Le graphe est non orienté → MA[i][j] = MA[j][i] = 0
    
def supprimer_arete(MA, i, j):
  # Récupérer le nombre de sommets
  n = len(MA)

  # Vérifier que i et j sont des indices valides
  if i >= n or j >= n or i < 0 or j < 0:
      print(f"Erreur : sommet {i} ou {j} hors limites (0 à {n-1})")
      return

  # Supprimer l’arête en mettant 0 dans les deux cases
  MA[i][j] = 0
  MA[j][i] = 0




# --------- Ajoute un sommet à la matrice d’adjacence MA (graphe non orienté).
# --------- Cela agrandit la matrice en ajoutant une ligne et une colonne de zéros.

def ajouter_sommet(MA):
  n = len(MA)  # Taille actuelle de la matrice

  # Ajouter un zéro à chaque ligne existante (colonne supplémentaire)
  for ligne in MA:
      ligne.append(0)

  # Ajouter une nouvelle ligne de n+1 zéros
  nouvelle_ligne = [0] * (n + 1)
  MA.append(nouvelle_ligne)