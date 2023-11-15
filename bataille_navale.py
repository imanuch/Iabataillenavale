#I want to code in python a battleship game
from classnavale import *
taille = 10
joueur1 = grille(taille)
joueur2attaque = grilleattaque(taille)
bateaux = [2,3,3,4,5]
i = 0
while i < len(bateaux):
    try:
        x,y = input("Entrez les coordonnées du bateau de taille "+str(bateaux[i])+" : ").split()
        orientation = ""
        while orientation != "droite" and orientation != "gauche" and orientation != "haut" and orientation != "bas":         
            orientation = input("Entrez l'orientation du bateau : ")
        batn(x,y,orientation,bateaux[i],joueur1)
        i+=1
        break
    except ValueError:
        print("Vous n'avez pas entré de coordonnées")

while True:
    x,y = input("Entrez les coordonnées de l'attaque : ").split()
    joueur2attaque.attaque(joueur1,x,y)
joueur2attaque.attaque(joueur1,1,1)
joueur2attaque.affichermap()
print(" ")
joueur1.affichermap()