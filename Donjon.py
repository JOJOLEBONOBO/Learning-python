import os
import json
import random
import matplotlib.pyplot as plt

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
    if os.path.exists("personnage.json"): 
        with open ("personnage.json", "r") as fichier: 
            return json.load(fichier)
    else: 
        return {"nom" : "Héros", "points_de_vie" : 100, "force" : 10, "speed" : 5}
    
class ennemi: 
    def __init__(self, nom="Inconnu", pv=100, force=0, speed=0) :
        self.nom = nom
        self.__pv = pv
        self.force = force
        self.speed = speed
        
    @property
    def pv(self):
        return self.__pv
    
    @pv.setter
    def pv(self, value):
        self.__pv = max(0, value)
        
class Gobelin(ennemi) :
    def __init__(self, nom="Gobelin", pv=50, force=5, speed=3) :
        super().__init__(nom, pv, force, speed)
    def parler(self) :
        print(f"{self.nom} ricane bêtement et prépare une attaque sournoise !")
    def capacite_speciale(self, defender) : 
        print(f"{self.nom} utilise sa capacité spéciale : Attaque sournoise !")
        defender.pv -= self.force
        self.pv += self.force*0.5
        print(f"{defender.nom} subit {self.force} dégâts de l'attaque sournoise et a {defender.pv} points de vie restants.") 
    def looter(self) :
        possibilites = [potion_soin, anneau_magique, gourdin, poile_torse]
        classe_choisie = random.choice(possibilites)      
        nouveau_loot = classe_choisie()
        print(f"{self.nom} a été vaincu et laisse tomber un {nouveau_loot.nom} !")
        return nouveau_loot
    
class Dragon(ennemi) :
    def __init__(self, nom="Dragon", pv=200, force=20, puissance_feu=30, speed=0.8) :
        super().__init__(nom, pv, force, speed)
        self.puissance_feu = puissance_feu
    def parler(self) :  
        print(f"{self.nom} crache des flammes et inflige {self.puissance_feu} dégâts !")
    def capacite_speciale(self, defender) :
        print(f"{self.nom} utilise sa capacité spéciale : Souffle de feu !")
        self.force = self.force * 0.9
        degats = self.puissance_feu
        defender.pv -= degats
        print(f"{defender.nom} subit {degats} dégâts de feu et a {defender.pv} points de vie restants.")
    def looter(self) :
        possibilites = ([ecaille_dragon, potion_force, epee_enflammee, crotte_de_dragon])
        classe_choisie = random.choice(possibilites)
        nouveau_loot = classe_choisie()
        print(f"{self.nom} a été vaincu et laisse tomber un {nouveau_loot.nom} !")
        return nouveau_loot

class objet :
    def __init__(self, nom="Inconnu", bonus_force=0, rarete="Inconnue", soin=0, speed=0, durabilite=3, price= 0) :
        self.nom = nom
        self.bonus_force = bonus_force
        self.rarete = rarete
        self.soin = soin
        self.speed = speed
        self.durabilite = durabilite
        self.price = price

        def __str__(self) :
            return self.nom
class potion_soin(objet) :
    def __init__(self, nom="Potion de soin", bonus_force=0, rarete="Commun", soin=10, price=5) :
        super().__init__(nom, bonus_force, rarete, soin=soin, price=price)
class potion_force(objet) :
    def __init__(self, nom="Potion de force", bonus_force=5, rarete="Peu commun", soin=0, price=5) :
        super().__init__(nom, bonus_force, rarete, soin=soin, price=price)
class anneau_magique(objet) :
    def __init__(self, nom="Anneau magique", bonus_force=0, rarete="Rare", soin=0, speed=2, price=10) :
        super().__init__(nom, bonus_force, rarete, soin=soin, speed=speed, price=price)
class epee_enflammee(objet) :
    def __init__(self, nom="Épée enflammée", bonus_force=10, rarete="Rare", soin=0, price=50) :
        super().__init__(nom, bonus_force, rarete, soin=soin, price=price)
class ecaille_dragon(objet) :
    def __init__(self, nom="Écaille de dragon", bonus_force=0, rarete="Peu commun", soin=30, price=20) :
        super().__init__(nom, bonus_force, rarete, soin=soin, price=price)
class gourdin(objet) :
    def __init__(self, nom="Gourdin", bonus_force=2, rarete="Commun", soin=0, price=10) :
        super().__init__(nom, bonus_force, rarete, soin=soin, price=price)
class poile_torse(objet) :
    def __init__(self, nom="Poile de torse", bonus_force=0, rarete="Commun", soin=0, price=5) :
        super().__init__(nom, bonus_force, rarete, soin=soin, price=price)
class crotte_de_dragon(objet) :
    def __init__(self, nom="Crotte de dragon", bonus_force=0, rarete="Commun", soin=0, price=1) :
        super().__init__(nom, bonus_force, rarete, soin=soin, price=price)

