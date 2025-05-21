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




# --------- Supprime le sommet i du graphe représenté par la matrice MA.
# --------- Cela revient à supprimer la i-ème ligne et la i-ème colonne.
    
def supprimer_sommet(MA, i):
  n = len(MA)  # Nombre de sommets

  # Vérifier que le sommet existe (index valide)
  if i < 0 or i >= n:
    print(f"Erreur : sommet {i} hors limites (0 à {n-1})")
    return

  # Supprimer la i-ème ligne (connexions sortantes du sommet)
  MA.pop(i)

  # Supprimer la i-ème colonne (connexions entrantes vers le sommet)
  for ligne in MA:
    ligne.pop(i)



# --------- Affiche une matrice d’adjacence avec les indices des sommets.

def afficher_matrice(MA):
  n = len(MA)  # nombre de sommets

  print("\nMatrice d’adjacence :")

  # Affichage de l'en-tête (indices des colonnes)
  print("   ", end="")  # pour décaler la première ligne
  for j in range(n):
    print(f"{j:2}", end=" ")
  print()  # retour à la ligne

  # Affichage des lignes avec les indices
  for i in range(n):
    print(f"{i:2} ", end="")  # indice de la ligne
    for j in range(n):
      print(f"{MA[i][j]:2}", end=" ")
    print()  # retour à la ligne après chaque ligne



# Retourne l’ordre du graphe, c’est-à-dire le nombre de sommets.

def calculer_ordre(MA):
  return len(MA)




# Calcule le degré de chaque sommet dans le graphe non orienté.
# Retourne une liste où chaque case i contient le degré du sommet i.
    

def degres_sommets(MA):
  n = len(MA)  # nombre de sommets
  degres = []

  for i in range(n):
    # Somme des connexions de la ligne i = degré du sommet i
    degre = sum(MA[i])
    degres.append(degre)

  return degres



# Affiche les voisins directs du sommet i (ceux qui sont connectés à i).
    
def voisinage(MA, i):
  n = len(MA)

  if i < 0 or i >= n:
    print(f"Erreur : sommet {i} hors limites (0 à {n-1})")
    return []

  voisins = []
  for j in range(n):
    if MA[i][j] == 1:
      voisins.append(j)

  return voisins



#     Trouve tous les chemins de longueur L entre les sommets i et j.
#     Retourne une liste de chemins (chaque chemin est une liste de sommets).

def chemins_longueur_L(MA, i, j, L):
  n = len(MA)
  
  if i < 0 or j < 0 or i >= n or j >= n:
    print("Erreur : sommet invalide.")
    return []

  resultats = []

  def dfs(actuel, chemin, longueur_restante):
    if longueur_restante == 0:
      if actuel == j:
        resultats.append(chemin[:])  # Copie du chemin trouvé
      return

    for voisin in range(n):
      if MA[actuel][voisin] == 1 and voisin not in chemin:
        chemin.append(voisin)
        dfs(voisin, chemin, longueur_restante - 1)
        chemin.pop()  # Revenir en arrière

  dfs(i, [i], L)

  if not resultats:
    print(f"❌ Aucun chemin de longueur {L} entre {i} et {j}.")
  else:
    print(f"✅ {len(resultats)} chemin(s) trouvé(s) entre {i} et {j} de longueur {L}:")

  for resultat in resultats:
    print(" → ".join(map(str, resultat)))
  


MA = [
    [0, 1, 0, 1],  # 0 → 1, 3
    [1, 0, 1, 0],  # 1 → 0, 2
    [0, 1, 0, 1],  # 2 → 1, 3
    [1, 0, 1, 0]   # 3 → 0, 2
]

chemins_longueur_L(MA, 0, 2, 2)
chemins_longueur_L(MA, 0, 0, 4)







