# Créé par THEO.PIPELIER, le 12/04/2024 en Python 3.7

"""
Programme du tron
nom(s), prÃ©nom(s), classe(s)
"""
import pygame
from random import *


LARGEUR=512
HAUTEUR=512
ROUGE=(255,0,0)
VERT=(0,255,0)
BLEU=(0,0,255)
NOIR=(0,0,0)
BLEUP=(169, 234, 254)
ORANGE=(244, 102, 27)
BLANC=(224, 233, 246)


pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")
font = pygame.font.Font('freesansbold.ttf', 20)
frequence = pygame.time.Clock()
direction = 'haut'
direction2 = 'haut'
tempsPartie=0
AssuranceDepart=1
AssuranceDepart2=1
manche=0

P=0
P2=0
score1=0
score2=0
SPAWNX=LARGEUR-50
SPAWNY=HAUTEUR-100
motoX2=randint(50,SPAWNX)
motoY2=randint(100,SPAWNY)
motoX=randint(50,SPAWNX)
motoY=randint(100,SPAWNY)
image_fond = pygame.image.load('tron.jpg')
image_fond = pygame.transform.scale(image_fond, (LARGEUR, HAUTEUR))
pygame.mixer.init()
son = pygame.mixer.Sound("tron.wav")
joueur1=''
joueur2=''
quitName=0
def afficher_nom():
    fenetre.fill(NOIR)
    texte_surface = font.render("Nom du joueur 1 en trois caractères: " + joueur1, True, ORANGE)
    fenetre.blit(texte_surface, (LARGEUR // 2 - texte_surface.get_width() // 2, HAUTEUR // 2))
    pygame.display.flip()
def afficher_nom2():
    fenetre.fill(NOIR)
    texte_surface = font.render("Nom du joueur 2 en trois caractères: " + joueur2, True, BLEUP)
    fenetre.blit(texte_surface, (LARGEUR // 2 - texte_surface.get_width() // 2, HAUTEUR // 2))
    pygame.display.flip()
def createName():
    global joueur1,q,quitName
    continuer = True
    while continuer:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    continuer = False

                elif event.key == pygame.K_BACKSPACE:
                    joueur1 = joueur1[:-1]
                elif event.key == pygame.K_ESCAPE:
                    q+=1
                    quitName+=1
                    continuer = False

                else:
                    joueur1 += event.unicode

        afficher_nom()

def createName2():
    global joueur2,quitName
    continuer = True
    while continuer==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    continuer = False
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE or quitName == 1:
                    continuer = False
                elif event.key == pygame.K_RETURN:
                    continuer = False
                elif event.key == pygame.K_BACKSPACE:
                    joueur2 = joueur1[:-1]
                else:
                    joueur2 += event.unicode

        afficher_nom2()
def format_score(score):
    """
    Formater le score avec 8 chiffres
    """
    return "{:08d}".format(score)

def dessineScore():
    fenetre.fill(NOIR)
    mancheAfficher = font.render("Manche : "+str(manche),True,BLANC)
    fenetre.blit(mancheAfficher, (LARGEUR // 2 - mancheAfficher.get_width() // 2, HAUTEUR // 4))
    TableauAfficher = font.render("Score :",True,BLEU)
    fenetre.blit(TableauAfficher, (LARGEUR // 2 - TableauAfficher.get_width() // 2, (HAUTEUR // 4) +40))
    quitterAfficher = font.render("Appuyez sur Echap pour quitter ", True, BLANC)
    fenetre.blit(quitterAfficher, (LARGEUR // 2 - quitterAfficher.get_width() // 2, (HAUTEUR // 2)+140))
    joueur1Afficher = font.render(joueur1+"  "+format_score(score1), True, BLEU)
    joueur2Afficher = font.render(joueur2+"  "+format_score(score2), True, BLEU)
    fenetre.blit(joueur1Afficher, ((LARGEUR //2 - joueur1Afficher.get_width())+70, HAUTEUR // 2))
    fenetre.blit(joueur2Afficher, ((LARGEUR //2 - joueur2Afficher.get_width())+70, (HAUTEUR // 3)+40))
    if score2>score1:
        gagnant=joueur2
        Colours=BLEUP
    else:
        gagnant=joueur1
        Colours=ORANGE
    gagnantAfficher = font.render("Victoire de : "+gagnant, True, Colours)
    fenetre.blit(gagnantAfficher, (LARGEUR // 2 - gagnantAfficher.get_width() // 2, (HAUTEUR // 2)+100))



def dessineAccueil():
    fenetre.blit(image_fond, (0, 0))
    instructions = font.render("Appuyez sur espace pour commencer", True, BLANC)
    mancheAfficher = font.render("Manche : "+str(manche),True,BLANC)
    fenetre.blit(instructions, (LARGEUR // 2 - instructions.get_width() // 2, HAUTEUR // 2))
    fenetre.blit(mancheAfficher, (LARGEUR // 2 - mancheAfficher.get_width() // 2, HAUTEUR // 3))
    quitterAfficher = font.render("Appuyez sur Echap pour quitter ", True, BLANC)
    fenetre.blit(quitterAfficher, (LARGEUR // 2 - quitterAfficher.get_width() // 2, (HAUTEUR // 2)+140))
    joueur1Afficher = font.render(joueur1+" : "+str(P2), True, ORANGE)
    joueur2Afficher = font.render(joueur2 +" : "+str(P), True, BLEUP)
    fenetre.blit(joueur1Afficher, ((LARGEUR - LARGEUR//2)+40, (HAUTEUR // 2)+50))
    fenetre.blit(joueur2Afficher, ((LARGEUR //4)+40 , (HAUTEUR // 2)+50))


def dessineDecor():
    """
    dessine un decor
    """
    for i in range(15):
        pygame.draw.rect(fenetre, ORANGE,[1, 1, LARGEUR-1, HAUTEUR-1],1)
        pygame.draw.circle(fenetre, ORANGE, (randint(1,LARGEUR),randint(1,HAUTEUR)), 10)
        pygame.draw.rect(fenetre, BLEU, [randint(1,LARGEUR),randint(1,HAUTEUR), 10, 10],0)
    pygame.draw.rect(fenetre,NOIR, [motoX2-50,motoY2-50, 100, 100],0) ;
    pygame.draw.rect(fenetre,NOIR, [motoX-50,motoY-50, 100, 100],0) ;





def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnÃ©es x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    global P,tempsPartie,score2
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond Ã  une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
        P+=1
        if 200>tempsPartie>100:
            score2+=500
        elif tempsPartie<100:
            score2+=750
        else:
            score2+=250
    return collision

def collisionMur2(x,y):
    global P2,tempsPartie,score1
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond Ã  une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme2=color[0]+color[1]+color[2]
    if somme2==0:
        collision2=False
    else:
        collision2=True
        P2+=1
        if 200>tempsPartie>100:
            score1+=500
        elif tempsPartie<100:
            score1+=750
        else:
            score1+=250
    return collision2




def deplacementmoto2():
    """
    deplace la moto si c'est possible
    """
    global motoX2,motoY2


    touche=False
    if direction2=='haut':
        x=motoX2
        y=motoY2-1
        touche=collisionMur2(x,y)
    elif direction2=='bas':
        x=motoX2
        y=motoY2+1
        touche=collisionMur2(x,y)
    elif direction2=='droite':
        x=motoX2+1
        y=motoY2
        touche=collisionMur2(x,y)
    elif direction2=='gauche':
        x=motoX2-1
        y=motoY2
        touche=collisionMur2(x,y)
    if touche==False:
        motoX2=x
        motoY2=y

    fenetre.set_at((x, y), BLEUP)
    return touche

def deplacementmoto():
    """
    deplace la moto si c'est possible
    """

    global motoX,motoY,P

    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX
        y=motoY+1
        touche=collisionMur(x,y)
    elif direction=='droite':
        x=motoX+1
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:
        motoX=x
        motoY=y
    fenetre.set_at((x, y), ORANGE)
    return touche

def accueil():
    global q,manche
    dessineAccueil()
    pygame.display.flip()
    lobby=True
    while lobby==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                q+=1
                lobby= False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    q+=1
                    lobby= False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            lobby= False

def EcrandeScore():
    global q
    dessineScore()
    pygame.display.flip()
    AFscore=True
    while AFscore==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                AFscore= False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    q+=1
                    AFscore= False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            Score= False




def game():
    global tempsPartie,direction,direction2,motoX,motoX2,motoY,motoY2,manche
    manche+=1
    SPAWNX=LARGEUR-50
    SPAWNY=HAUTEUR-100
    motoX2=randint(50,SPAWNX)
    motoY2=randint(100,SPAWNY)
    motoX=randint(50,SPAWNX)
    motoY=randint(100,SPAWNY)
    fenetre.fill((0,0,0))
    dessineDecor()
    pygame.display.flip()
    son.play()
    jeu=True
    while jeu==True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jeu = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and direction!= 'bas':
            direction = 'haut'
        elif keys[pygame.K_DOWN] and direction!='haut':
            direction = 'bas'
        elif keys[pygame.K_RIGHT] and direction!='gauche':
            direction = 'droite'
        elif keys[pygame.K_LEFT] and direction!='droite':
            direction = 'gauche'
        elif keys[pygame.K_z] and direction2!='bas':
            direction2 = 'haut'
        elif keys[pygame.K_s] and direction2!='haut':
            direction2 = 'bas'
        elif keys[pygame.K_d] and direction2!='gauche':
            direction2 = 'droite'
        elif keys[pygame.K_q] and direction2!='droite':
            direction2 = 'gauche'


        if deplacementmoto()==True or deplacementmoto2() :
            jeu=False
        frequence.tick(60)
        pygame.display.update()
        tempsPartie+=1
    son.stop()


loop=True
dessineDecor()
while loop==True:
    q=0
    if manche==0:
        createName()
        compteur=0
        for i in range(len(joueur1)):
                compteur+=1
        while compteur!=3 and q!=1:
            compteur=0
            createName()
            for i in range(len(joueur1)):
                    compteur+=1
            print(joueur1)
        createName2()
        compteur=0
        for i in range(len(joueur2)):
                compteur+=1
        while compteur!=3 and q!=1:
            compteur=0
            createName()
            for i in range(len(joueur2)):
                    compteur+=1
            print(joueur2)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
    if q == 1:
        pygame.quit()
    tempsPartie = 0
    accueil()
    if q == 1:
        pygame.quit()
    game()

    if P==3 or P2== 3:
        EcrandeScore()


pygame.quit()
print('perdu')
print('temps partie',tempsPartie)