class personnage: 
    def __init__(self, nom="Inconnu", pv=100, force=0, speed=0, pv_max=100, inventaire=None, poid_max=5, Or=0) :
        self.nom = nom
        self.__pv = pv
        self.force = force
        self.speed = speed
        self.pv_max = pv_max
        self.inventaire = []
        self.poid_max = poid_max
        self.Or = Or
    def se_soigner(self, montant_soin) :
        self.pv += montant_soin
        print(f"{self.nom} se soigne de {montant_soin} points de vie et a maintenant {self.pv} points de vie.")
    
    def ramasser_objet(self, objet) :
        if len(self.inventaire) >= self.poid_max:
            print("Ton inventaire est plein ! Tu dois jeter un objet pour en ramasser un nouveau.")
            self.afficher_inventaire()
            choix = input("Quel objet veux-tu jeter ? (1, 2, 3, etc.) : ")
            if choix.isdigit() and 1 <= int(choix) <= len(self.inventaire):
                objet_jete = self.inventaire.pop(int(choix) - 1)
                print(f"Tu as jeté {objet_jete.nom} de ton inventaire.")
            else:
                print("Choix invalide, essaie encore.")
        else:
            self.inventaire.append(objet)
            print(f"{self.nom} ramasse un {objet.nom} et l'ajoute à son inventaire !")

    def utiliser_objet(self) :
        if not self.inventaire:
            print(f"{self.nom} n'a aucun objet à utiliser.")
            return
        self.afficher_inventaire()
        choix = input("Quel objet veux-tu utiliser ? (1, 2, 3, etc.), si tu ne veux pas en utiliser -> 0 : ")       
        if choix == "0":
            print("Tu ne veux pas utiliser d'objet.")
            return
        if choix.isdigit() and 1 <= int(choix) <= len(self.inventaire):
            objet = self.inventaire[int(choix) - 1]
            if objet.durabilite > 0:
                self.se_soigner(objet.soin)
                self.force += objet.bonus_force
                self.speed += objet.speed
                objet.durabilite -= 1
                print(f"{self.nom} utilise {objet.nom} et gagne {objet.soin} points de vie, {objet.bonus_force} points de force et {objet.speed} points de vitesse !")
                if objet.durabilite == 0:
                    self.inventaire.remove(objet)
                    self.force -= objet.bonus_force
                    self.speed -= objet.speed
                    print(f"{objet.nom} est cassé et ne peut pas être utilisé.")
        else:
            print("Choix invalide.")

    def reparer_objet(self) :
        if not self.inventaire:
            print(f"{self.nom} n'a aucun objet à réparer.")
            return
        self.afficher_inventaire()
        choix = input("Quel objet veux-tu réparer ? (1, 2, 3, etc.), si tu ne veux rien réparer -> 0 : ")
        if choix == "0":
            print("Tu ne veux pas réparer d'objet.")
            return
        if choix.isdigit() and 1 <= int(choix) <= len(self.inventaire) and self.Or >= 50:
            objet = self.inventaire[int(choix) - 1]
            if objet.durabilite < 1:
                objet.durabilite = 3
                print(f"{self.nom} a réparé {objet.nom} !")
                self.Or -= 50
            else:
                print(f"{objet.nom} n'a pas besoin d'être réparé.")

    def afficher_inventaire(self) :
        if self.inventaire:
            print(f"{self.nom} a les objets suivants dans son inventaire :")
            for i, objet in enumerate(self.inventaire, 1):
                print(f"- {i}. {objet.nom} (Bonus de force : {objet.bonus_force}, Soin : {objet.soin}, Bonus de vitesse : {objet.speed}, Durabilité : {objet.durabilite})")

        else:
            print(f"{self.nom} n'a aucun objet dans son inventaire.")   

    @property
    def pv(self):
        return self.__pv
    
    @pv.setter
    def pv(self, value):
        self.__pv = max(0, min(value, self.pv_max))

    def afficher_etat(self) : 
        print(f"Nom : {self.nom}")
        print(f"Points de vie : {self.pv}")
        print(f"Force : {self.force}")
        print(f"Vitesse : {self.speed}")

    def modifier_personnage(self) :
        self.nom = input("Quel est ton nom ? ") 
        self.pv = int(input("Combien de points de vie as-tu ? ")) 
        self.force = int(input("Quelle est ta force ? "))
        self.speed = int(input("Quelle est ta vitesse ? "))

    donjon = [Gobelin(), Gobelin(), Gobelin(), Gobelin(), Dragon()]          
    
    def entrer_donjon(self, donjon) :
        print("Tu entres dans le donjon et tu rencontres un ennemi !")
        for ennemi in donjon:  
            defender = ennemi
            tour = 0
            while defender.pv > 0 and self.pv > 0 :
                tour += 1
                if tour % 3 == 0:
                    self.se_soigner(self.pv_max * 0.2)
                    self.reparer_objet()
                if defender.speed > self.speed:
                    ennemi.parler()
                    print(f"{defender.nom} est plus rapide que {self.nom} et attaque en premier !")
                    self.pv -= defender.force
                    print(f"{defender.nom} attaque {self.nom} et lui inflige {defender.force} dégâts !")
                    print(f"{self.nom} a {self.pv} points de vie restants.")
                    print(f"C'est au tour de {self.nom} d'attaquer !")
                    self.utiliser_objet()
                    defender.pv -= self.force
                    print(f"{self.nom} attaque {defender.nom} et lui inflige {self.force} dégâts !")
                    print(f"{defender.nom} a {defender.pv} points de vie restants.")
                else:
                    print(f"{self.nom} attaque {defender.nom} !")
                    degats_min = int(self.force * 0.5)
                    degats_max = int(self.force * 1.5)
                    degats_aleatoires = random.randint(degats_min, degats_max)
                    self.utiliser_objet()
                    defender.pv -= degats_aleatoires
                    print(f"{self.nom} attaque {defender.nom} et lui inflige {degats_aleatoires} dégâts !")
                    print(f"{defender.nom} a {defender.pv} points de vie restants.")
                if defender.pv > 0 and defender.speed <= self.speed : 
                    print(f"{defender.nom} replique !")
                    if random.randint(1, 3) == 1:
                        defender.capacite_speciale(self)
                        print(f"{defender.nom} utilise sa capacité spéciale et inflige {defender.force} dégâts à {self.nom} !")
                    else:
                        print(f"La contre-attaque de {defender.nom} a échoué !")
                if random.randint (1, 2) == 1: 
                    print(f"{defender.nom} rate son attaque !")
                if defender.pv <= 0:
                    print(f"{defender.nom} est mort !")
                    self.Or += random.randint(10, 50)
                    objet = defender.looter()
                    self.ramasser_objet(objet)
                    print(f"Tu trouves {objet.nom} après avoir vaincu {defender.nom} !")
                if self.pv <= 0 : 
                    print(f"{self.nom} est mort !")
                    print("Game Over !")
                    break
                if ennemi == donjon[-1] and defender.pv <= 0:
                    print("Félicitations ! Tu as vaincu tous les ennemis du donjon !")
                    donjon.clear()
                    break

    def attaquer(self, defender=None) :
        choix = input("Quel ennemi veux-tu attaquer ? (1 ou 2) : ")
        if defender == self : 
            print("Pourquoi tu veux te suicider ? Appel le 3114!")
            return
        if choix == "1" : 
            defender = joueur_1
        elif choix == "2" : 
            defender = joueur_2
        else : 
            print("Choix invalide, attaque annulée")  
            return     
        while defender.points_de_vie > 0 and self.points_de_vie > 0 :
            print(f"{self.nom} attaque {defender.nom} !")
            degats_min = int(self.force * 0.5)
            degats_max = int(self.force * 1.5)
            degats_aleatoires = random.randint(degats_min, degats_max)
            defender.points_de_vie -= degats_aleatoires
            print(f"{self.nom} attaque {defender.nom} et lui inflige {degats_aleatoires} dégâts !")
            print(f"{defender.nom} a {defender.points_de_vie} points de vie restants.")
            if defender.points_de_vie > 0 : 
                print(f"{defender.nom} contre-attaque {self.nom} !")
                if random.randint (1, 5) == 1: 
                    print(f"{defender.nom} rate son attaque !")
                else :
                    self.points_de_vie -= defender.force
                print(f"{defender.nom} contre-attaque {self.nom} et lui inflige {defender.force} dégâts !")
                print(f"{self.nom} a {self.points_de_vie} points de vie restants.")
            if defender.points_de_vie <= 0:
                print(f"{defender.nom} est mort !")
            if self.points_de_vie <= 0:
                print(f"{self.nom} est mort !")
                break

joueur_1 = personnage("Hortense", 10000, 200)

joueur_2 = personnage("Gaia", 100000, 10)

joueur_3 = personnage("Henri", 1000, 20)

mon_hero = joueur_3

continuer = True 

while continuer : 
    print("===SUPER MENU RPG===") 
    print(f"1. Héro actuel {joueur_3.nom}")
    print("2. Modifier mon personnage")
    print("3. Attaquer un ennemi") 
    print("4. Entrer dans le donjon")
    print("5. Quitter le jeu")

    choix = input("\nVotre choix (1 à 5) : ")

    if choix =="1": 
        mon_hero.afficher_etat()
    elif choix =="2":
        mon_hero.modifier_personnage()
        sauvegarder_personnage()
    elif choix =="3":
        mon_hero.attaquer(joueur_1)
    elif choix == "4":
        mon_hero.entrer_donjon(mon_hero.donjon)
    elif choix == "5":
        print("Merci d'avoir joué ! À bientôt !")
        continuer = False
    else:
        print("\nChoix invalide, essaie encore")



