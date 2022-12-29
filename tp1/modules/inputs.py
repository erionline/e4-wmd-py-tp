def dataChange(text, dataActuelle):
    """Demande et gère la donnée entrée """
    userInput = input(f"{text}\nPour conserver la donnée actuelle, tapez 1 : ").strip()

    if len(userInput) < 1:
        print("Aucune donnée entrée, le champ ne peut-être vide, la donnée actuelle est conservée")
        return dataActuelle

    if userInput == dataActuelle:
        print("La donnée entrée est identique à la donnée actuelle, la donnée actuelle est conservée")
        return dataActuelle

    if userInput == "1":
        print("La donnée actuelle est conservée")
        return dataActuelle

    return userInput

def yesNo(text):
    """Pose une question et attend une réponse oui ou non"""
    userInput = input(f"{text} (oui/non) : ").strip().lower()

    if userInput == "oui":
        return True
    elif userInput == "non":
        return False
    else:
        print("La réponse entrée est invalide, veuillez réessayer")
        return yesNo(text)
