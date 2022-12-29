from ferme import Chien,Chat

def ajouter_animal(ferme):
    """Ajoute un animal à la ferme"""
    print("Quel type d'animal voulez-vous ajouter ? (1: Chat, 2: Chien)")
    type_animal = int(input())
    if type_animal == 1:
        classe = Chat
    elif type_animal == 2:
        classe = Chien
    else:
        print("Type d'animal non reconnu")
        return
    print("Entrez le nom de l'animal :")
    nom = input()
    print("Entrez l'âge de l'animal :")
    age = int(input())
    animal = classe(nom, age)
    ferme.ajouter_animal(animal)
    print(f"Le {classe.__name__.lower()} {nom} est né")

def crier(ferme):
    """Fait crier tous les animaux de la ferme"""
    ferme.crier()

def tuer(ferme):
    """Tue un animal de la ferme"""
    print("Entrez le nom de l'animal à tuer :")
    nom = input()
    trouve = False
    for animal in ferme.animaux:
        if animal.nom == nom:
            ferme.animaux.remove(animal)
            print(f"Le {animal.__class__.__name__.lower()} {nom} est mort")
            trouve = True
            break
    if not trouve:
        print("Animal introuvable")

def afficher_nombre_animaux(ferme):
    """Affiche le nombre d'animaux dans la ferme"""
    print(ferme)

def quitter():
    """Quitte le programme"""
    print("Au revoir !")
    exit()
