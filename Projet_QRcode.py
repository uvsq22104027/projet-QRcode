###code déjà fourni qui permet de charger et sauvegarder une image en noir et blanc dans le fichier projet.py###

import PIL as pil
from PIL import Image
from PIL import ImageTk 
import tkinter as tk


def saving(matPix, filename):#sauvegarde l'image contenue dans matpix dans le fichier filename
							 #utiliser une extension png pour que la fonction fonctionne sans perte d'information
    toSave=pil.Image.new(mode = "1", size = (nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j,i),matPix[i][j])
    toSave.save(filename)

def loading(filename):#charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente 
					  #l'image en noir et blanc
    toLoad=pil.Image.open(filename)
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    return mat

def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)

###############  QUESTION 1  ############

# Création de la matrice des coins
mat_carre = []
for i in range(8):
    liste = []
    for j in range(8):
        liste.append([0,0,0,255])
    mat_carre.append(liste)

# Remplissage de la matrice des coins
def chgmt_carre():
    "Place les lignes blanche dans la matrice pour les coins"
    global mat_carre
    for i in range(8):
        for j in range(8):
            if (i==1 or i == 5) and j<6 and j>0:
                mat_carre[i][j]=[255,255,255,255]
            elif (j==1 or j == 5) and i<6 and i>0:
                mat_carre[i][j]=[255,255,255,255]
            elif j == 7 or i == 7:
                mat_carre[i][j]=[255,255,255,255]
            else :
                mat_carre[i][j]=[0,0,0,255]
                
chgmt_carre()

def affiche_matrice():
    "affiche la matrice coin dans le canvas (pour vérifier la question 1"
    couleur = "grey"
    for i in range(len(mat_carre)):
        for j in range(len(mat_carre[i])):
            couleur = "grey"
            if mat_carre[i][j]==[255,255,255,255]:
                couleur = "white"
            else :
                couleur = "black"
            canvas.create_rectangle((j)*50, (i)*50, (j+1)*50, (i+1)*50, fill = couleur)

"""
Je cherche d'abord a comparer avec la matrice des coins : OK
ensuite je lui ferai regarder là ou il doit y avoir des coins, pour noté où il y en a : Commencé (compart a un endrois donné)
enfain je lui ferais tourner en fonction
"""

# Comparaison d'une matrice de 8x8 avec la matrice coin
def comparaison_coin(matrice_a_comparer, x, y):
    "Compare une matrice à partire des position x et y avec la matrice coin, retourne True si pareil, faux si différent"
    # doit regarder pr chaque ij de mat_a_comp si == a mat_coin
    if x>=len(matrice_a_comparer)-7 or y>=len(matrice_a_comparer)-7:
        # si pas la place (trop en bas ou trop a doite)
        return False
    else :
        for i in range(len(matrice_a_comparer)):
            for j in range(len(matrice_a_comparer)):
                if matrice_a_comparer[x+i][y+j]!=mat_carre[i][j]:
                    return False
        return True

# 2 matrices de 8x8 a comparer : x vrai, y faux
matrice_x = [[[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255]]]
matrice_y = [[[255, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [255, 255, 255, 255]], [[255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255]]]
#print(comparaison_coin(matrice_x,0,0))

#creation d'une matrice de taille 25x25
mat_25 = []
for i in range(25):
    liste = []
    for j in range(25):
        liste.append([0,0,0,255])
    mat_25.append(liste)

print(comparaison_coin(mat_25,17,17))


################
# Tkinter

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "white")
canvas.grid(row = 1, column = 1)

#affiche_matrice()

#racine.mainloop()
