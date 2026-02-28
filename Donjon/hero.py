import random
import items


class personnage: 
    def __init__(self, nom="Inconnu", pv=100, force=0, speed=0, pv_max=100, inventaire=None, poid_max=5, Or=0) :
        self.nom = nom
        self.__pv = pv
        self.force = force
        self.speed = speed
        self.pv_max = pv_max
        self.inventaire = []
        self.__poid_max = poid_max
        self.Or = Or

    @property
    def pv(self):
        return self.__pv
    
    @pv.setter
    def pv(self, value):
        self.__pv = max(0, min(value, self.pv_max))
    
    @property
    def poid_max(self):
        return self.__poid_max
    
    @poid_max.setter
    def poid(self, value):
        self.__poid_max = max(0, min (value, self.__poid_max))


    from entities import Gobelin, Dragon
    donjon = [Gobelin(), Gobelin(), Gobelin(), Gobelin(), Dragon()] 
    def entrer_donjon(self, donjon) :
        print("Tu entres dans le donjon et tu rencontres un ennemi !")
        for ennemi in donjon:  
            defender = ennemi
            tour = 0
            while defender.pv > 0 and self.pv > 0 :
                tour += 1
                if tour % 5 == 0:
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
        
    def entrer_taverne(self, marchand):
        print(f"--- {marchand.nom} vous salue ---")
        marchand.actual_price()
        try:
            choix = int(input("Souhaitez-vous Vendre(1), Acheter(2), Sortir(0) ? "))
        except ValueError: 
            print("Veuillez entrer un chiffre")
            return
        if choix == 1: 
            self.afficher_inventaire()
            if not self.inventaire: 
                print("Ton sac est vide, Henri ! ")
                return 
            reponse_vendre = input("Quel objet souhaitez-vous vendre ? ")
            if reponse_vendre.isdigit() and 1 <= int(reponse_vendre) <= len(self.inventaire):
                objet = self.inventaire.pop(int(reponse_vendre) - 1)
                self.Or += objet.price
                print(f"Tu vends {objet.nom} pour {objet.price} or !")
            else : 
                print("Choix invalide ! ")

        elif choix == 2: 
            if not marchand.inventaire: 
                print("Le marchand n'a rien en stock, reviens plus tard ! ")
                return
            for i, obj in enumerate(marchand.inventaire, 1):
                print(f"{i}. {obj.nom} ({obj.price} or)")
            
            reponse_achat = input("Lequel veux-tu acheter (0 pour partir) ? ")
            if reponse_achat.isdigit() and 1 <= int(reponse_achat) <= len(marchand.inventaire):
                index = int(reponse_achat) - 1
                objet_boutique = marchand.inventaire[index]
            
                if self.Or >= objet_boutique.price:
                    self.Or -= objet_boutique.price
                    marchand.inventaire.pop(index)
                    self.ramasser_objet(objet_boutique)
                    print(f"Tu as acheté {objet_boutique.nom} pour {objet_boutique.price} or.")
                else:
                    ("Désolé Henri, pas assez d'or !")
            else : 
                print("Choix invalide")
                return

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

    def trier_inventaire(self) :
      import items
      n = len(self.inventaire)
      self.chercher_par_prix()
      for i in range(n): 
        for j in range(0, n-i-1):  
            try: 
                if self.inventaire[j].price < self.inventaire[j+1] .price :
                    self.inventaire[j], self.inventaire[j+1] = self.inventaire[j+1], self.inventaire[j]
            except AttributeError :
                pass

    def chercher_par_prix(self, price_recherche):  
        debut = 0
        fin = len(self.inventaire)-1
        while debut <= fin : 
            milieu = (debut + fin)//2
            objet_milieu = self.inventaire[milieu]
            if objet_milieu.price == price_recherche : 
                return objet_milieu
            elif objet_milieu.price < price_recherche : 
                fin = milieu - 1
            else : 
                debut = milieu + 1
        return None
            
    def afficher_etat(self) : 
        print(f"Nom : {self.nom}")
        print(f"Points de vie : {self.pv}")
        print(f"Force : {self.force}")
        print(f"Vitesse : {self.speed}")

    def modifier_personnage(self) :
        try :
            while True : 
                self.nom = input("Quel est ton nom ? ")
                if self.nom.strip():
                    break
                else:
                    print("Nom invalide. Veuillez entrer un nom valide.")
        except ValueError:
            print("Nom invalide. Veuillez entrer un nom valide.")
            self.nom = "Héros"
        try :
            while True:
                pv_input = input("Combien de points de vie as-tu ? ")
                if pv_input.isdigit():
                    self.pv = int(pv_input)
                    break
                else:
                    print("Valeur invalide pour les points de vie. Veuillez entrer un nombre entier.")
        except ValueError:
            print("Valeur invalide pour les points de vie. Veuillez entrer un nombre entier.")
            self.pv = 1000
        try :
            while True:
                self.force = input("Quelle est ta force ? ")
                if self.force.isdigit():
                    self.force = int(self.force)
                    break
                else:
                    print("Valeur invalide pour la force. Veuillez entrer un nombre entier.")
            self.force = int(input("Quelle est ta force ? "))
        except ValueError:
            print("Valeur invalide pour la force. Veuillez entrer un nombre entier.")
            self.force = 20
        try :
            while True : 
                self.speed = input("Quelle est ta vitesse ? ")
                if self.speed.isdigit():
                    self.speed = int(self.speed)
                    break
                else:
                    print("Valeur invalide pour la vitesse. Veuillez entrer un nombre entier.")
            self.speed = int(input("Quelle est ta vitesse ? "))
        except ValueError:
            print("Valeur invalide pour la vitesse. Veuillez entrer un nombre entier.")
            self.speed = 5

         
   



joueur_1 = personnage("Hortense", 10000, 200)

joueur_2 = personnage("Gaia", 100000, 10)

joueur_3 = personnage("Henri", 1000, 20)

mon_hero = joueur_3

continuer = True 