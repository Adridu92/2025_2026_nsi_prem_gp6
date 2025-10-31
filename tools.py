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

def déposer_argent(montant)
    client["depots"].append([montant, today])
    print("Dépôt effectué avec succès !")
    print(f" Nouveau solde de {client['prenom']} {client['nom']} : {client['solde']} €")

def get_clients_base():
    if file_doesnt_exist("clients.json"):
        clients_dict = make_clients_from_data(raw_clients)
        save_python_dict_to_json_file(clients_dict, "clients.json")
    else:
        clients_dict = make_python_dict_from_json_file("clients.json")
    return clients_dict






from databank import *
import json

def pin_good():
    pin = [1013, 1023, 1033, 1043, 1063, 1073, 1093, 1193]
    # pour l'instant cette fonction ne fait rien mais on pourra la réutiliser plus tard
         

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


def message_aurevoir():
    print("Merci d'avoir utilisé notre DAB, au revoir !")

def déposer_argent(montant):
    client["depots"].append([montant, today])
    print("Dépôt effectué avec succès !")
    print(f" Nouveau solde de {client['prenom']} {client['nom']} : {client['solde']} €")

def trouver_client_par_pin(pin):
    for client in clients:
        if client[0] == str(pin):  # dans databank, les PIN sont des chaînes
            return client
    return None

def consulter_solde(client):
    prenom = client[1]
    nom = client[2]
    solde = client[3]
    print(f"Solde actuel de {prenom} {nom} : {solde} €\n")

def get_clients_base():
    if file_doesnt_exist("clients.json"):
        clients_dict = make_clients_from_data(raw_clients)
        save_python_dict_to_json_file(clients_dict, "clients.json")
    else:
        clients_dict = make_python_dict_from_json_file("clients.json")
    return clients_dict


def main():
    message_de_bienvenue()

    pin = entrer_code_pin()
    if pin is None:  # si l'utilisateur quitte
        return

    client = trouver_client_par_pin(pin)
    if client:
        consulter_solde(client)
    else:
        print("Erreur : client introuvable.\n")

    message_aurevoir()


if __name__ == "__main__":
    main()
