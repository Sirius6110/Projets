import random
import string
from typing import Tuple, List, Optional

MINUSCULES = string.ascii_lowercase
MAJUSCULES = string.ascii_uppercase
CHIFFRES = string.digits
SPECIAUX = string.punctuation

def obtenir_longueur() -> int:
    while True:
        try:
            longueur = int(input("Quelle longueur souhaitez-vous pour le mot de passe (nombre entier) ? "))
            if longueur > 0:
                return longueur
            else:
                print("Veuillez entrer un nombre positif.")
        except ValueError:
            print("Saisie invalide. Veuillez entrer un nombre entier.")

def obtenir_option(question: str) -> bool:
    while True:
        reponse = input(question + " (oui/non) : ").strip().lower()
        if reponse == "oui":
            return True
        elif reponse == "non":
            return False
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

def construire_pool_et_requis(inclure_chiffres: bool, inclure_speciaux: bool) -> Optional[Tuple[str, List[str]]]:
    pool_total = MINUSCULES + MAJUSCULES
    caracteres_requis = []

    if inclure_chiffres:
        pool_total += CHIFFRES
        caracteres_requis.append(random.choice(CHIFFRES))
        print("Chiffres inclus.")
    else:
        print("Chiffres exclus.")

    if inclure_speciaux:
        pool_total += SPECIAUX
        caracteres_requis.append(random.choice(SPECIAUX))
        print("Caractères spéciaux inclus.")
    else:
        print("Caractères spéciaux exclus.")

    if not pool_total:
        print("Erreur : Aucun type de caractère n'a été sélectionné. Impossible de générer un mot de passe.")
        return None

    return pool_total, caracteres_requis

def generer_mot_de_passe():
    longueur = obtenir_longueur()
    inclure_speciaux = obtenir_option("Souhaitez-vous inclure des caractères spéciaux ?")
    inclure_chiffres = obtenir_option("Souhaitez-vous inclure des chiffres ?")

    resultats = construire_pool_et_requis(inclure_chiffres, inclure_speciaux)

    if resultats is None:
        return

    pool_de_caracteres, caracteres_requis = resultats
    
    nb_requis = len(caracteres_requis)
    if nb_requis > longueur:
        print(f"\nErreur : La longueur demandée ({longueur}) est insuffisante pour inclure {nb_requis} caractères requis.")
        print("Veuillez choisir une longueur supérieure ou désactiver certaines options.")
        return

    mot_de_passe_liste = caracteres_requis[:]
    longueur_restante = longueur - nb_requis
    
    for _ in range(longueur_restante):
        caractère_aleatoire = random.choice(pool_de_caracteres)
        mot_de_passe_liste.append(caractère_aleatoire)
    
    random.shuffle(mot_de_passe_liste)
    mot_de_passe_final = "".join(mot_de_passe_liste)

    print("\n" + "=" * 40)
    print(" " * 6 + "MOT DE PASSE GÉNÉRÉ AVEC SUCCÈS")
    print("=" * 40)
    print(f"Longueur demandée : {longueur}")
    print(f"Diversité garantie : {nb_requis} caractères forcés inclus.")
    print(f"VOTRE MOT DE PASSE : {mot_de_passe_final}")
    print("=" * 40)

if __name__ == "__main__":
    generer_mot_de_passe()