
from tools import *
from databank import *
from datetime import date
   
def main():
    print("Bonjour ! Bienvenue au distributeur automatique de billets.\n")
    
    # Demander le code PIN
    pin = demander_code_pin()
    
    # Si l'utilisateur a quitté
    if pin is None:
        return
    
    # Trouver le client correspondant au PIN
    client = trouver_client_par_pin(pin)
    
    if client:
        # Afficher le solde
        afficher_solde(client)
        
        # Afficher le menu
        print("=== Menu ===")
        print("1. Retirer de l'argent")
        print("2. Déposer de l'argent")
        
        try:
            choix = float(input("Tapez 1 pour retirer de l'argent, 2 pour en déposer : "))
            
            if choix == 1:
                retirer_argent(client)
            elif choix == 2:
                deposer_argent(client)
            else:
                print("Choix invalide.\n")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.\n")
    else:
        print("Erreur : client introuvable.\n")
    
    afficher_message_aurevoir()


def retirer_argent(client):
    """
    Partie 3 Retirer de l'argent.
    client : liste [pin, prenom, nom, solde, depots, retraits]
    Vérifie que le montant est valide, multiple de 5 et <= solde.
    Met à jour le solde du client et enregistre la transaction avec la date du jour.
    """
    print("=== Retrait d'argent ===")

    try:
        montant = float(input("Entrez le montant à retirer (en euros, multiple de 5) : "))
    except ValueError:
        print("Erreur : vous devez entrer un nombre.\n")
        return

    # Vérification de validité
    if montant <= 0:
        print("Le montant doit être supérieur à 0.\n")
        return
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 (5, 10, 20, 50...).\n")
        return
    if montant > client[3]:
        print("Fonds insuffisants pour effectuer ce retrait.\n")
        return

    # Décomposition en billets
    billets = [50, 20, 10, 5]
    reste = montant
    decomposition = {}
    for b in billets:
        nb = int(reste // b)
        if nb > 0:
            decomposition[b] = nb
            reste -= nb * b

    # Affichage des billets distribués
    print("Billets distribués :")
    for valeur, nombre in decomposition.items():
        print(f" - {nombre} x {valeur}€")

    # Confirmation
    confirm = input(f"Confirmer le retrait de {montant:.2f} € ? (o/n) : ").strip().lower()
    if confirm not in ("o", "oui", "y", "yes"):
        print("Retrait annulé.\n")
        return

    # Mise à jour du solde et enregistrement du retrait
    today = str(date.today())
    client[3] -= montant
    client[5].extend([montant, today])  # Index 5 = retraits

    print(f"Retrait de {montant:.2f} € effectué avec succès.")
    print(f"Nouveau solde de {client[1]} {client[2]} : {client[3]:.2f} €\n")


main()