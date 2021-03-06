import PIL as pil
from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog


def saving(matPix, filename):
    """sauvegarde l'image contenue dans matpix dans le fichier filename utiliser une extension png pour que la fonction fonctionne sans perte d'information"""
    toSave = pil.Image.new(mode="1", size=(nbrCol(matPix), nbrLig(matPix)))
    for i in range(nbrLig(matPix)):
        for j in range(nbrCol(matPix)):
            toSave.putpixel((j, i), matPix[i][j])
    toSave.save(filename)


mat_charger = []


def loading(filename):
    """charge le fichier image filename et renvoie une matrice de 0 et de 1 qui représente l'image en noir et blanc"""
    global mat_charger
    toLoad = pil.Image.open(filename)
    mat = [[0]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j] = 0 if toLoad.getpixel((j, i)) == 0 else 1
    mat_charger = mat
    for i in range(len(mat_charger)):
        for j in range(len(mat_charger)):
            if mat_charger[i][j] == 0:
                mat_charger[i][j] = 1
            elif mat_charger[i][j] == 1:
                mat_charger[i][j] = 0
    return mat


create = True
nomImgCourante = ""
nomImgDebut = ""


def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    global nomImgDebut
    filename = filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante = filename.name
    nomImgDebut = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:
        canvas = tk.Canvas(widg, width=img.size[0], height=img.size[1])
        dessin = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.grid(row=0, column=1, rowspan=4, columnspan=2)
        create = False

    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width=img.size[0], height=img.size[1])
        dessin = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.grid(row=0, column=1, rowspan=4, columnspan=2)
    loading(filename)


def modify(matrice):
    global imgModif
    global nomImgCourante
    saving(matrice, "modif.png")
    imgModif = ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    nomImgCourante = "modif.png"
    return imgModif


def nbrCol(matrice):
    if type(matrice[0]) == int:
        return(1)
    else:
        return(len(matrice[0]))


def nbrLig(matrice):
    return len(matrice)


# Var global

message = ""

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
        if (i == 1 or i == 5) and j < 6 and j > 0:
            mat_carre[i][j] = 0
        elif (j == 1 or j == 5) and i < 6 and i > 0:
            mat_carre[i][j] = 0
        elif j == 7 or i == 7:
            mat_carre[i][j] = 0
        else:
            mat_carre[i][j] = 1

# Comparaison avec la matrice ligne


def comparaison_coin(matrice_a_comparer, x, y):
    "Compare une matrice à partire des position x et y avec la matrice coin, retourne True si pareil, faux si différent"
    cpt = 0
    for i in range(len(mat_carre)):
        for j in range(len(mat_carre)):
            if matrice_a_comparer[x+i][y+j] == mat_carre[i][j]:
                cpt += 1
            else:
                cpt += 0
    if cpt == len(mat_carre)*len(mat_carre[0]):
        return True
    else:
        return False


def recup_coin(matrice, x, y):
    "fonction secondaire pour regarde_coin_25, recupere un morceau d'une matrice de la taille d'un coin"
    res = [[] for i in range(8)]
    for i in range(0, len(mat_carre)):
        for j in range(0, len(mat_carre[0])):
            res[i].append(matrice[x+i][y+j])
    return res


## Question 2
# Création et remplissage de la matrice pointiller entre les coins (mat_carre)

mat_ligne = []
for i in range(9):
    if i % 2 == 0:
        mat_ligne.append(1)
    elif i % 2 == 1:
        mat_ligne.append(0)

# Comparaison avec la matrice ligne

def extraction_ligne(matrice, x, y, sens):
    "extrais d'une matrice une matrice de ligne"
    res = []
    if sens == "h" :
        for i in range(len(mat_ligne)):
            res.append(matrice[x+i][y])
    elif sens == "v" :
        for i in range(len(mat_ligne)):
            res.append(matrice[x][y+i])
    return res


def comparaison_ligne(matrice_a_comparer, x, y, sens):
    "Compare une matrice à partire des position x et y avec la matrice pointiller, retourne True si pareil, faux si différent"
    cpt = 0
    matrice_a_comparer_tourne = extraction_ligne(matrice_a_comparer, x, y, sens)
    for i in range(len(mat_ligne)):
        if matrice_a_comparer_tourne[i] == mat_ligne[i]:
            cpt += 1
        else:
            cpt += 0
    if cpt == len(mat_ligne):
        return True
    else:
        return False


