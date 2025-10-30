from databank import *
import json
def pin_good():
    pin = [1013, 1023, 1033, 1043, 1063, 1073, 1093, 1193 ]
         


def message_de_bienvenue():
    print("Bonjour ! Bienvenue au distributeur automatique de billets.")

def entrer_code_pin():
    while True:
        demande_id = input("Entrez votre code PIN (ou tapez 'quit' pour quitter) : ")
        
        if demande_id.lower() in quitting_words:
            print("Vous avez quitté le programme, à bientôt !")
            return None
        
        try:
            code = int(demande_id)
            if code in pins_valides:
                print("PIN correct. Accès autorisé.\n")
                return code  
            else:
                print("PIN incorrect. Réessayez.\n")
        except:
            print("Vous devez entrer un nombre pour le code PIN.\n")


def message_aurevoir()
    print("Merci d'avoir utilisé notre DAB, au revoir !")