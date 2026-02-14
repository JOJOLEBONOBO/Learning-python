
import matplotlib.pyplot as plt
import os 
import json

def sauvegarder_stock(): 
    with open ("inventaire.json", "w") as fichier : 
        json.dump(stock, fichier, indent=4)
    print("Stock sauvegardé avec succés!")

def charger_stock(): 
    if os.path.exists("inventaire.json"): 
        with open ("inventaire.json", "r") as fichier: 
            return json.load(fichier)
    else: 
        return {"pommes" : 30, "bananes" : 15, "kiwi" : 10}

stock = charger_stock()

def afficher_stock():
    print("\n--- État du Stock ---")
    for fruit, quantite in stock.items():
        alerte = ""
        if quantite == 0 : 
            print("RUPTURE DE STOCK")
        elif quantite <= 5 : 
            print("!!! STOCK CRITIQUE !!!")
        print(f"{fruit.capitalize()} : {quantite}{alerte}")
    print("---------------------\n")

afficher_stock ()

def vendre(fruit):
    if fruit in stock: 
        print(f"Stock de {fruit} : {stock[fruit]}")
        qte = int(input(f"Quantité de {fruit} vendue : "))

        if qte <= stock[fruit]: 
            stock[fruit] -= qte 
        else : 
            print("Stock insuffisant")
    else : 
        print("Erreur : fruit inconnu")
    sauvegarder_stock()

def reception_livraison(): 
    fruit = input("Quelle fruit a été livré : ").lower()
    qte = int(input("Combien de ce fruit a été livré : "))
    if fruit in stock : 
        stock[fruit] += qte
        print(f"Réapprovisionnement réussi, nouveau stock de {fruit}: {stock[fruit]} ")
    else : 
        stock[fruit] = qte
        print(f"Nouveau fruit enregistré dans le catalogue : {fruit}")
    sauvegarder_stock()

def afficher_analyse_visuelle():
    noms_fruits = list(stock.keys())
    quantites = list(stock.values())
    
    liste_couleurs=[]
    for qte in quantites: 
        if qte < 5: 
             liste_couleurs.append('red')
        else: 
            liste_couleurs.append('green')

    plt.bar(noms_fruits, quantites, color = liste_couleurs)
    plt.axhline (y=5, color='blue', linestyle=':', label= f"Seuil critique")
    plt.title (f"Mon stock")
    plt.xlabel("Type Fruit")
    plt.ylabel("Nombres de fruits")
    plt.grid(True)
    plt.savefig("Mon stock.png")
    plt.legend()
    plt.show()

continuer = True 

while continuer : 
    print("===SUPER MENU DU STOCK===") 
    print("1. Vente de bananes")
    print("2. Vente de pommes")
    print("3. Vente de kiwis") 
    print("4. Afficher le stock")
    print("5. Réception stock")
    print("6. Graphique")
    print("7. Quitter le programme")

    choix = input("\nVotre choix (1 à 6) : ")

    if choix =="1": 
        vendre("bananes")
    elif choix =="2":
        vendre("pommes")
    elif choix =="3":
        vendre("kiwi")   
    elif choix == "4":
        afficher_stock()
    elif choix == "5" : 
        reception_livraison()
    elif choix == "6":
        print("Merci, aurevoir !")
        afficher_analyse_visuelle()
    elif choix == "7":
        continuer = False
        
    else:
        print("\nChoix invalide, essaie encore")
    
