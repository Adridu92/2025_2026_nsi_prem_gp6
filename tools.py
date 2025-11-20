import json
from datetime import date
import os
import databank

# Liste des codes PIN valides
pins_valides = [1013, 1023, 1033, 1043, 1063, 1073, 1093, 1193]
# Liste des mots-clés pour quitter le programme
quitting_words = ["quit", "ciao", "byebye", "au revoir", "adios"]

# Charger la base depuis JSON si elle existe
if os.path.exists("databank.json"):
    with open("databank.json", "r") as f:
        clients = json.load(f)
else:
    clients = databank.clients  # sinon base par défaut

# -----------------------------
# FONCTIONS
# -----------------------------
def afficher_message_bienvenue():
    print("Bonjour ! Bienvenue au distributeur automatique de billets.\n")

def demander_code_pin():
    while True:
        code_saisi = input("Entrez votre code PIN (ou tapez 'quit' pour quitter) : ").strip()
        if code_saisi.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !")
            return None
        if not code_saisi.isdigit():
            print("\nVous devez entrer un nombre pour le code PIN.\n")
            continue
        code = int(code_saisi)
        if code in pins_valides:
            print("\nPIN correct. Accès autorisé.\n")
            return code
        else:
            input("\nLe code PIN est mauvais. Réessayez.\n")

def afficher_message_aurevoir():
    print("Merci d'avoir utilisé notre DAB, au revoir !")

def afficher_solde(client):
    prenom = client[1]
    nom = client[2]
    solde = client[3]
    print(f"Solde actuel de {prenom} {nom} : {solde} €\n")

def trouver_client_par_pin(pin):
    for client in clients:
        if client[0] == str(pin):
            return client
    return None

def deposer_argent(client):
    print("=== Dépôt d'argent ===")
    while True:
        montant_str = input("Entrez le montant à déposer : ").strip()
        if montant_str.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !")
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
    print(f"Dépôt de {montant:.2f} € effectué avec succès.")
    print(f"Nouveau solde de {client[1]} {client[2]} : {client[3]:.2f} €\n")
    sauvegarder_clients()

def sauvegarder_clients():
    with open("databank.json", "w") as f:
        json.dump(clients, f, indent=4)
