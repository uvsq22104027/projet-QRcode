
"""
Tout ce qui est affichage existe seulement pour tester

Fait : 
- fonction rotation
- fct rotation appliquer aux coin

A faire :
- clean
- Verifier que tout marche

- charger un qr code 
- savoir le lire
- le faire tourné
test
"""

###code déjà fourni qui permet de charger et sauvegarder une image en noir et blanc dans le fichier projet.py###

import PIL as pil
from PIL import Image
from PIL import ImageTk 
import tkinter as tk
import random as rd
from tkinter import filedialog

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

create=True
nomImgCourante=""
nomImgDebut = ""

def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    global nomImgDebut
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante=filename.name
    nomImgDebut = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)
        create=False
        
    else: 
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin=canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)


def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)

###############  QUESTION 1  ############

# Création de la matrice des coins (mat_carre)
mat_carre = []
for i in range(8):
    liste = []
    for j in range(8):
        liste.append([0,0,0,255])
    mat_carre.append(liste)

# Remplissage de la matrice des coins
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


def affiche_matrice(matrice): #Pour nos tests
    "affiche une matrice dans le canvas"
    taille = taille_canvas/len(matrice)
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            couleur = "grey"
            if matrice[i][j]==[255,255,255,255]:
                couleur = "white"
            else :
                couleur = "black"
            canvas.create_rectangle((j)*taille, (i)*taille, (j+1)*taille, (i+1)*taille, fill = couleur)


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
        liste.append([255,255,255,255])
    mat_25.append(liste)

#print(comparaison_coin(mat_25,17,17))

def regarde_aux_coins(matrice):
    "regarde ou il y a des coin et donne des instruction pour la rotation du Qr code" #pas encore utilisé
    coin_haut_gauche = comparaison_coin(matrice,0,0)
    coin_haut_droite = comparaison_coin(matrice,0,len(matrice(25-len(mat_carre))))
    coin_bas_gauche = comparaison_coin(matrice,len(matrice(25-len(mat_carre)),0))
    coin_bas_droite = comparaison_coin(matrice,len(matrice(25-len(mat_carre)),len(matrice(25-len(mat_carre)))))
    if not coin_bas_droite:
        rotation = "rien"
        # ou 0 a droite
    elif not coin_bas_gauche :
        rotation = "gauche"
        # ou 3 a droite
    elif not coin_haut_droite:
        rotation = "droite"
        # ou 1 a droite
    else :
        rotation = "2"
        # ou 2 a droite
    return(rotation)

def ajoute_coin(matrice_a_modif, matrice_a_ajouté,x,y):
    #print("ok", x,y)
    "rajoute un coin a un endrois donner"
    for i in range(len(matrice_a_ajouté)):
        for j in range(len(matrice_a_ajouté)):
            matrice_a_modif[x+i][y+j] = matrice_a_ajouté[i][j]

def ajoute_coin_hasard(matrice_a_modif):
    "rajoute au hasard des coins sur 3 des 4 coins de mat_27"
    coin = rd.randint(0,4)
    coin_hg = True
    coin_hd = True
    coin_bg = True
    coin_bd = True
    if coin == 1 :
        coin_hg = False
    elif coin == 2 :
        coin_hd = False
    elif coin == 3 :
        coin_bg = False
    else :
        coin_bd = False
    if coin_hg == True:
        ajoute_coin(matrice_a_modif,mat_carre,0,0)
    if coin_hd == True:
        ajoute_coin(matrice_a_modif,rotation_multiple(mat_carre,1),0,len(matrice_a_modif)-len(mat_carre))
        # Faut faire tourné mat_carre aussi !
    if coin_bg == True:
        ajoute_coin(matrice_a_modif,rotation_multiple(mat_carre,3),len(matrice_a_modif)-len(mat_carre),0)
        # Faut faire tourné mat_carre aussi !
    if coin_bd == True:
        ajoute_coin(matrice_a_modif,rotation_multiple(mat_carre,2),len(matrice_a_modif)-len(mat_carre),len(matrice_a_modif)-len(mat_carre))
        # F

def rotation_multiple(matrice,nbr_rotation):
    mat=matrice
    while nbr_rotation != 0:
        mat = rotation(mat)
        nbr_rotation -= 1
    return mat

def rotation(matrice):
    "fait tournée une matrice sur la droite"
    matrice_tourne=[]

    for i in range(nbrCol(matrice)):
        matrice_tourne.append([])
        for j in range(nbrLig(matrice)):
            matrice_tourne[i].append([])

    # tourne 1 fois à droite
    for i in range(nbrLig(matrice)):
        for j in range(nbrCol(matrice)):
            matrice_tourne[i][j]=matrice[-j-1][i]

    return matrice_tourne

################# QUESTION 2 ##############
def question_2(mat_25):
    "je crois que ca créer juste les trucs, ca va pas verifier si y'a sur une image telechargee..."
    for i in range(25):
        for j in range(25):
            if i== 6 and 7<j<17:
                if j % 2 ==0:
                    mat_25[i][j]=[0,0,0,255]
                else:
                    mat_25[i][j]=[255,255,255,255]
            elif j==6 and 7<i<17:
                if i % 2 ==0:
                    mat_25[i][j]=[0,0,0,255]
                else:
                    mat_25[i][j]=[255,255,255,255]
    return mat_25

############### QUESTION 3 ###################################@
liste_essay=[0,0,0,0,1,1,0]

def code_Hamming(liste):
    c1=liste[0]+liste[1]+liste[3]
    c2=liste[0]+liste[2]+liste[3]
    c3=liste[1]+liste[2]+liste[3]
    if c1!=liste[4] and c2!=liste[5] and c3==liste[6]:
        liste[0]=(liste[0]+1)%2
        print(liste[0])
    if c1!=liste[4] and c3!=liste[6] and c2==liste[5]:
        liste[1]=(liste[1]+1)%2
        print(liste[1])
    if c2!=liste[5] and c3!=liste[6] and c1==liste[4]:
        liste[2]=(liste[2]+1)%2
        print(liste[0])
    if c2!=liste[5] and c3!=liste[6] and c1!=liste[4]:
        liste[3]=(liste[3]+1)%2
        print(liste[0])
    if c1!=liste[4] and (c2==liste[5] and c3==liste[6]):
        liste[4]=(liste[4]+1)%2
        print(liste[4])
    if c2!=liste[5] and (c1==liste[4] and c3==liste[6]):
        liste[5]=(liste[5]+1)%2
        print(liste[4])
    if c3!=liste[6] and (c2==liste[5] and c1==liste[4]):
        liste[6]=(liste[6]+1)%2
        print(liste[6])

    return liste

code_Hamming(liste_essay)
print(liste_essay)    

################
# Tkinter

racine = tk.Tk()

taille_canvas = 500

canvas = tk.Canvas(racine, width = taille_canvas, height = taille_canvas, bg = "white")
canvas.grid(row = 1, column = 1)

Bouton_charger=tk.Button(racine, text="charger", command=lambda: charger(racine))
Bouton_charger.grid(row=5,column=1)
mat_test=[[[255,255,255,255],[255,255,255,255],[255,255,255,255]],[[0,0,0,255],[0,0,0,255],[0,0,0,255]],[[255,255,255,255],[255,255,255,255],[255,255,255,255]]]

ajoute_coin_hasard(mat_25)
affiche_matrice(mat_25)
question_2(mat_25)



racine.mainloop()