def regarde_coin_25(matrice):
    "Sur la matrice de 25/25, regarde où il y a des coins et retourne le nombre de rotation à faire"
    mat_hd = rotation_multiple(recup_coin(matrice, 0, 25-8), 3)
    mat_bg = rotation(recup_coin(matrice, 25-8, 0))
    mat_bd = rotation_multiple(recup_coin(matrice, 25-8, 25-8), 2)
    coin_haut_gauche = comparaison_coin(matrice, 0, 0)
    coin_haut_droite = comparaison_coin(mat_hd, 0, 0)
    coin_bas_gauche = comparaison_coin(mat_bg, 0, 0)
    coin_bas_droite = comparaison_coin(mat_bd, 0, 0)
    if not(coin_bas_droite):
        return 0
    elif not(coin_bas_gauche):
        return 3
    elif not(coin_haut_droite):
        return 1
    elif not(coin_haut_gauche):
        return 2


def inverse_pour_modify(matrice):
    "transphorme les 1 en 0 et les 0 en 1"
    mat = []
    for i in range(len(matrice)):
        mat.append([])
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                mat[i].append(0)
            else:
                mat[i].append(1)
    return mat


def rotation_multiple(matrice, nbr_rotation):
    "appel plusieurs fois rotation"
    global mat_charger
    mat = matrice
    while nbr_rotation != 0:
        mat = rotation(mat)
        nbr_rotation -= 1
    modify(inverse_pour_modify(mat))
    mat_charger = mat
    return mat


def rotation(matrice):
    "fait tournée une matrice sur la droite"
    matrice_tourne = []

    for i in range(nbrCol(matrice)):
        matrice_tourne.append([])
        for j in range(nbrLig(matrice)):
            matrice_tourne[i].append([])
    # tourne 1 fois à droite
    for i in range(nbrLig(matrice)):
        for j in range(nbrCol(matrice)):
            matrice_tourne[i][j] = matrice[-j-1][i]

    return matrice_tourne


############### QUESTION 3 ###################################@


def code_Hamming(liste):
    #prend en compte les 7 erreures possibles et les modifies, et met dans un nouvelle liste les 4 bits d'informations
    res = []
    c1 = (liste[0]+liste[1]+liste[3]) % 2
    c2 = (liste[0]+liste[2]+liste[3]) % 2
    c3 = (liste[1]+liste[2]+liste[3]) % 2
    if (c1 != liste[4] and c2 != liste[5] and c3 == liste[6]):
        liste[0] = (liste[0]+1) % 2
    if (c1 != liste[4] and c3 != liste[6]) and c2 == liste[5]:
        liste[1] = (liste[1]+1) % 2
    if (c2 != liste[5] and c3 != liste[6]) and c1 == liste[4]:
        liste[2] = (liste[2]+1) % 2
    if c2 != liste[5] and c3 != liste[6] and c1 != liste[4]:
        liste[3] = (liste[3]+1) % 2
    if c1 != liste[4] and (c2 == liste[5] and c3 == liste[6]):
        liste[4] = (liste[4]+1) % 2
    if c2 != liste[5] and (c1 == liste[4] and c3 == liste[6]):
        liste[5] = (liste[5]+1) % 2
    if c3 != liste[6] and (c2 == liste[5] and c1 == liste[4]):
        liste[6] = (liste[6]+1) % 2

    res.append(liste[0])
    res.append(liste[1])
    res.append(liste[2])
    res.append(liste[3])

    return res

############### QUESTION 4 ##################
# J

res = [[], []]


def extraction_1_bloc(x, y):
    "lit un morceau de la matrice charger de 2/7 et retourne les données brutes"
    global res
    res = [[], []]
    for i in range(2):
        for j in range(7):
            res[i].append(mat_charger[x+i][y+j])
    return res


mat_lecture = [[2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2]]

