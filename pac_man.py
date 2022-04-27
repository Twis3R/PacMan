import pygame
from pygame.locals import *
from constante import*
from creation_fond_niveau import*
pygame.init()

#chargement et affichage de l'image du niveau
fond_niveau(L)
image_niveau = "images/niveau.bmp"
fond_niveau = pygame.image.load(image_niveau).convert_alpha()
fenetre.blit(fond_niveau,(0,0))
pygame.display.flip()

#affichage Pac Man
pac=pygame.image.load(image_icone).convert_alpha()
pac=pygame.transform.scale(pac,(30,30)) ## redimensionne l'image
position_perso = pac.get_rect() ##récupère les coord du personnage
position_perso = position_perso.move(30,30) ##deplacer perso en (30,30)
fenetre.blit(pac,position_perso)
pygame.display.flip() ##actualisation de l'affichage

#chargement de l'image noir
noir=pygame.image.load(image_sprite_noir).convert_alpha()
noir=pygame.transform.scale(noir,(30,30))

#i et j compteurs pour parcourir la liste de listes L -> savoir si mur ?
i=1
j=1
L[i][j]='V' #case vide

#initialisation boucle principale infinie
continuer=True
compteur_nourriture=0
while continuer==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            continuer=False
            break
        #gérer le déplacement au clavier
        if event.type==KEYDOWN :
            if event.key==K_DOWN : #flèche du bas
                if 1<=i<=(nbr_sprite_largeur-2) and L[i+1][j]!= 'm':
##                    fenetre.blit(fond_niveau,(0,0))
                    fenetre.blit(noir,position_perso)
                    position_perso=position_perso.move(0,taille_sprite)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i+1][j]=='N':
                        compteur_nourriture=compteur_nourriture+1
                        L[i+1][j]='V'
                    i=i+1
            if event.key==K_UP : #flèche du haut
                if 1<=i<=(nbr_sprite_largeur-2) and L[i-1][j]!= 'm':
##                    fenetre.blit(fond_niveau,(0,0))
                    fenetre.blit(noir,position_perso)
                    position_perso=position_perso.move(0,-taille_sprite)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i-1][j]=='N':
                        compteur_nourriture=compteur_nourriture+1
                        L[i-1][j]='V'
                    i=i-1
            if event.key==K_LEFT : #flèche de gauche
                if 1<=j<=(nbr_sprite_longueur-2) and L[i][j-1]!= 'm':
##                    fenetre.blit(fond_niveau,(0,0))
                    fenetre.blit(noir,position_perso)
                    position_perso=position_perso.move(-taille_sprite,0)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i][j-1]=='N':
                        compteur_nourriture=compteur_nourriture+1
                        L[i][j-1]='V'
                    j=j-1
            if event.key==K_RIGHT : #flèche de gauche
                if 1<=j<=(nbr_sprite_longueur-2) and L[i][j+1]!= 'm':
##                    fenetre.blit(fond_niveau,(0,0))
                    fenetre.blit(noir,position_perso)
                    position_perso=position_perso.move(taille_sprite,0)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i][j+1]=='N':
                        compteur_nourriture=compteur_nourriture+1
                        L[i][j+1]='V'
                    j=j+1
            print("Pac-gommes :",compteur_nourriture)












#fermeture fenetre
pygame.display.update()
pygame.time.wait(3000) # attend 3000 ms avant de terminer
pygame.quit()