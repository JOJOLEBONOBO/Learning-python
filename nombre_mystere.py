import random
import matplotlib.pyplot as plt
import os 

dossier_du_jeu = os.path.dirname(os.path.abspath(__file__))
CHEMIN_FICHIER = os.path.join(dossier_du_jeu, "record.txt")
def afficher_graphique():
    if not os.path.exists(CHEMIN_FICHIER): 
        print("\n Oups ! Le fichier 'record.txt' n'existe pas encore.")
        print("\nFais une petite partie (choix 1) pour enregistrer ton premier score !")
        return
    list_scores = []
    with open (CHEMIN_FICHIER, "r") as fichier : 
            for ligne in fichier : 
             mots = ligne.split ()
             if len(mots) >= 3 : 
                    valeur = int(mots[2])
                    list_scores.append(int(mots[2]))
            if not list_scores: 
                return 

    x = range(1, len(list_scores) + 1)
    dernier_score = list_scores[-1]
    moyenne = sum(list_scores) / len(list_scores)
    plt.figure(figsize=(10, 6))
    couleur_points = []
    for s in list_scores:
        if s <= moyenne:
            couleur_points("green") 
        else: 
            couleur_points("red")
    
    plt.plot(x, list_scores, color="black", linestyle='--', linewidth=2, markersize=8, label="Mes_scores", zorder=1)
    plt.title (f"Ma liste {moyenne:.2f}")
    plt.scatter(x, list_scores, c=couleur_points, s=100, zorder=2)
    plt.axhline (y=moyenne, color='blue', linestyle=':', label= f"Moyenne({moyenne:.2f})")
    plt.xlabel("Numero de parties")
    plt.ylabel("Tentatives")
    plt.grid(True)
    plt.savefig("ma_progression.png")
    plt.legend()
    plt.show()

def afficher_score():
    print("\n ---Anciens Scores---")
    try:
        with open (CHEMIN_FICHIER, "r") as fichier :
            contenu = fichier.read()
            if not contenu: 
                print ("\nHistorique vide")
            else:
                print("\nHistorique des score :")
                print(contenu.strip())
    except FileNotFoundError:
        print("\nAucun score enregistré.")
    print("---------------------\n")

def jouer():
    print("\nQue la partie commence !")
    nombre_mystere = random.randint(1, 100)
    tentative = 0
    compteur_tentative = 0

    while tentative != nombre_mystere and compteur_tentative < 7 :
        try:
            tentative = int(input("\ndevine le nombre mystere"))
        except ValueError:
            print("\nErreur, tape un chiffre !")
            continue

        compteur_tentative += 1

        if tentative > nombre_mystere : 
            print("\nc'est moins")
        elif tentative < nombre_mystere : 
            print("\nc'est plus")

    if tentative == nombre_mystere: 
        print(f"\nVicoire ! Trouve en {compteur_tentative} essais.")
    else:
        print(f"\nPerdu, le nombre était {nombre_mystere}")

    with open(CHEMIN_FICHIER, "a") as fichier: 
        fichier.write(f"Score : {compteur_tentative} essais\n")

continuer = True 

while continuer : 
    print("===SUPER MENU DU JEU===") 
    print("1. Jouer une partie")
    print("2. Voir l'historique des scores")
    print("3. Quitter le programme") 
    print("4. Afficher le graphique")

    choix = input("\nVotre choix (1, 2, 3 ou 4) : ")

    if choix =="1": 
        jouer()
    elif choix =="2":
        afficher_score()
    elif choix =="3":
        print ("\nMerci d'avoir joue ! à bientot")
        continuer = False
    elif choix == "4":
        afficher_graphique()
    
    else:
        print("\nChoix invalide, essaie encore") 	
    


