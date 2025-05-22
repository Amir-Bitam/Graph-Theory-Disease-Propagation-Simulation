# --------- Crée une matrice d’adjacence vide pour un graphe non orienté avec n sommets. ---------
# ---------         Chaque case MA[i][j] vaut 0 : il n'y a pas encore d’arêtes.          ---------
    
def creer_matrice(n):
  return [[0 for _ in range(n)] for _ in range(n)]


# ----- TEST -----
print()
print("Fonction 1 : Créer une matrice d’adjacence vide")
MA = creer_matrice(4)
for ligne in MA:
    print(ligne)


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
    
    
# ----- TEST -----  
print()
print("Fonction 2 : Ajouter une arête au graphe")
MA = creer_matrice(4)
ajouter_arete(MA, 1, 3)
ajouter_arete(MA, 0, 2)

for ligne in MA:
    print(ligne)
 

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


# ----- TEST -----  
print()
print("Fonction 3 : Supprimer une arête du graphe")
MA = creer_matrice(4)
ajouter_arete(MA, 1, 2)
ajouter_arete(MA, 0, 3)

print("Avant suppression :")
for ligne in MA:
    print(ligne)

supprimer_arete(MA, 1, 2)

print("Après suppression de l’arête (1,2) :")
for ligne in MA:
    print(ligne)


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


# ----- TEST ----- 
print()
print("Fonction 4 : Ajouter un sommet au graphe")
MA = creer_matrice(3)
ajouter_arete(MA, 0, 1)
print("Avant ajout de sommet :")
for ligne in MA:
    print(ligne)

ajouter_sommet(MA)
print("Après ajout d’un sommet :")
for ligne in MA:
    print(ligne)


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


# ----- TEST ----- 
print()
print("Fonction 5 : Supprimer un sommet du graphe")
MA = creer_matrice(4)
ajouter_arete(MA, 0, 1)
ajouter_arete(MA, 2, 3)

print("Avant suppression du sommet 2 :")
for ligne in MA:
    print(ligne)

supprimer_sommet(MA, 2)

print("Après suppression du sommet 2 :")
for ligne in MA:
    print(ligne)


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


# ----- TEST ----- 
print("Fonction 6 : Afficher la matrice d’adjacence")
MA = creer_matrice(4)
ajouter_arete(MA, 0, 1)
ajouter_arete(MA, 2, 3)

afficher_matrice(MA)


# --------- Retourne l’ordre du graphe, c’est-à-dire le nombre de sommets.

def calculer_ordre(MA):
  return len(MA)


# ----- TEST ----- 
print()
print("Fonction 7 : Calculer l’ordre du graphe")
MA = creer_matrice(5)
ajouter_sommet(MA)
ajouter_sommet(MA)

afficher_matrice(MA)
ordre = calculer_ordre(MA)
print(f"\n✅ Ordre du graphe : {ordre}")



# --------- Calcule le degré de chaque sommet dans le graphe non orienté.
# --------- Retourne une liste où chaque case i contient le degré du sommet i.
    

def degres_sommets(MA):
  n = len(MA)  # nombre de sommets
  degres = []

  for i in range(n):
    # Somme des connexions de la ligne i = degré du sommet i
    degre = sum(MA[i])
    degres.append(degre)

  return degres


# ----- TEST ----- 
print()
print("Fonction 8 : Calculer les degrés des sommets")
MA = creer_matrice(4)
ajouter_arete(MA, 0, 1)
ajouter_arete(MA, 0, 2)
ajouter_arete(MA, 1, 3)

afficher_matrice(MA)

degres = degres_sommets(MA)
for i, d in enumerate(degres):
    print(f"Sommet {i} : degré {d}")


# --------- Affiche les voisins directs du sommet i (ceux qui sont connectés à i).
    
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


# ----- TEST ----- 
print()
print("Fonction 9 : Afficher le voisinage d’un sommet")
MA = creer_matrice(5)
ajouter_arete(MA, 0, 1)
ajouter_arete(MA, 0, 3)
ajouter_arete(MA, 2, 3)

afficher_matrice(MA)

v = voisinage(MA, 0)
print(f"\nVoisins du sommet 0 : {v}")

v = voisinage(MA, 3)
print(f"Voisins du sommet 3 : {v}")


# --------- Trouve tous les chemins de longueur L entre les sommets i et j.
# --------- Retourne une liste de chemins (chaque chemin est une liste de sommets).

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
    
    
# ----- TEST ----- 
print()
print("Fonction 10 : Afficher l’existence d’un chemin de longueurs L")    
MA = creer_matrice(6) 
ajouter_arete(MA, 0, 1)
ajouter_arete(MA, 0, 3)
ajouter_arete(MA, 1, 2)
ajouter_arete(MA, 1, 3)
ajouter_arete(MA, 2, 4)
ajouter_arete(MA, 3, 4)
ajouter_arete(MA, 3, 5)
ajouter_arete(MA, 4, 5)

chemins_longueur_L(MA, 0, 4, 3)
chemins_longueur_L(MA, 0, 2, 1)
    
# --------- Détecte et affiche s’il existe un chemin ou un cycle eulérien dans le graphe.
# --------- Utilise les fonctions déjà réalisées : degres_sommets, est_connexe.

def tester_eulerien(MA):
  
  # --------- Vérifie si le graphe est connexe : tous les sommets doivent être atteignables à partir d’un seul.
  
  def est_connexe(MA):
    n = len(MA)
    visités = set()

    def dfs(s):
        visités.add(s)
        for voisin in range(n):
            if MA[s][voisin] == 1 and voisin not in visités:
                dfs(voisin)

    # Commencer à partir du sommet 0 (ou n’importe lequel)
    dfs(0)

    if len(visités) == n:
        return True
    else:
        return False

  if not est_connexe(MA):
    print("❌ Le graphe n’est pas connexe → pas de chemin ni cycle eulérien.")
    return

  degres = degres_sommets(MA)
  impairs = [i for i in range(len(degres)) if degres[i] % 2 == 1]

  if len(impairs) == 0:
    print("✅ Le graphe contient un **cycle eulérien** (tous les sommets ont un degré pair).")
  elif len(impairs) == 2:
    print(f"✅ Le graphe contient un **chemin eulérien** (exactement deux sommets ont un degré impair) : {impairs}.")
  else:
    print(f"❌ Le graphe n’a **ni chemin ni cycle eulérien** (sommets de degré impair : {len(impairs)}) : {impairs}.")

 
# ----- TEST ----- 
print()
print("Fonction 11 : Afficher un cycle et un chemin eulérien") 
MA = creer_matrice(6) 
ajouter_arete(MA, 0, 1)
ajouter_arete(MA, 0, 3)
ajouter_arete(MA, 1, 2)
ajouter_arete(MA, 1, 3)
ajouter_arete(MA, 2, 4)
ajouter_arete(MA, 3, 4)
ajouter_arete(MA, 3, 5)
ajouter_arete(MA, 4, 5)

afficher_matrice(MA)
tester_eulerien(MA)

supprimer_arete(MA, 1, 3)
supprimer_arete(MA, 4, 3)
tester_eulerien(MA)

ajouter_arete(MA, 0, 5)
tester_eulerien(MA)

ajouter_sommet(MA)
afficher_matrice(MA)
tester_eulerien(MA)







