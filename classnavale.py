class case():
    def __init__(self):
        self.etat = 0  #etat = 0 : case vide, etat = 1 : case occupée, etat = 2 : case touchée, etat = 3 : case coulée
        self.bateau = None
    def __str__(self) -> str:
        return str(self.etat)
    def setetat(self,bateau):
        if self.etat == 0:
            self.etat = 1
            self.bateau = bateau
            
    def setbat(self,bateau):
        self.bateau = bateau
        
    def attaque(self) -> int:
        if self.etat == 0:
            return 5
        if self.etat == 2:
            print("Erreur, la case est déjà touchée")
        if self.etat == 1:
            self.etat = self.etat+1
            self.bateau.bateautouche()
            if self.bateau.gettailleactu() == 0:
                print("coulé")
                return 1
                
                
        if self.etat == 3:
            print("Erreur, la case est déjà coulée")
        return 0
    
    def coule(self):
        print("la aussi")
        self.etat = 3
        
    def getetat(self):
        return self.etat

class grille():
    def __init__(self, taille : int):
        self.map = []
        self.taille = taille
        self.map = [[case() for _ in range(self.taille)] for _ in range(self.taille)]

                
    def placercarte(self,x : int,y : int,bateau):
        self.map[x][y].setetat(bateau)
        
    def grilleattaque(self,x,y):
        coule = self.map[x][y].attaque()
        if coule == 1:
            self.bateaucoule(self.map[x][y].bateau)
            
    def getcase(self,x,y):
        return self.map[x][y].getetat()
    
    def affichermap(self):
        alph = "abcdefghijklmnopqrstuvwxyz"
        k = 0
        for i in range(self.taille):
            print(i+1,end = " ")
        print()
        for ligne in self.map:
            for case in ligne:
                print(case, end=' ')
            print(alph[k])
            k+=1
    
    def bateaucoule(self, bateau):
        x = bateau.x
        y = bateau.y
        orientation = bateau.orientation
        if orientation == "droite":
            for i in range(bateau.taille):
                self.map[x][y+i].coule()
        elif orientation == "gauche":
            for i in range(bateau.taille):
                self.grille[x][y-i].coule()
        elif orientation == "haut":
            for i in range(bateau.taille):
                self.grille[x-i][y].coule()
        elif orientation == "bas":
            for i in range(bateau.taille):
                self.grille[x+i][y].coule()
              
class grilleattaque():
    def __init__(self, taille : int):
        self.map = []
        self.taille = taille
        self.map = [[0 for _ in range(self.taille)] for _ in range(self.taille)]
    def attaque(self,grille : grille,x : int,y : int):
        x = x-1
        y = y-1
        grille.grilleattaque(x,y)
        self.map[x][y] = grille.map[x][y].getetat()
    
    def affichermap(self):
        alph = "abcdefghijklmnopqrstuvwxyz"
        k = 0
        for i in range(self.taille):
            print(i+1,end = " ")
        print()
        for ligne in self.map:
            for case in ligne:
                print(case, end=' ')
            print(alph[k])
            k+=1

class batn():
    def __init__(self,x : int,y : int,orientation : str ,taille : int ,grille : grille):
        self.x = x-1
        self.y = y-1
        self.orientation = orientation
        self.taille = taille
        self.tailleactu = taille
        erreur = 0
        
        if self.orientation =="droite" and self.y+self.taille<grille.taille:
            for i in range(self.taille):
                if grille.map[self.x][self.y+i].getetat() == 1:
                    print("Erreur, la case est déjà occupée")
                    erreur = 1
                    break
                
            if erreur == 0 :
                for i in range(self.taille):
                    grille.placercarte(self.x,self.y+i,self)
                print()
                    
        elif self.orientation == "gauche" and self.y>self.taille:
            
            for i in range(self.taille-1):
                if grille.map[self.x][self.y-i].getetat() == 1:
                    print("Erreur, la case est déjà occupée")
                    erreur = 1
                    break
                
            if erreur ==0:
                for i in range(self.taille-1):
                    grille.placercarte(self.x,self.y-i,self)
                    
                    
        elif self.orientation == "haut" and self.x>self.taille:                
            for i in range(self.taille-1):
                if grille.map[self.x-i][self.y].getetat() == 1:
                    print("Erreur, la case est déjà occupée")
                    erreur = 1
                    break
                
            if erreur == 0:
                for i in range(self.taille-1):
                    grille.placercarte(self.x-i,self.y,self)
                    
        elif self.orientation == "bas" and self.x + self.taille<grille.taille:
                
            for i in range(self.taille-1):
                if grille.map[self.x+i][self.y].getetat() == 1:
                    print("Erreur, la case est déjà occupée")
                    erreur = 1
                    break
                
            if erreur == 0:
                for i in range(self.taille):
                    grille.placercarte(self.x+i,self.y,self)
                    
    def bateautouche(self):
        self.tailleactu -=1
        if self.taille == 0:
            print("Le bateau est coulé")
            
    def gettailleactu(self):
        return self.tailleactu
        
                    
            
class ia():
    def __init__(self,bateau : batn,taille : int):
        self.bateau = bateau
        self.taille = taille
        self.grilleponderee = [[0 for _ in range(self.taille)] for _ in range(self.taille)]

        pass
    def ponderergrille(self,grilleattaque : grilleattaque):
        for bat in range(len(self.bateau)):
            for i in range(self.taille-self.bateau[bat]):
                for j in range(self.taille):
                    if grilleattaque.map[i][j] == 0 and grilleattaque.map[i+1][j] == 0:
                        self.grilleponderee[i][j] += 1

    def affichergrille(self):
        alph = "abcdefghijklmnopqrstuvwxyz"
        k = 0
        for i in range(self.taille):
            print(i+1,end = " ")
        print()
        for ligne in self.grilleponderee:
            for case in ligne:
                print(case, end=' ')
            print(alph[k])
            k+=1
    
    
    