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


################
# Tkinter

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 800, height = 800, bg = "white")
canvas.grid(row = 1, column = 1)

affiche_matrice()

racine.mainloop()
