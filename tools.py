import json
from datetime import date
import os
import databank


# CONSIGNE 1 : S'identifier avec un code PIN (fictif et enregistré dans le programme)
pins_valides = [1013, 1023, 1033, 1043, 1063, 1073, 1093, 1193]
quitting_words = ["quit", "ciao", "byebye", "au revoir", "adios"]


if os.path.exists("databank.json"):
    with open("databank.json", "r") as f:
        clients = json.load(f)
else:
    clients = databank.clients



# FONCTIONS d'interface

def afficher_message_bienvenue():
    print("Bonjour ! Bienvenue au distributeur automatique de billets.\n")


def afficher_message_aurevoir():
    print("Merci d'avoir utilisé notre DAB, au revoir !\n")

# Partie 1 : S'identifier avec un code PIN (fictif et enregistré dans le programme)

def demander_code_pin():
    while True:
        code_saisi = input("Entrez votre code PIN (ou tapez 'quit' pour quitter) : ").strip()

        if code_saisi.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !\n")
            return None

        if not code_saisi.isdigit():
            print("\nLe code PIN doit être un nombre.\n")
            continue

        code = int(code_saisi)
        if code in pins_valides:
            print("\nPIN correct. Accès autorisé.\n")
            return code
        else:
            print("\nCode PIN incorrect. Réessayez.\n")
            continue


def trouver_client_par_pin(pin):
    for client in clients:
        if client[0] == str(pin):
            return client
    return None

# Partie 2 : Consulter le solde disponible du compte

def afficher_solde(client):
    prenom = client[1]
    nom = client[2]
    solde = client[3]
    print(f"Solde actuel de {prenom} {nom} : {solde:.2f} €\n")

# Partie 4 : Déposer de l'argent et mettre à jour le solde

def deposer_argent(client):
    print("=== Dépôt d'argent ===")
    while True:
        montant_str = input("Entrez le montant à déposer : ").strip()

        if montant_str.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !\n")
            return

        try:
            montant = float(montant_str)
        except ValueError:
            print("Veuillez entrer un montant valide.\n")
            continue

        if montant <= 0:
            print("Le montant doit être supérieur à 0.\n")
            continue
        break

    today = str(date.today())
    client[3] += montant
    client[4].extend([montant, today])

    print(f"\nDépôt de {montant:.2f} € effectué avec succès.")
    print(f"Nouveau solde de {client[1]} {client[2]} : {client[3]:.2f} €\n")

    sauvegarder_clients()


def sauvegarder_clients():
    """Sauvegarde les données dans databank.json"""
    with open("databank.json", "w") as f:
        json.dump(clients, f, indent=4)
