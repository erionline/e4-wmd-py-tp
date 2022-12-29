import os

def doesFileExists(filePath):
    """Vérifie si le fichier existe"""
    if os.path.isfile(filePath):
        return True
    else:
        print("Le fichier que vous avez saisie n'existe pas. Veuillez réessayer.")
        exit()

def readFileLines(filePath):
    """Lit le fichier et retourne un liste de dictionnaires de chaque lignes du fichier"""
    with open(filePath, "r", encoding='utf-8-sig') as file:
        try:
            lignes = file.readlines()
            resultats = []
            for ligne in lignes:
                if ligne == lignes[0] and ligne.startswith("nom"):
                    # Si la première ligne du fichier énonce les clés : "nom;prenom;age;ville"
                    # On passe à la ligne suivante
                    continue
                res = ligne.replace("\n", "").split(";" if ";" in ligne else ",")
                dictUser = {
                    "nom": res[0].strip().capitalize(),
                    "prenom": res[1].strip().capitalize(),
                    "age": res[2].strip(),
                    "ville": res[3].strip().capitalize()
                }
                resultats.append(dictUser)
        except Exception as e:
            print(f"Le fichier est vide ou ne peut-être lu : {e}")
            exit()
    return resultats

def checkFileKeysAreCorrect(filePath, keys):
    """Vérifie si les clés du fichier sont correctes"""
    # Ouvre le fichier en mode lecture
    lignes = readFileLines(filePath)
    # Pour la première ligne du fichier CSV
    ligne = lignes[0]
    # Pour chaque clé du fichier
    for key in keys:
        # Si la clé n'est pas dans la valeur 
        if not key.strip() in ligne:
            # Affiche un message d'erreur
            print(f"La clé {key} n'est pas présente dans le fichier {filePath}. Veuillez réessayer.")
            # Quitte le programme
            exit()

def checkNameEntry(name: str):
    """Vérifie si le nom entré est un nom valide"""
    # Supprimer les espaces avant et après le nom entré
    name = name.strip()
    print(name)

    # Si le nom n'est pas vide, trop court ou trop long
    if len(name) <= 1 or len(name) > 50:
        print("Le nom que vous avez entré est trop long ou trop court. Veuillez réessayer.")
        return False
    
    # Si le nom contient des caractères spéciaux
    if not name.isalpha():
        print("Le nom que vous avez entré est invalide. Veuillez réessayer.")
        return False

    return True

def checkAgeEntry(age: str):
    """Vérifie si l'âge entré est un âge valide"""
    # Si l'âge n'est pas un nombre
    if not age.isnumeric():
        print("L'âge que vous avez entré est invalide. Veuillez réessayer.")
        return False

    age = int(age)
    
    # Si l'âge est inférieur à 0 ou supérieur à 130
    if age <= 0 or age > 130:
        print("L'âge que vous avez entré est invalide. Veuillez réessayer.")
        return False

    return True

def checkCityEntry(city: str):
    """Vérifie si la ville entrée est une ville valide"""
    # Supprimer les espaces avant et après la ville entrée
    city = city.strip()

    # Si la ville n'est pas vide, trop courte ou trop longue
    if len(city) < 1 and len(city) > 50:
        print("La ville que vous avez entrée est trop longue ou trop courte. Veuillez réessayer.")
        return False

    return True
