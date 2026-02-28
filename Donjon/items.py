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
