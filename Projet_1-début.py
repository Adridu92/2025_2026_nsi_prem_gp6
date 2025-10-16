class CompteBancaire:
    def __init__(self, numero_carte, pin, solde=0):
        self.numero_carte = numero_carte
        self.pin = pin
        self.solde = solde
        self.releves = []

    def deposer(self, montant):
        self.solde += montant
        self.releves.append(f"Dépôt de {montant}€")
        return self.solde

    def retirer(self, montant):
        if montant > self.solde:
            return "Solde insuffisant"
        self.solde -= montant
        self.releves.append(f"Retrait de {montant}€")
        return self.solde

    def consulter_solde(self):
        return self.solde

    def consulter_releves(self):
        return self.releves

    def changer_pin(self, ancien_pin, nouveau_pin):
        if self.pin == ancien_pin:
            self.pin = nouveau_pin
            return "PIN changé avec succès"
        return "Ancien PIN incorrect"

class DAB:
    def __init__(self):
        self.comptes = {}

    def ajouter_compte(self, numero_carte, pin, solde=0):
        self.comptes[numero_carte] = CompteBancaire(numero_carte, pin, solde)

    def authentifier(self, numero_carte, pin):
        compte = self.comptes.get(numero_carte)
        if compte and compte.pin == pin:
            return compte
        return None

def main():
    dab = DAB()
    dab.ajouter_compte("123456789", "1234", 1000)

    print("Bienvenue au DAB")
    numero_carte = input("Entrez votre numéro de carte : ")
    pin = input("Entrez votre PIN : ")

    compte = dab.authentifier(numero_carte, pin)
    if compte:
        print("Authentification réussie")
        while True:
            print("\n1. Dépôt")
            print("2. Retrait")
            print("3. Consulter solde")
            print("4. Consulter relevés")
            print("5. Changer PIN")
            print("6. Quitter")
            choix = input("Choisissez une option : ")

            if choix == "1":
                montant = float(input("Entrez le montant à déposer : "))
                nouveau_solde = compte.deposer(montant)
                print(f"Nouveau solde : {nouveau_solde}€")
            elif choix == "2":
                montant = float(input("Entrez le montant à retirer : "))
                nouveau_solde = compte.retirer(montant)
                if isinstance(nouveau_solde, str):
                    print(nouveau_solde)
                else:
                    print(f"Nouveau solde : {nouveau_solde}€")
            elif choix == "3":
                print(f"Solde actuel : {compte.consulter_solde()}€")
            elif choix == "4":
                print("Relevés :")
                for releve in compte.consulter_releves():
                    print(releve)
            elif choix == "5":
                ancien_pin = input("Entrez votre ancien PIN : ")
                nouveau_pin = input("Entrez votre nouveau PIN : ")
                print(compte.changer_pin(ancien_pin, nouveau_pin))
            elif choix == "6":
                print("Merci d'avoir utilisé le DAB")
                break
            else:
                print("Option invalide")
    else:
        print("Authentification échouée")

if __name__ == "__main__":
    main()