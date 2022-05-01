"""
comparaison mat carre et pointiller : 1er if, remetre si matrice a comparer plus petite que mat carre/ligne
finir comparaison ligne
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

mat_charger = []

def loading(filename):#charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente 
					  #l'image en noir et blanc
    global mat_charger
    toLoad=pil.Image.open(filename)
    mat=[[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]= 0 if toLoad.getpixel((j,i)) == 0 else 1
    mat_charger = mat
    for i in range(len(mat_charger)):
        for j in range(len(mat_charger)):
            if mat_charger[i][j]==0:
                mat_charger[i][j]=1
            elif mat_charger[i][j]==1:
                mat_charger[i][j]=0
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
    loading(filename)


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
        liste.append(1)
    mat_carre.append(liste)
# Remplissage de la matrice des coins
for i in range(8):
    for j in range(8):
        if (i==1 or i == 5) and j<6 and j>0:
            mat_carre[i][j]=0
        elif (j==1 or j == 5) and i<6 and i>0:
            mat_carre[i][j]=0
        elif j == 7 or i == 7:
            mat_carre[i][j]=0
        else :
            mat_carre[i][j]=1

## Question 2
# Création et remplissage de la matrice pointiller entre les coins (mat_carre)
mat_ligne = [] 
for i in range(9):
    if i % 2 == 0:
        mat_ligne.append(1)
    elif i % 2 == 1:
        mat_ligne.append(0)

a=[]
# Comparaison d'une matrice de 8x8 avec la matrice coin
def comparaison_coin(matrice_a_comparer, x, y):
    "Compare une matrice à partire des position x et y avec la matrice coin, retourne True si pareil, faux si différent"
    global a
    # doit regarder pr chaque ij de mat_a_comp si == a mat_coin
    #if x>=len(matrice_a_comparer)-7 or y>=len(matrice_a_comparer)-7:
    if 1!=1:
        # si pas la place (trop en bas ou trop a doite)
        return False
    else :
        cpt = 0
        for i in range(len(mat_carre)):
            for j in range(len(mat_carre)):
                mat = 2
                if matrice_a_comparer[x+i][y+j] == 0:
                    mat = 0
                elif matrice_a_comparer[x+i][y+j] == 1:
                    mat = 1
                if mat==mat_carre[i][j]:
                    cpt += 1
                else :
                    cpt += 0
        if cpt == len(mat_carre)*len(mat_carre[0]):
            a.append((x,y))
            return True
        else :
            return False

b = []
# // matrice pointiller
def comparaison_ligne_horizontal(matrice_a_comparer, x, y):
    "Compare une matrice à partire des position x et y avec la matrice pointiller, retourne True si pareil, faux si différent"
    global b
    if 1!=1:
        # si pas la place (trop en bas ou trop a doite)
        return False
    else :
        cpt = 0
        for i in range(len(mat_ligne)):
            mat = 2
            if matrice_a_comparer[x+i][y] == 0:
                mat = 0
            elif matrice_a_comparer[x+i][y] == 1:
                mat = 1
            if mat==mat_carre[i][j]:
                cpt += 1
            else :
                cpt += 0
        if cpt == len(mat_ligne):
            b.append((x,y))
            return True
        else :
            return False


b2 = []
def comparaison_ligne_vertical(matrice_a_comparer, x, y):
    "Compare une matrice à partire des position x et y avec la matrice pointiller, retourne True si pareil, faux si différent"
    global b2
    if 1!=1:
        # si pas la place (trop en bas ou trop a doite)
        return False
    else :
        cpt = 0
        for i in range(len(mat_ligne)):
            mat = 2
            if matrice_a_comparer[x][y+i] == 0:
                mat = 0
            elif matrice_a_comparer[x][y+i] == 1:
                mat = 1
            if mat==mat_carre[i][j]:
                cpt += 1
            else :
                cpt += 0
        if cpt == len(mat_ligne):
            b2.append((x,y))
            return True
        else :
            return False


def recup_coin(matrice,x,y):
    "fonction secondaire pour regarde_coin_25, recupere un morceau d'une matrice de la taille d'un coin"
    res = [[] for i in range(8)]
    for i in range(0,len(mat_carre)):
        for j in range(0,len(mat_carre[0])):
            res[i].append(matrice[x+i][y+j])
    return res

def regarde_coin_25(matrice):
    "Sur la matrice de 25/25, regarde où il y a des coins et retourne le nombre de rotation à faire"
    mat_hd = rotation_multiple(recup_coin(matrice,0,25-8),3)
    mat_bg = rotation(recup_coin(matrice,25-8,0))
    mat_bd = rotation_multiple(recup_coin(matrice,25-8,25-8),2)
    coin_haut_gauche = comparaison_coin(matrice,0,0)
    coin_haut_droite = comparaison_coin(mat_hd,0,0)
    coin_bas_gauche = comparaison_coin(mat_bg,0,0)
    coin_bas_droite = comparaison_coin(mat_bd,0,0)
    if not(coin_bas_droite) :
        print("0")
        return 0
    elif not(coin_bas_gauche) :
        print("3")
        return 3
    elif not(coin_haut_droite) :
        print("1")
        return 1
    elif not(coin_haut_gauche) :
        print("2")
        return 2
    else :
        print("pblm")

def rotation_multiple(matrice,nbr_rotation):
    "appel plusieurs fois rotation"
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

############### QUESTION 3 ###################################@
liste_essay1=[1,1,1,1,1,1,1]
liste_essay2=[1,0,1,1,1,0,1]

def code_Hamming(liste):
    l=[]
    c1=liste[0]+liste[1]+liste[3]
    c2=liste[0]+liste[2]+liste[3]
    c3=liste[1]+liste[2]+liste[3]
    if c1!=liste[4] and c2!=liste[5] and c3==liste[6]:
        liste[0]=(liste[0]+1)%2
    if c1!=liste[4] and c3!=liste[6] and c2==liste[5]:
        liste[1]=(liste[1]+1)%2
    if c2!=liste[5] and c3!=liste[6] and c1==liste[4]:
        liste[2]=(liste[2]+1)%2
    if c2!=liste[5] and c3!=liste[6] and c1!=liste[4]:
        liste[3]=(liste[3]+1)%2
    if c1!=liste[4] and (c2==liste[5] and c3==liste[6]):
        liste[4]=(liste[4]+1)%2
    if c2!=liste[5] and (c1==liste[4] and c3==liste[6]):
        liste[5]=(liste[5]+1)%2
    if c3!=liste[6] and (c2==liste[5] and c1==liste[4]):
        liste[6]=(liste[6]+1)%2

    l.append(liste[0])
    l.append(liste[1])
    l.append(liste[2])
    l.append(liste[3])

    return l

code_Hamming(liste_essay1)
print(liste_essay1)
code_Hamming(liste_essay2)
print(liste_essay2)

############### QUESTION 4 ##################

def lecture_1_bloc(x, y):
    "lit un morceau de la matrice charger de 2/14 et retourne les données brutes"
    res = [[],[]]
    for i in range(2):
        for j in range(7):
            res[i].append(mat_charger[x+i][y+j])
    print(res)
    return res

############### QUESTION 5 ##################
def question5(liste1, liste2):
    ######## Hexadecimal #######
    s1=0
    s2=0
    for i in range(len(liste1)):
        s1+=(liste1[-1-i]*(2**i))
    if s1==10:
        s1="A"
    if s1==11:
        s1="B"
    if s1==12:
        s1="C"
    if s1==13:
        s1="D"
    if s1==14:
        s1="E"
    if s1==15:
        s1="F"
    print(s1)
    for i in range(len(liste2)):
        s2+=(liste2[-1-i]*(2**i))
    if s2==10:
        s2="A"
    if s2==11:
        s2="B"
    if s2==12:
        s2="C"
    if s2==13:
        s2="D"
    if s2==14:
        s2="E"
    if s2==15:
        s2="F"
    print(s2)
    ############# ACSII ############

question5(code_Hamming(liste_essay1), code_Hamming(liste_essay2))   

################
# Tkinter

racine = tk.Tk()


Bouton_charger=tk.Button(racine, text="charger", command=lambda: charger(racine))
Bouton_charger.grid(row=5,column=1)

Bouton_comparer=tk.Button(racine, text="comparer", command=lambda: lecture_1_bloc(0, 0))
Bouton_comparer.grid(row=5,column=2)
#regarde_coin_25(mat_charger)



racine.mainloop()
