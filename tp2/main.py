from ferme import Ferme
from utils import ajouter_animal, crier, tuer, afficher_nombre_animaux, quitter

# Création de la ferme
ferme = Ferme()

while True:
    print("""
1: Ajouter un animal
2: Lancer le cri de tous les animaux de la ferme
3: Tuer un animal
4: Afficher le nombre d'animaux dans la ferme
5: Quitter le programme
    """)

    choice = input("Entrez votre choix : ")
    if choice == "1":
        ajouter_animal(ferme)
    elif choice == "2":
        crier(ferme)
    elif choice == "3":
        tuer(ferme)
    elif choice == "4":
        afficher_nombre_animaux(ferme)
    elif choice == "5":
        quitter()
    else:
        print("🛑 Veuillez entrer un choix valide.")