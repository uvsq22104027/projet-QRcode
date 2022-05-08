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

def modify(matrice):
    global imgModif
    global nomImgCourante
    saving(matrice,"modif.png")
    imgModif=ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    nomImgCourante="modif.png"
    return imgModif


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
        return 0
    elif not(coin_bas_gauche) :
        return 3
    elif not(coin_haut_droite) :
        return 1
    elif not(coin_haut_gauche) :
        return 2
    else :
        print("pblm")

def inverse_pour_modify(matrice):
    "transphorme les 1 en 0 et les 0 en 1"
    mat = []
    for i in range(len(matrice)):
        mat.append([])
        for j in range(len(matrice)):
            if matrice[i][j]==1:
                mat[i].append(0)
            else :
                mat[i].append(1)
    return mat

def rotation_multiple(matrice,nbr_rotation):
    "appel plusieurs fois rotation"
    mat=matrice
    while nbr_rotation != 0:
        mat = rotation(mat)
        nbr_rotation -= 1
    modify(inverse_pour_modify(mat))
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

############### QUESTION 4 ##################

res = [[],[]]

def extraction_1_bloc(x,y):
    "lit un morceau de la matrice charger de 2/14 et retourne les données brutes"
    global res
    for i in range(2):
        for j in range(7):
            res[i].append(mat_charger[x+i][y+j])
    return res

def lecture_1_bloc(x, y):
    extraction_1_bloc(x,y)
    print(extraction_1_bloc(x,y))

    mat = [[],[]]
    """
    1 : 1        ...       14   premiere lettre
    2 : 1        ...       14   2eme lettre

    2, 14
    1, 14
    2, 13
    1, 13
    """
    """for i in range(14,0):
        j = 2
        k = 1
        mat[j].append  """
        
    #Astrid
    """    mat = [[2,2,2,2,2,2,2],[2,2,2,2,2,2,2]]
    for j in range(7):   
        for k in range(1,3):
            if j==0:
                mat[0][j]=res[(k+1)%2][-1]
                mat[1][j]=res[k%2][-4]
                print(-1)
            else:
                mat[0][j]=res[(k+1)%2][-j-k]
                mat[1][j]=res[k%2][-j-k]
                print(-j-k)
                print("")"""
    
    return mat

    

############### QUESTION 5 ##################
def question5(liste1, liste2):
    ######## Hexadecimal #######
    s1=0
    s2=0
    s=0
    liste=liste1+liste2
    print(mat_charger[24][8])
    if mat_charger[24][8]==1:
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
    ############# ASCII ############
    else:
        for i in range(len(liste)):
            s+=(liste[-1-i]*(2**i))
        s=chr(s)
        print(s)

################ QUESTION 6 ################
def filtre_00(mat):
    mat_00=[[0]*14]*16
    for i in range(9,25):
        for j in range(11,25):
            mat[i][j]=mat[i][j]^mat_00[i-9][j-11]
            modify(inverse_pour_modify(mat))

mat_01=[[1]*14 for k in range(16)]
for i in range(nbrLig(mat_01)):
    for j in range(nbrCol(mat_01)):
        if i%2==0 and j%2==0:
            mat_01[i][j]=0
        if i%2==1 and j%2==1:
            mat_01[i][j]=0

def filtre_01(mat):
    for i in range(nbrLig(mat_01)):
        for j in range(nbrCol(mat_01)):
            mat[i+9][j+11]=mat[i+9][j+11]^mat_01[i][j]
            modify(inverse_pour_modify(mat))
        

mat_10=[[1]*14 for k in range(16)]
for i in range(nbrLig(mat_10)):
    for j in range(nbrCol(mat_10)):
        if i%2==0:
            mat_10[i][j]=0

def filtre_10(mat):
    for i in range(nbrLig(mat_10)):
            for j in range(nbrCol(mat_10)):
                mat[i][j]=mat[i][j]^mat_10[i][j]
                modify(inverse_pour_modify(mat))

mat_11=[[1]*14 for k in range(16)]
for i in range(nbrLig(mat_11)):
    for j in range(nbrCol(mat_11)):
        if j%2==0:
            mat_11[i][j]=0
        
def filtre_11(mat):
    for i in range(nbrLig(mat_11)):
            for j in range(nbrCol(mat_11)):
                mat[i+9][j+11]=mat[i+9][j+11]^mat_11[i][j]
                modify(inverse_pour_modify(mat))


def filtre(mat):
    mat= mat_charger
    if (1-mat_charger[22][8])==0:
        if (1-mat_charger[23][8])==0:
            filtre_00(mat_charger)
        else:
            filtre_01(mat_charger)
    else:
        if (1-mat_charger[23][8])==0:
            print(1-mat_charger[23][8])
            filtre_10(mat_charger)
        else:
            filtre_11(mat_charger)

#question5(code_Hamming(lecture_1_bloc(0,0)[0]), code_Hamming(lecture_1_bloc(0,0)[1])))

################
# Tkinter

racine = tk.Tk()


Bouton_charger=tk.Button(racine, text="charger", command=lambda: charger(racine))
Bouton_charger.grid(row=5,column=1)

Bouton_comparer=tk.Button(racine, text="comparer", command=lambda: question5(code_Hamming(lecture_1_bloc(0,0)[0]), code_Hamming(lecture_1_bloc(0,0)[1])))
Bouton_comparer.grid(row=5,column=2)

Bouton_filtre=tk.Button(racine, text="filtre", command=lambda: filtre(mat_charger))
Bouton_filtre.grid(row=6, column=1)

Bouton_rotation=tk.Button(racine, text="rotation", command=lambda: rotation_multiple(mat_charger,regarde_coin_25(mat_charger)))
#Bouton_rotation=tk.Button(racine, text="rotation", command=lambda: inverse_pour_modify(mat_charger))
Bouton_rotation.grid(row=5, column=3)



racine.mainloop()