def lecture_1_bloc_de_droite_a_gauche(x, y):
    "récupere un bloc et remet dans un nouvelle liste les bits dans le bon ordre pour quand on veut lire le bloc de droite a gauche"
    global mat_lecture
    extraction_1_bloc(x, y)
    k = 0
    for j in range(7):
        if j % 2 == 0:
            mat_lecture[0][j] = res[(j+1) % 2][-1-k]
            mat_lecture[1][j] = res[j % 2][-4-k]
            k += 1
        else:
            k -= 1
            mat_lecture[0][j] = res[(j+1) % 2][-1-k]
            k += 1
            mat_lecture[1][j] = res[j % 2][-4-k]
    mat_lecture[0][6] = res[1][3]
    mat_lecture[1][6] = res[0][0]
    return mat_lecture



def lecture_1_bloc_de_gauche_a_droite(x, y):
    "récupere un bloc et remet dans un nouvelle liste les bits dans le bon ordre pour quand on veut lire le bloc de gauche a droite"
    global mat_lecture
    extraction_1_bloc(x, y)
    k = 0
    for j in range(7):
        if j % 2 == 0:
            mat_lecture[0][j] = res[(j+1) % 2][k]
            mat_lecture[1][j] = res[j % 2][3+k]
            k += 1
        else:
            k -= 1
            mat_lecture[0][j] = res[(j+1) % 2][k]
            k += 1
            mat_lecture[1][j] = res[j % 2][3+k]
    mat_lecture[0][6] = res[1][3]
    mat_lecture[1][6] = res[0][6]

    return mat_lecture


def lecture_1_bloc(x, y):
    "lit un bloc de droite à gauche ou de gauche à droite en fonction de ou se trouve le bloc dans le QRcode"
    if x == 11 or x == 15 or x == 19 or x == 23:
        return lecture_1_bloc_de_droite_a_gauche(x, y)
    else:
        return lecture_1_bloc_de_gauche_a_droite(x, y)


def decoder():
    "lit le QRcode dans le sens demandé: prend le bloc de la fin puis lits les blocs à gauche, en haut, à droite, en haut,..."
    x = 23
    y = 18
    for i in range(lecture_nmbr_bloc()):
        if i == 0 or i == 4 or i == 8 or i == 12 or i == 16:
            question5(code_Hamming(lecture_1_bloc(x-i, y)[0]), code_Hamming(lecture_1_bloc(x-i, y)[1]))
        if i == 1 or i == 5 or i == 9 or i == 13:
            question5(code_Hamming(lecture_1_bloc(x-i+1, y-7)[0]), code_Hamming(lecture_1_bloc(x-i+1, y-7)[1]))
        if i == 2 or i == 6 or i == 10 or i == 14:
            question5(code_Hamming(lecture_1_bloc(x-i, y-7)[0]), code_Hamming(lecture_1_bloc(x-i, y-7)[1]))
        if i == 3 or i == 7 or i == 11 or i == 15:
            question5(code_Hamming(lecture_1_bloc(x-i+1, y)[0]), code_Hamming(lecture_1_bloc(x-i+1, y)[1]))

############### QUESTION 5 ##################


def question5(liste1, liste2):
    "lit un bloc et retourne le message en ASCII ou Hexadécimal"
    global message
    s1 = 0
    s2 = 0
    s = 0
    liste = liste1+liste2
    ######## Hexadecimal #######
    "lit la premiere partie du bloc et renvoie sa valeur en hexadecimal"
    if mat_charger[24][8] == 1:
        for i in range(len(liste1)):
            s1 += (liste1[i]*(2**i))
        if s1 == 10:
            s1 = "A"
        if s1 == 11:
            s1 = "B"
        if s1 == 12:
            s1 = "C"
        if s1 == 13:
            s1 = "D"
        if s1 == 14:
            s1 = "E"
        if s1 == 15:
            s1 = "F"
        message += str(s1)#str manger
        "lit la deuxieme partie du bloc et renvoie sa valeur en hexadecimal"
        for i in range(len(liste2)):
            s2 += (liste2[i]*(2**i))
        if s2 == 10:
            s2 = "A"
        if s2 == 11:
            s2 = "B"
        if s2 == 12:
            s2 = "C"
        if s2 == 13:
            s2 = "D"
        if s2 == 14:
            s2 = "E"
        if s2 == 15:
            s2 = "F"
        message += str(s2) #str manger
    ############# ASCII ############
        "lit le bloc en entier et renvoie sa valeur en ascii"
    else:
        liste3 = []
        for i in range(len(liste)-1):
            liste3.append(liste[-i])
        print(liste3)
        for i in range(len(liste3)):
            s += (liste3[-i-1]*(2**i))
        s = chr(s)
        message += s


