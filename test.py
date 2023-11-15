from classnavale import *
taille = 10
joueur1 = grille(taille)
joueur2attaque = grilleattaque(taille)
bateaux = [2,3,3,4,5]
ia = ia(bateaux,taille)


batn(1,1,"droite",2,joueur1)
batn(10,10,"gauche",3,joueur1)
batn(1,10,"bas",4,joueur1)
batn(10,1,"haut",4,joueur1)
joueur2attaque.attaque(joueur1,1,1)
joueur2attaque.attaque(joueur1,1,2)
joueur2attaque.attaque(joueur1,1,3)
joueur2attaque.attaque(joueur1,2,3)
ia.ponderergrille(joueur2attaque)
joueur2attaque.affichermap()
print()
ia.affichergrille()