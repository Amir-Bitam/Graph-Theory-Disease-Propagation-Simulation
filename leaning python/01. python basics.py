# #------------ Variables ---------------
# nom = "Amir"                                      # chaîne de caractères (str)
# age = 23                                          # entier (int)
# print ("bonjour je m'apple",nom + " j'ai",age)    # bonjour je m'apple Amir j'ai 23
# print(type(nom))                                  # <class 'str'>

# #------------ Conditions ---------------

# age = int(input("donne ton age batard\n"))
# if age < 18:
#   print("walah maedkhol")
# else:
#   print("hehehe ma7ba camarade")

# #------------ Boucles ---------------

# i = 1
# while i < 11:
#   print(i)
#   i += 1

# i = 0 
# for i in range(1, 11):
#   print(i)

# for i in range(2,21):
#   if i % 2 == 0:
#     print(i)
    
    
# mdp = ""
# while mdp != "secret":
#   mdp = input("doone mdp: ")
  
# print("mdp correct")

#------------ Listes ---------------

# fruits = ["pomme", "bannane", "orange"]

# for i in fruits:
#   print(i)
# print(len(fruits))  
# fruits.append("kiwi")

# print("\n")
# for i in fruits:
#   print(i)
# print(len(fruits))  
# fruits.remove("bannane")

# print("\n")
# for i in fruits:
#   print(i)
# print(len(fruits))  

films = []

print("🎬 Donne-moi tes 3 films préférés :")
for i in range(1, 4):
    film = input(f"{i}. Film : ").strip()
    films.append(film)

print("\n📽️ Voici tes films préférés :")
for index, film in enumerate(films, start=1):
    print(f"{index}. Tu kiff le film : {film}")