################ QUESTION 6 ################


def filtre_00(mat):
    "fait un xor entre la matrice 00 et la partie du QRcode auquel on applique le filtre"
    mat_00 = [[0]*14]*16
    for i in range(9, 25):
        for j in range(11, 25):
            mat[i][j] = mat[i][j] ^ mat_00[i-9][j-11]
            modify(inverse_pour_modify(mat))


# création de la matrice 01 (un damier dont la case en haut à gauche est noire

mat_01 = [[1]*14 for k in range(16)]

for i in range(nbrLig(mat_01)):
    for j in range(nbrCol(mat_01)):
        if i % 2 == 0 and j % 2 == 0:
            mat_01[i][j] = 0
        if i % 2 == 1 and j % 2 == 1:
            mat_01[i][j] = 0


def filtre_01(mat):
    "fait un xor entre la matrice 01 et la partie du QRcode auquel on applique le filtre"
    for i in range(nbrLig(mat_01)):
        for j in range(nbrCol(mat_01)):
            mat[i+9][j+11] = mat[i+9][j+11] ^ mat_01[i][j]
            modify(inverse_pour_modify(mat))

# création de la matrice 10 (des lignes horizontales altern ́ees noires et blanches, la plus haute  ́etant noire

mat_10 = [[1]*14 for k in range(16)]
for i in range(nbrLig(mat_10)):
    for j in range(nbrCol(mat_10)):
        if i % 2 == 0:
            mat_10[i][j] = 0


def filtre_10(mat):
    "fait un xor entre la matrice 10 et la partie du QRcode auquel on applique le filtre"
    for i in range(nbrLig(mat_10)):
        for j in range(nbrCol(mat_10)):
            mat[i][j] = mat[i][j] ^ mat_10[i][j]
            modify(inverse_pour_modify(mat))

# création de la matrice 11 (des lignes verticales altern ́ees noires et blanches, la plus `a gauche  ́etant noire

mat_11 = [[1]*14 for k in range(16)]

for i in range(nbrLig(mat_11)):
    for j in range(nbrCol(mat_11)):
        if j % 2 == 0:
            mat_11[i][j] = 0


def filtre_11(mat):
    "fait un xor entre la matrice 11 et la partie du QRcode auquel on applique le filtre"
    for i in range(nbrLig(mat_11)):
        for j in range(nbrCol(mat_11)):
            mat[i+9][j+11] = mat[i+9][j+11] ^ mat_11[i][j]
            modify(inverse_pour_modify(mat))


def filtre():
    if (1-mat_charger[22][8]) == 0:
        if (1-mat_charger[23][8]) == 0:
            filtre_00(mat_charger)
        else:
            filtre_01(mat_charger)
    else:
        if (1-mat_charger[23][8]) == 0:
            filtre_10(mat_charger)
        else:
            filtre_11(mat_charger)

################ QUESTION 7 ################


def lecture_nmbr_bloc():
    """lit de (13,0) a (17,0) pour déterminer le nombre de bloc à lire (res)"""
    res = []
    s = 0
    for i in range(5):
        res.append(mat_charger[13+i][0])
    if len(res) == 5:
        for i in range(len(res)):
            s += (res[i]*(2**i))

    return s


def lire():
    "lance toute les étapes de la lecture : rotation, filtre, décodage"
    global message
    message = ""
    rotation_multiple(mat_charger, regarde_coin_25(mat_charger))
    if comparaison_ligne(mat_charger, 6, 8,"v") and comparaison_ligne(mat_charger, 8, 6,"h"):
        filtre()
        decoder()
        Label_message.configure(text="message : " + message)
        print("message : ", message,)

################
# Tkinter


racine = tk.Tk()


Bouton_charger = tk.Button(racine, text="charger", command=lambda: charger(racine))
Bouton_charger.grid(row=5, column=1)

Bouton_lire = tk.Button(racine, text="lire", command=lambda: lire())
Bouton_lire.grid(row=5, column=2)

Label_message = tk.Label(racine, text="")
Label_message.grid(row=6, column=1, columnspan=2)

racine.mainloop()
