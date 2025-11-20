import json

import databank

# Liste des codes PIN valides
pins_valides = [1013, 1023, 1033, 1043, 1063, 1073, 1093, 1193]

# Liste des mots-clés pour quitter le programme
quitting_words = ["quit", "ciao", "byebye", "au revoir", "adios"]

# Base de données des clients (Data Bank)
clients = [
    ["1013", "Manuel", "Macaron", 999999, [10000, "2025-10-05", 12000, "2025-10-02"], []],
    ["1033", "Christian", "Goataldo", 10023, [1300, "2025-10-03", 1200, "2025-10-02"], [200, "2025-09-04"]],
    ["1023", "Hadrien", "Raisingay", 12, [1, "2025-10-03", 2, "2025-10-01"], [1, "2025-10-06"]],
    ["1043", "Leon", "Moisi", 0, [1, "2025-10-03", 1, "2025-10-02"], [2, "2025-10-04"]],
    ["1073", "Marin", "Pêcheur", 1200, [700, "2025-10-01", 600, "2025-10-03"], [300, "2025-10-05"]],
    ["1063", "Jean", "clenchetasoeur", 8000, [500, "2025-10-02"], [150, "2025-10-04"]],
    ["1093", "Alban", "Boulard", 1500, [100, "2025-10-03"], [75, "2025-10-04"]],
    ["1193", "Xi", "jinping", 240000000, [100000, "2025-10-03"], [75000, "2025-10-04"]]
]

# Fonction qui affiche un message de bienvenue
def afficher_message_bienvenue():
    print("Bonjour ! Bienvenue au distributeur automatique de billets.\n")

# Fonction qui demande à l'utilisateur d'entrer un code PIN
def demander_code_pin():
    while True:
        # Demande à l'utilisateur d'entrer son code PIN
        code_saisi = input("Entrez votre code PIN (ou tapez 'quit' pour quitter) : ")

        # Si l'utilisateur veut quitter
        if code_saisi.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !")
            return None
        
        try:
            # Convertir le code PIN en entier et vérifier s'il est valide
            code = int(code_saisi)
            if code in pins_valides:
                print("PIN correct. Accès autorisé.\n")
                return code
            else:
                print("PIN incorrect. Réessayez.\n")
        except ValueError:
            print("Vous devez entrer un nombre pour le code PIN.\n")

# Fonction qui affiche un message de départ
def afficher_message_aurevoir():
    print("Merci d'avoir utilisé notre DAB, au revoir !")

# Fonction qui affiche le solde du client
def afficher_solde(client):
    prenom = client[1]
    nom = client[2]
    solde = client[3]
    print(f"Solde actuel de {prenom} {nom} : {solde} €\n")

# Fonction qui trouve un client à partir de son code PIN
def trouver_client_par_pin(pin):
    for client in clients:
        if client[0] == str(pin):  # Le PIN est enregistré sous forme de chaîne
            return client
    return None

# Fonction principale qui contrôle le flux du programme
def main():
    afficher_message_bienvenue()

    pin = demander_code_pin()
    if pin is None:
        return

    client = trouver_client_par_pin(pin)
    if client:
        afficher_solde(client)
    else:
        print("Erreur : client introuvable.\n")

    afficher_message_aurevoir()

# Si ce script est exécuté directement, on appelle la fonction principale
if __name__ == "__main__":
    main()

def menu ():
    print ("Que voulez-vous faire ?")
    print ("1 - Consulter mon solde")
    print ("2 - Déposer de l'argent")
    print ("3 - Retirer de l'argent")

def user_continues(n):
    return n not in quitting_words