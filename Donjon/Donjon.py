import os
import json
import random
import sys
import matplotlib.pyplot as plt
from entities import Gobelin, Dragon, marchand
from hero import personnage


def sauvegarder_personnage(hero): 
    donnes_personnage = {
        "nom" : hero.nom
        ,"points_de_vie" : hero.pv
        ,"force" : hero.force
        ,"vitesse" : hero.speed
        ,"pv_max" : hero.pv_max
    }
    with open ("personnage.json", "w") as fichier : 
        json.dump(donnes_personnage, fichier, indent=4)
    print("Personnage sauvegardé avec succés!")

def charger_personnage(): 
    try : 
        with open ("personnage.json", "r") as fichier: 
            donnes_personnage = json.load(fichier)
            return personnage(
                nom=donnes_personnage["nom"],
                pv=donnes_personnage["points_de_vie"],
                force=donnes_personnage["force"],
                speed=donnes_personnage["vitesse"],
                pv_max=donnes_personnage["pv_max"]
            )
    except FileNotFoundError:
        print("Aucun personnage sauvegardé trouvé.")
    else: 
        return {"nom" : "Héros", "points_de_vie" : 100, "force" : 10, "speed" : 5}

joueur_1 = personnage("Hortense", 10000, 200)

joueur_2 = personnage("Gaia", 100000, 10)

joueur_3 = personnage("Henri", 1000, 20)

mon_hero = joueur_3

Le_marchand = marchand("Marchand")
Le_marchand.inventaire_du_marchand(3)

continuer = True 



while continuer : 
    print("===SUPER MENU RPG===") 
    print(f"1. Héro actuel {joueur_3.nom}")
    print("2. Modifier mon personnage")
    print("3. Attaquer un ennemi") 
    print("4. Entrer dans le donjon")
    print("5. Entrer dans la taverne")
    print("6. Quitter le jeu")

    choix = input("\nVotre choix (1 à 6) : ")

    if choix =="1": 
        mon_hero.afficher_etat()
    elif choix =="2":
        mon_hero.modifier_personnage()
        sauvegarder_personnage(mon_hero)
    elif choix =="3":
        mon_hero.attaquer(joueur_1)
    elif choix == "4":
        mon_hero.entrer_donjon(mon_hero.donjon)
    elif choix == "5": 
            mon_hero.entrer_taverne(Le_marchand)
    elif choix == "6":
        print("Merci d'avoir joué ! À bientôt !")
        continuer = False
    else:
        print("\nChoix invalide, essaie encore")


