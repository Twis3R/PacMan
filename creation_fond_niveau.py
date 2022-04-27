import pygame
from pygame.locals import *
from constante import *
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))

#chargement du fond
fond=pygame.image.load(image_fond).convert()
fenetre.blit(fond,(0,0))

#Titre
pygame.display.set_caption("Pac Man")

#chargement des images
mur = pygame.image.load(image_mur).convert()
nourriture = pygame.image.load(image_nourriture).convert()
nourriture = pygame.transform.scale(nourriture,(taille_sprite,taille_sprite)) #redimension de l'image à la taille d'un sprite
pac=pygame.image.load(image_icone).convert()
pac = pygame.transform.scale(pac,(taille_sprite,taille_sprite))

#création des lignes
Ligne1=list('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
Ligne2=list('mNNNNNNNNNNNNNNNNNNNNNNNNNNNNm')
Ligne3=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne4=list('mNmBBBmNmBBBmNmmNmBBBmNmBBBmNm')
Ligne5=list('mNmBBBmNmBBBmNmmNmBBBmNmBBBmNm')
Ligne6=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne7=list('mNNNNNNNNNNNNNNNNNNNNNNNNNNNNm')
Ligne8=list('mmmmmNmmmmmmNmmmmNmmmmmmNmmmmm')
Ligne9=list('mBBBmNmNNNNNNNNNNNNNNNNmNmBBBm')
Ligne10=list('mBBBmNmNmmmmmNmmNmmmmmNmNmBBBm')
Ligne11=list('mBBBmNmNmmmmmNmmNmmmmmNmNmBBBm')
Ligne12=list('mBBBmNmNNNNNNNNNNNNNNNNmNmBBBm')
Ligne13=list('mmmmmNmmmmmmNmmmmNmmmmmmNmmmmm')
Ligne14=list('mNNNNNNNNNNNNNNNNNNNNNNNNNNNNm')
Ligne15=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne16=list('mNmBBBmNmBBBmNmmNmBBBmNmBBBmNm')
Ligne17=list('mNmBBBmNmBBBmNmmNmBBBmNmBBBmNm')
Ligne18=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne19=list('mNNNNNNNNNNNNNNNNNNNNNNNNNNNNm')
Ligne20=list('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

L=[Ligne1,Ligne2,Ligne3,Ligne4,Ligne5,Ligne6,Ligne7,Ligne8,Ligne9,Ligne10,Ligne11,Ligne12,Ligne13,Ligne14,Ligne15,Ligne16,Ligne17,Ligne18,Ligne19,Ligne20]

def fond_niveau(L):
    numero_ligne=0
    for ligne in L:
        numero_case=0
        #parcours de la ième Ligne
        for sprite in ligne:
            #position du coin supérieur gauche du sprite à afficher
            x=numero_case*taille_sprite
            y=numero_ligne*taille_sprite
            if sprite=="N":
                fenetre.blit(nourriture,(x,y))
            elif sprite=="m" :
                fenetre.blit(mur,(x,y))
            numero_case=numero_case+1
        numero_ligne=numero_ligne+1
    pygame.image.save(fenetre,'images/niveau.bmp')

##fond_niveau(L)
##pac=pygame.image.load(image_icone).convert()
##pac = pygame.transform.scale(pac,(30,30))
##fenetre.blit(pac,(30,30))



###fermeture fenêtre
##pygame.display.update()
##pygame.time.wait(3000) #attend 3000ms avant de terminer
##pygame.quit()