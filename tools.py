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
        code_saisi = input("Entrez votre code PIN (ou tapez 'quit' pour quitter) : ")

        # Si l'utilisateur veut quitter
        if code_saisi.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !")
            return None

        # Vérifier que c’est bien un nombre
        if not code_saisi.isdigit():
            print("\n Vous devez entrer un nombre pour le code PIN.\n")
            continue

        # Convertir en entier pour comparaison
        code = int(code_saisi)

        # Vérifier si le code est valide
        if code in pins_valides:
            print("\n PIN correct. Accès autorisé.\n")
            return code
        else:
            # 🔹 Ici ton message d’erreur apparaît toujours
            input("\n Le code PIN est mauvais. Réessayez.\n")

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

from datetime import date

# Demande du montant en boucle jusqu'à ce qu'il soit valide
while True:
    try:
        montant = float(input("Entrez le montant à déposer : "))
        if montant <= 0:
            print("Le montant doit être supérieur à 0.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un montant valide.")

# Mise à jour du solde et enregistrement du dépôt
today = str(date.today())
client[3] += montant
client[5].append(["dépôt", montant, today])

print(f"Dépôt de {montant:.2f} € effectué avec succès.")
print(f"Nouveau solde de {client[1]} {client[2]} : {client[3]:.2f} €\n")