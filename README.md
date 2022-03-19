# projet-QRcode
###code déjà fourni qui permet de charger et sauvegarder une image en noir et blanc dans le fichier projet.py###

import PIL as pil
from PIL import Image
from PIL import ImageTk 


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
mat_carre=[[0,0,0,255]*8 for k in range (8)]
def carre():
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

### je ne comprends pas ca ne m'affiche rien... ca fait deux heures que je suis dessus juste pour avoir fait ca, j'en ai marre je reprendrais plus trad mais je le push quand meme au cas où tu veuilles travailler dessus aussi.
