from tools import *
from datetime import date

#  Partie 3 : Retirer Argent
#   - Vérifier que le montant demandé est disponible
#   - Décomposer le montant en billets (ex. 50€, 20€, 10€, 5€)
#   - Mettre à jour le solde du compte

def retirer_argent(client):
    print("=== Retrait d'argent ===")
    while True:
        montant_str = input("Entrez le montant à retirer (multiple de 5) : ").strip()

        if montant_str.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !\n")
            return

        try:
            montant = float(montant_str)
        except ValueError:
            print("Erreur : vous devez entrer un nombre.\n")
            continue

        if montant <= 0:
            print("Le montant doit être supérieur à 0.\n")
            continue

        if montant % 5 != 0:
            print("Le montant doit être un multiple de 5 (5, 10, 20, 50...).\n")
            continue

        if montant > client[3]:
            print("Fonds insuffisants pour ce retrait.\n")
            continue

        break

   
    billets = [50, 20, 10, 5]
    reste = montant
    decomposition = {}
    for b in billets:
        nb = int(reste // b)
        if nb > 0:
            decomposition[b] = nb
            reste -= nb * b

    print("\nBillets distribués :")
    for valeur, nombre in decomposition.items():
        print(f" - {nombre} x {valeur}€")

    confirm = input(f"\nConfirmer le retrait de {montant:.2f} € ? (o/n) : ").strip().lower()
    if confirm not in ("o", "oui", "y", "yes"):
        print("Retrait annulé.\n")
        return

    today = str(date.today())
    client[3] -= montant
    client[5].extend([montant, today])

    print(f"\nRetrait de {montant:.2f} € effectué avec succès.")
    print(f"Nouveau solde : {client[3]:.2f} €\n")

    sauvegarder_clients()


# -----------------------------
# FONCTION PRINCIPALE
# -----------------------------
def main():
    afficher_message_bienvenue()

# Accueil

    pin = demander_code_pin()        
    if pin is None:
        return

# Partie 1 : S'identifier avec un code PIN

    client = trouver_client_par_pin(pin)
    if not client:
        print("Erreur : client introuvable.\n")
        return

# Partie 2 : Consulter le solde disponible du compte

    afficher_solde(client)

    print("=== Menu ===")
    print("1. Retirer de l'argent")
    print("2. Déposer de l'argent")

    while True:
        choix_str = input("Tapez 1 pour retirer, 2 pour déposer : ").strip()

# Partie 5 : Quitter le programme

        if choix_str.lower() in quitting_words:
            print("\nVous avez quitté le programme, à bientôt !\n")
            return

        if not choix_str.isdigit():
            print("Choix invalide. Tapez 1 pour retirer, 2 pour déposer :")
            continue

        choix = int(choix_str)
        if choix == 1:

 # Partie 3 : Retirer argent

            retirer_argent(client)
            break
        elif choix == 2:

# Partie 4 : Déposer argent

            deposer_argent(client)
            break
        else:
            print("Choix invalide. Tapez 1 pour retirer, 2 pour déposer :")

# Partie 5 : Quitter le programme
    afficher_message_aurevoir()


if __name__ == "__main__":
    main()
