import random
import requests
import json


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
        from items import potion_soin, anneau_magique, gourdin, poile_torse
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
        from items import ecaille_dragon, potion_force, epee_enflammee, crotte_de_dragon
        possibilites = [ecaille_dragon, potion_force, epee_enflammee, crotte_de_dragon]
        classe_choisie = random.choice(possibilites)
        nouveau_loot = classe_choisie()
        print(f"{self.nom} a été vaincu et laisse tomber un {nouveau_loot.nom} !")
        return nouveau_loot
    
class marchand ():
    def __init__(self, nom="Marchand", inventaire = None,):
        self.nom = nom
        self.inventaire = []
    def inventaire_du_marchand(self, nombre_objet = 3):
        from items import ecaille_dragon, potion_force, epee_enflammee, crotte_de_dragon, potion_soin, anneau_magique, gourdin, poile_torse
        possibilites = [ecaille_dragon, potion_force, epee_enflammee, crotte_de_dragon, potion_soin, anneau_magique, gourdin, poile_torse]
        for _ in range(nombre_objet) : 
            classe_choisie = random.choice(possibilites)
            nouvelle_objet = classe_choisie()
            self.inventaire.append(nouvelle_objet)
    def trier_inventaire(self) :
      import items
      n = len(self.inventaire)
      for i in range(n): 
        for j in range(0, n-i-1):  
            try: 
                if self.inventaire[j].price < self.inventaire[j+1] .price :
                    self.inventaire[j], self.inventaire[j+1] = self.inventaire[j+1], self.inventaire[j]
            except AttributeError :
                pass
    def actual_price(self): 
        url = "https://jsonplaceholder.typicode.com/posts/1"
        reponse = None
        try: 
            reponse = requests.get(url)
            if reponse is not None and reponse.status_code == 200 :                 
                donnes = reponse.json()
                new_price = donnes["id"]*100
                print (f"Bourse mise à jour ! Le nouveau prix de la bourse est de {new_price} or ")
                for objet in self.inventaire : 
                    objet.price = new_price
                    print(f"Le prix de {objet.nom} est maintenant de {objet.price} or. ")                
            else: 
                print ("le serveur dort, reviens plus tard.")
        except Exception as e: 
            print(f"Erreur réseau : {e} le pigeon est tombé dans l'eau. ")