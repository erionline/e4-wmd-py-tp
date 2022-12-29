class Animal:
    """Classe représentant un animal"""
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def cri(self):
        pass

class Chat(Animal):
    """Classe représentant un chat"""
    def cri(self):
        """Retourne le cri du chat"""
        return "Miaou"

class Chien(Animal):
    """Classe représentant un chien"""
    def cri(self):
        """Retourne le cri du chien"""
        return "Ouaf"

class Ferme:
    """Classe représentant une ferme"""
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        """Ajoute un animal à la ferme"""
        self.animaux.append(animal)

    def crier(self):
        """Fait crier tous les animaux de la ferme"""
        for animal in self.animaux:
            print(animal.cri())

    def __str__(self):
        return f"Ferme avec {len(self.animaux)} animaux"