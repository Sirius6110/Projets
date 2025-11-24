def addition(a, b):
    resultat = a + b
    return resultat

def soustraction(a, b):
    resultat = a - b
    return resultat

def multiplication(a, b):
    resultat = a * b
    return resultat

def division(a, b):
    if b == 0:
        return "Erreur : Impossible de diviser par zéro."
    else:
        resultat = a / b
        return resultat

while True:
    print("\n--------------------------")
    print("Sélectionnez une opération :")
    print("1- Addition")
    print("2- Soustraction")
    print("3- Multiplication")
    print("4- Division")
    print("5- Quitter")
    print("--------------------------")
    
    choix = input("Votre choix (1/2/3/4/5): ")

    if choix == "5":
        print("Fin du programme.")
        break
    
    elif choix in ("1", "2", "3", "4"):
        try:
            nombre1 = float(input("Premier nombre = "))
            nombre2 = float(input("Deuxième nombre = "))
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            continue
            
        resultat_calcul = None
        
        if choix == "1":
            resultat_calcul = addition(nombre1, nombre2)
            operation_symbole = "+"
        elif choix == "2":
            resultat_calcul = soustraction(nombre1, nombre2)
            operation_symbole = "-"
        elif choix == "3":
            resultat_calcul = multiplication(nombre1, nombre2)
            operation_symbole = "*"
        elif choix == "4":
            resultat_calcul = division(nombre1, nombre2)
            operation_symbole = "/"

        print(f"\nRésultat : {nombre1} {operation_symbole} {nombre2} = {resultat_calcul}")
            
    else:
        print("Choix invalide. Veuillez sélectionner une option entre 1 et 5.")