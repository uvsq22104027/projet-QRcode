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

###############  QUESTION 1  ############
def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)

#mat_carre=[[0,0,0,255]*8 for k in range (8)]
mat_carre = []
for i in range(8):
    for j in range(8):
        mat_carre.append([0,0,0,255])

print(mat_carre)
print("ok")

def chgmt_carre():
    global mat_carre
    mat_carre=[[0,0,0,255]*8 for k in range (8)]
    for i in range(8):
        for j in range(8):
            if i==2:
                print("ok")
                mat_carre[i][j]=[255,255,255,255]
            else :
                mat_carre[i][j]=[0,0,0,255]
                

chgmt_carre()

def carre():
    global mat_carre
    mat_carre=[[0,0,0,255]*8 for k in range (8)]
    for i in range(8):
        for j in range (8):
            if i==0 and j != 7:
                mat_carre[i][j]=[255,255,255,255]
            elif j==0 and i != 7:
                mat_carre[i][j]=[255,255,255,255]
            elif i==6 and j != 7:
                mat_carre[i][j]=[255,255,255,255]
            elif j==6 and i!=7:
                mat_carre[i][j]=[255,255,255,255]
            elif 1<i<5 and 1<j<5:
                mat_carre[i][j]=[255,255,255,255]
            else:
                mat_carre[i][j]=[0,0,0,255]
            print (mat_carre[i][j])



def affiche_matrice():
    couleur = "grey"
    for i in range(len(mat_carre)):
        for j in range(len(mat_carre[i])):
            couleur = "grey"
            if mat_carre[i][j]==[255,255,255,255]:
                couleur = "blue"
            else :
                couleur = "pink"
            canvas.create_rectangle((j-1)*50, (i-1)*50, (j)*50, (i)*50, fill = couleur)

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 800, height = 800, bg = "white")
canvas.grid(row = 1, column = 1)

affiche_matrice()

racine.mainloop()
