# Ecrivez un programme qui prend en entrée un fichier csv contenant des informations sur plusieurs personnes, 
# chacune sur une ligne différente, sous la forme "nom, prénom, âge, ville". 
# Le programme doit lire ce fichier et créer un dictionnaire pour chaque personne, 
# avec les informations du fichier en tant que valeurs associées aux clés "nom", "prenom", "age" et "ville".

# Le programme doit ensuite afficher un menu permettant à l'utilisateur de :
	
# - Afficher la liste de toutes les personnes enregistrées, sous la forme "nom prénom, âge ans, ville"
# - Ajouter une nouvelle personne en saisissant les informations au clavier
# - Modifier les informations d'une personne en saisissant son nom et en modifiant les informations souhaitées
# - Supprimer une personne en saisissant son nom

import modules.checker as checker
import modules.file as file
import modules.inputs as inputs

fichier = input("👋 Bienvenue dans le programme de gestion de fichier CSV !\n\nEntrez le chemin du fichier pour commencer : ")

# Vérifie si le fichier existe
checker.doesFileExists(fichier)

# Ouvre le fichier en mode lecture
data = checker.readFileLines(fichier)

# Vérifie si les clés du fichier sont correctes
checker.checkFileKeysAreCorrect(fichier, ["nom", "prenom", "age", "ville"])

def printFileContent():
    """Affiche la liste des personnes"""
    # Pour chaque dictionnaire de la liste
    print(f"Liste des personnes ({len(data)} résultat(s)): \n\n")
    for d in data:
        # Affiche les informations de la personne
        print(f"{d['nom']} {d['prenom']}, {d['age']} ans, {d['ville']}")
    print("\n")

def addPerson():
    """Ajoute une personne"""
    # Demande le nom de la personne
    nom = input("Entrez le nom de la personne : ")
    while not checker.checkNameEntry(nom):
        nom = input("Entrez le nom de la personne : ")
    # Demande le prénom de la personne
    prenom = input("Entrez le prénom de la personne : ")
    while not checker.checkNameEntry(prenom):
        prenom = input("Entrez le prénom de la personne : ")
    # Demande l'âge de la personne
    age = input("Entrez l'âge de la personne : ")
    while not checker.checkAgeEntry(age):
        age = input("Entrez l'âge de la personne : ")
    # Demande la ville de la personne
    ville = input("Entrez la ville de la personne : ")
    while not checker.checkNameEntry(ville):
        ville = input("Entrez la ville de la personne : ")

    # Ajoute la personne à la liste
    data.append({"nom": nom, "prenom": prenom, "age": age, "ville": ville})
    file.writeToFile(data, fichier)

    print(f"🎉 Personne ajoutée !\nLes données qui lui correspondent : {nom} {prenom}, {age} ans, {ville}")

def modifyPerson():
    """Cherche une personne par son nom et modifie ses informations"""
    # Demande le nom de la personne
    nom = input("Entrez le nom de la personne : ")

    # Cherche la personne dans la liste
    for d in data:
        # Si le nom de la personne est trouvé
        if d["nom"].strip().lower() == nom.strip().lower():
            print(f"🎉 Personne trouvée !\n Les données qui lui correspondent : {d['nom']} {d['prenom']}, {d['age']} ans, {d['ville']}")

            # Demande à nouveau le nom de la personne, dans le cas où on souhaite le modifier
            nom = inputs.dataChange("Entrez le nom de la personne.", d["nom"])
            while not checker.checkNameEntry(nom):
                nom = inputs.dataChange("Entrez le nom de la personne.", d["nom"])
            # Demande le prénom de la personne
            prenom = inputs.dataChange("Entrez le prénom de la personne.", d["prenom"])
            while not checker.checkNameEntry(prenom):
                prenom = inputs.dataChange("Entrez le prénom de la personne.", d["prenom"])
            # Demande l'âge de la personne
            age = inputs.dataChange("Entrez l'âge de la personne.", d["age"])
            while not checker.checkAgeEntry(age):
                age = inputs.dataChange("Entrez l'âge de la personne.", d["age"])
            # Demande la ville de la personne
            ville = inputs.dataChange("Entrez la ville de la personne.", d["ville"])
            while not checker.checkNameEntry(ville):
                ville = inputs.dataChange("Entrez la ville de la personne.", d["ville"])

            # Modifie les informations de la personne
            d["nom"] = nom
            d["prenom"] = prenom
            d["age"] = age
            d["ville"] = ville

            file.writeToFile(data, fichier)

            return print(f"🎉 Personne modifiée !\nLes nouvelles données qui lui correspondent : {nom} {prenom}, {age} ans, {ville}")

    print("🛑 Personne non trouvée. Veuillez réessayer.")

def deletePerson():
    """Cherche une personne par son nom et la supprime"""
    # Demande le nom de la personne
    nom : str = input("Entrez le nom de la personne : ")

    # Cherche la personne dans la liste
    for d in data:
        # Si le nom de la personne est trouvé
        if d["nom"].lower() == nom.lower():
            print(f"🎉 Personne trouvée !\n Les données qui lui correspondent : {d['nom']} {d['prenom']}, {d['age']} ans, {d['ville']}")

            # Demande la confirmation de la suppression
            if inputs.yesNo("Voulez-vous vraiment supprimer cette personne ?"):
                # Supprime la personne de la liste
                data.remove(d)
                file.writeToFile(data, fichier)

                return print("🎉 Personne supprimée !")

            else:  
                return print("👍 Suppression annulée !")

    print("🛑 Personne non trouvée. Veuillez réessayer.")


def interactiveMainMenu():
    """Main menu for the interactive mode"""
    print("""
1. Afficher la liste de toutes les personnes enregistrées
2. Ajouter une nouvelle personne
3. Modifier les informations d'une personne
4. Supprimer une personne
5. Quitter le programme
    """)
    choice = input("Entrez votre choix : ")
    if choice == "1":
        printFileContent()
        interactiveMainMenu()
    elif choice == "2":
        addPerson()
        interactiveMainMenu()
    elif choice == "3":
        modifyPerson()
        interactiveMainMenu()
    elif choice == "4":
        deletePerson()
        interactiveMainMenu()
    elif choice == "5":
        print("Au revoir !")
        exit()
    else:
        print("🛑 Veuillez entrer un choix valide.")
        interactiveMainMenu()

interactiveMainMenu()