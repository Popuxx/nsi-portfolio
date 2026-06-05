#Projet NFT art: Manel GORDO, Paul Julliard, Santiago Gomez-Roca, Jacques Giraud-Patino

#Code de Manel Gordo (Partie en bas à gauche de la grande figure)

from turtle import*
setup(800,800) #Fenêtre du projet
up()
goto (-400,-400)
down()
speed(500)

def carre(n):
    """fonction carré utilisé tout au long du projet"""
    for i in range(4):
        forward(n)
        left(90)
carre(400)



def triangle (longueur,x,y,c):
    """fonction qui trace un triangle avec les coordonnées souhaitées"""
    position(x,y) #fait appel à la fonction position
    color(c) #Permet de choisir la couleur voulue (définie avec le paramètre "c")
    for i in range(2): #répéter 2 fois
        left(90) #tourner de 90°
        forward (longueur) #avancer de la longueur voulue, utilele pour les fonctions d'après
    left(45)
    goto (x,y)
#triangle(100,10,10,"pink")
#carre(100)



#fonction qui déplace la tortue à des coordonnés sans dessiner pour gagner du temps
def position(x,y):
    up()
    goto(x,y)
    down()



#Début du code des figures


# Figure 1 : bandes bleues et blanches horizontales

x0, y0 = -400, -400      # coin inférieur gauche du carré
x1 = -300                # coin inférieur droit du carré
hauteur = 100 / 7        # hauteur d'une bande (7 bandes au total)

# Bande 1 (bleue)
fillcolor("cornflowerblue")
begin_fill()
position(x0, y0)               # départ du bas gauche
goto(x1, y0)                   # bas droit
goto(x1, y0 + hauteur)         # haut droit
goto(x0, y0 + hauteur)         # haut gauche
goto(x0, y0)                   # retour au point de départ
end_fill()

# Bande 2 (blanche)
fillcolor("white")
begin_fill()
position(x0, y0 + hauteur)
goto(x1, y0 + hauteur)
goto(x1, y0 + 2 * hauteur)
goto(x0, y0 + 2 * hauteur)
goto(x0, y0 + hauteur)
end_fill()

# Bande 3 (bleue)
fillcolor("cornflowerblue")
begin_fill()
position(x0, y0 + 2 * hauteur)
goto(x1, y0 + 2 * hauteur)
goto(x1, y0 + 3 * hauteur)
goto(x0, y0 + 3 * hauteur)
goto(x0, y0 + 2 * hauteur)
end_fill()

# Bande 4 (blanche)
fillcolor("white")
begin_fill()
position(x0, y0 + 3 * hauteur)
goto(x1, y0 + 3 * hauteur)
goto(x1, y0 + 4 * hauteur)
goto(x0, y0 + 4 * hauteur)
goto(x0, y0 + 3 * hauteur)
end_fill()

# Bande 5 (bleue)
fillcolor("cornflowerblue")
begin_fill()
position(x0, y0 + 4 * hauteur)
goto(x1, y0 + 4 * hauteur)
goto(x1, y0 + 5 * hauteur)
goto(x0, y0 + 5 * hauteur)
goto(x0, y0 + 4 * hauteur)
end_fill()

# Bande 6 (blanche)
fillcolor("white")
begin_fill()
position(x0, y0 + 5 * hauteur)
goto(x1, y0 + 5 * hauteur)
goto(x1, y0 + 6 * hauteur)
goto(x0, y0 + 6 * hauteur)
goto(x0, y0 + 5 * hauteur)
end_fill()

# Bande 7 (bleue)
fillcolor("cornflowerblue")
begin_fill()
position(x0, y0 + 6 * hauteur)
goto(x1, y0 + 6 * hauteur)
goto(x1, y0 + 7 * hauteur)
goto(x0, y0 + 7 * hauteur)
goto(x0, y0 + 6 * hauteur)
end_fill()

# Chaque bloc trace une bande horizontale remplie d'une couleur différente.
# Les coordonnées sont calculées pour se placer juste au-dessus de la précédente.
# L'ensemble forme un carré de 100x100 avec 7 bandes de même taille.

# Figure d'un carré en relief
def manel_figurecube (longueur,position_x,position_y):
    position(position_x,position_y)      # place la tortue à la position donnée (coin inférieur gauche du cube)
    fillcolor("yellow")                  # couleur du carré principal (face avant)
    begin_fill()
    carre (longueur)                     # trace le carré de base
    end_fill()

    fillcolor("white")                   # couleur du carré supérieur (face claire du cube)
    begin_fill()
    forward (longueur*(5/11))            # décale légèrement vers la droite pour placer la deuxième face
    carre(longueur*(6/11))               # trace un carré plus petit, décalé
    end_fill()

    fillcolor("cornflowerblue")          # couleur du côté en perspective (face latérale)
    left(90)                             # tourne vers le haut pour commencer ce côté
    begin_fill()
    forward(longueur*(6/11))             # monte la hauteur du côté bleu
    left(45)                             # tourne pour rejoindre l’angle du grand carré
    goto(position_x,position_y+longueur) # relie au sommet gauche du grand carré
    left(45)                             # ajuste l’orientation pour fermer la face
    goto(position_x,position_y)          # revient au point de départ
    end_fill()

# appel de la fonction avec taille 100 et position (-300, -100)
manel_figurecube(100,-300,-100)



# Figure de 2 rectangles qui coupe un des carré

fillcolor("yellow")              # couleur de remplissage du premier carré (jaune)
position(-200,-200)              # place la tortue au coin inférieur gauche du carré jaune
begin_fill()
carre(100)                       # trace un carré jaune de 100x100
end_fill()

position(-250,-300)              # se déplace pour placer le rectangle bleu en dessous du carré jaune
right(180)                       # oriente la tortue dans la direction opposée
fillcolor("cornflowerblue")      # couleur bleue pour le rectangle
begin_fill()
setheading(0)                    # réinitialise l'orientation vers la droite (0°)
for i in range(2):               # boucle pour dessiner un rectangle (2 côtés longs, 2 côtés courts)
    left(90)                     # tourne à gauche de 90°
    forward(100)                 # côté vertical du rectangle
    left(90)                     # tourne à gauche à nouveau pour tracer le côté horizontal
    forward(50)                  # côté horizontal du rectangle
end_fill()


# Figure d'un carrer rose incliné
position(-300,-200)              # positionne la tortue pour dessiner un carré noir (contour)
carre(100)                       # trace un carré vide (juste le contour noir)
position(-250,-185)              # déplace légèrement la tortue pour centrer le carré rose à l'intérieur
fillcolor("pink")                # couleur rose pour le carré intérieur
setheading(45)                   # oriente la tortue en diagonale (45°)
begin_fill()
carre(50)                        # trace un carré rose incliné
end_fill()


# Figure d'un étoile à 8 branches

position(-400, -300)         # place la tortue au coin inférieur gauche du carré rose
setheading(0)                # oriente la tortue vers la droite (angle 0°)

fillcolor("pink")            # couleur du carré de fond
begin_fill()
for _ in range(4):           # boucle pour tracer les 4 côtés du carré
    forward(100)             # avance de 100 unités (longueur d’un côté)
    left(90)                 # tourne à gauche de 90° pour former les angles droits
end_fill()                   # termine le remplissage rose du carré

# se placer au centre du carré
up()                         # lève le stylo pour se déplacer sans dessiner
forward(50)                  # avance jusqu’au milieu du carré (horizontalement)
left(90)                     # tourne vers le haut
forward(50)                  # avance jusqu’au centre verticalement
down()                       # baisse le stylo pour recommencer à dessiner

color("yellow")              # fixe la couleur du trait en jaune
fillcolor("yellow")          # couleur intérieure des branches
width(8)                     # augmente l’épaisseur du tracé pour bien voir les branches

begin_fill()
for i in range(8):           # boucle pour créer les 8 branches de l’étoile
    forward(25)              # trace une branche vers l’extérieur
    backward(25)             # revient au centre du carré
    left(45)                 # tourne de 45° pour préparer la branche suivante
end_fill()                   # termine le remplissage jaune de l’étoile

color("black")               # repasse à la couleur noire pour les contours normaux
width(1)                     # remet l’épaisseur standard du trait



# Figure des des diagonales, la figure ou j'ai eu le plus de mal

position(-200, -400)           # place la tortue au coin inférieur gauche du carré
setheading(0)                  # oriente la tortue vers la droite (0°)
color("black")                 # fixe la couleur du trait à noir pour le contour du carré

# Dessin du carré
for _ in range(4):             # boucle pour tracer les 4 côtés du carré
    forward(100)               # trace un côté de 100 unités
    left(90)                   # tourne à gauche pour continuer le carré

# 8 bandes diagonales occupant tout le carré
x0, y0 = -200, -400            # coordonnées du coin inférieur gauche du carré
largeur = 100 / 8 * 2          # définit la largeur des bandes diagonales (deux fois plus large que les normales)

for i in range(8):             # boucle qui trace les 8 bandes diagonales
    if i % 2 == 0:             # si l’indice est pair
        fillcolor("yellow")    # la bande sera jaune
    else:                      # sinon
        fillcolor("cornflowerblue")  # la bande sera bleue
    begin_fill()
    position(x0, y0 + i * largeur)   # positionne la tortue pour commencer la bande en bas à gauche
    goto(x0 + i * largeur, y0)       # trace une diagonale vers le bas droit
    goto(x0 + (i + 1) * largeur, y0) # continue vers la droite (bord inférieur)
    goto(x0, y0 + (i + 1) * largeur) # remonte pour former la bande complète
    goto(x0, y0 + i * largeur)       # revient au point de départ
    end_fill()                       # remplit la bande de la couleur choisie

# Les diagonales dépassent, je ne saurai comment le modifier je vais donc mettre les autres dessins par dessus


# Figure des 3 triangles collés

# 1er triangle (en bas à gauche)
position(-400,-200)           # place la tortue au coin inférieur gauche du carré de base
setheading(0)                 # oriente la tortue vers la droite
carre(100)                    # trace le carré de fond servant de repère
fillcolor("yellow")           # couleur du premier triangle (jaune)
begin_fill()
position(-400,-200)           # point de départ du triangle jaune
goto(-300,-200)               # base du triangle (vers la droite)
goto(-400,-100)               # sommet du triangle (en haut à gauche)
goto(-400,-200)               # retour au point de départ pour fermer la forme
end_fill()                    # remplissage jaune terminé

# triangle bleu
fillcolor("cornflowerblue")   # couleur bleue pour le deuxième triangle
begin_fill()
position(-350,-150)           # position centrale du triangle bleu
goto(-300,-100)               # sommet supérieur droit
goto(-300,-200)               # coin inférieur droit du carré
goto(-350,-150)               # retour au point de départ pour fermer le triangle
end_fill()                    # remplissage bleu terminé

# triangle blanc
fillcolor("white")            # couleur blanche pour le troisième triangle
begin_fill()
position(-350,-150)           # départ au centre du carré
goto(-400,-100)               # coin supérieur gauche
goto(-300,-100)               # coin supérieur droit
goto(-350,-150)               # retour au point central
end_fill()                    # remplissage blanc terminé

# figure triangle blanc dans un fond rose (code de base de Paul j'ai modifié des choses pour l'adapter à mon programme)
def manel_triangleblanc (longueur,position_x,position_y):
  position(position_x,position_y)                 # place la tortue au coin inférieur gauche du carré
  fillcolor("pink")                               # couleur de fond rose
  begin_fill()
  carre(longueur)                                 # trace un carré de la taille donnée
  end_fill()

  # positionnement pour le triangle blanc
  position(position_x+longueur/2,position_y+longueur/8)  # se place au milieu de la base du carré
  fillcolor("white")                                      # couleur du triangle = blanc
  begin_fill()
  left(60)                                                # oriente la tortue pour dessiner le premier côté
  forward (longueur/2+longueur/4)                         # trace le premier côté du triangle (long)
  up()                                                    # lève le stylo pour se repositionner sans tracer
  goto(position_x+longueur/2,position_y+longueur/8)       # revient au point de départ du triangle
  down()                                                  # rebaisse le stylo pour tracer la suite
  left(60)                                                # ajuste l’angle pour le deuxième côté
  forward (longueur/2+longueur/4)                         # trace le deuxième côté du triangle
  right(120)                                              # tourne à droite pour fermer la forme
  forward (longueur/2+longueur/4)                         # trace le troisième côté pour rejoindre la base
  end_fill()                                              # termine le remplissage du triangle blanc

# appel de la fonction avec un carré de 100px en bas à gauche (-400, -100)
manel_triangleblanc(100,-400,-100)



# figure arc de cercle jaune avec un arrière plan lavender
fillcolor("lavender")                # couleur de fond du carré
position(-100,-200)                  # placement de la tortue
begin_fill()
carre(100)                           # carré de fond
end_fill()

position(0,-200)                     # départ du tracé de l’arc
fillcolor("yellow")                  # couleur jaune pour l’arc
begin_fill()
circle(100,-90)                      # arc de cercle de 90° (quart de cercle)
setheading(0)                        # réorientation vers la droite
forward(100)                         # complète la forme du quart de disque
right(90)
forward(100)
end_fill()                           # fin du remplissage



# figure arc de cercle lavender avec un arrière plan rose comme celle d'au dessus
fillcolor("pink")                    # couleur du fond
position(-200,-200)                  # position du carré de fond
begin_fill()
carre(100)
end_fill()

position(-100,-200)                  # départ du quart de cercle
fillcolor("lavender")                # couleur lavender pour l’arc
begin_fill()
setheading(180)                      # tourne la tortue vers la gauche
circle(100,90)                       # trace un quart de cercle vers le haut
setheading(0)                        # remet l’orientation de base
forward(100)                         # trace les bords droits pour fermer la forme
right(-90)
forward(100)
end_fill()

# Fond rose de la figure d'en dessous
position(-100,-100)            # place la tortue pour le carré de fond
fillcolor("pink")               # couleur du fond
begin_fill()
carre(100)                      # carré rose de 100x100
end_fill()

# Figure des 4 arcs de cercles (inspirée du code de Paul, adaptée à ce programme)
def arcsdecercles (longueur,position_init_x, position_init_y):   # fonction avec longueur et coordonnées initiales
    position(position_init_x,position_init_y)   # placement initial de la figure
    fillcolor("pink")                           # couleur de remplissage par défaut

    for i in range(2):                          # première boucle horizontale (2 colonnes)
        position(position_init_x+i*longueur,position_init_y)    # décale la position à droite
        for j in range(2):                      # deuxième boucle verticale (2 lignes)
            setheading(0)                       # remet l’orientation à droite
            begin_fill()                        # commence le remplissage
            circle(longueur,-90)                # trace un quart de cercle (sens horaire)
            left(90)                            # tourne pour fermer la forme
            triangle(longueur, position_init_x+i*longueur, position_init_y+j*longueur, "lavender")  # appelle la fonction triangle pour remplir la partie interne
            end_fill()                          # termine le remplissage

            color("black")                      # repasse en contour noir
            left(225)                           # tourne pour tracer le carré suivant
            carre(longueur)                     # trace le carré associé
            forward(longueur)                   # avance pour se replacer correctement
    up()                                        # lève le stylo pour éviter les traces

# appel de la fonction pour tracer la figure complète
arcsdecercles(50,-150,-100)


# 6 triangles jaunes, fond lavender (gauche) et blanc (droite)

# Fond lavender (colonne gauche)
fillcolor("cornflowerblue")        # couleur du fond gauche
begin_fill()
position(-300,-400)                # coin inférieur gauche
goto(-250,-400)                    # bas droit
goto(-250,-300)                    # haut droit
goto(-300,-300)                    # haut gauche
goto(-300,-400)                    # retour au point de départ
end_fill()

# Fond blanc (colonne droite)
fillcolor("white")                 # couleur du fond droit
begin_fill()
position(-250,-400)
goto(-200,-400)
goto(-200,-300)
goto(-250,-300)
goto(-250,-400)
end_fill()

# Triangles jaunes (pointe vers la droite, collés)
color("black","yellow")            # contour noir et remplissage jaune

# Triangle 1 (bas gauche)
begin_fill()
position(-300,-400)                # base gauche
goto(-250,-383)                    # pointe vers la droite
goto(-300,-366)                    # sommet haut gauche
goto(-300,-400)                    # ferme le triangle
end_fill()

# Triangle 2
begin_fill()
position(-300,-366)
goto(-250,-350)
goto(-300,-333)
goto(-300,-366)
end_fill()

# Triangle 3 (haut gauche)
begin_fill()
position(-300,-333)
goto(-250,-316)
goto(-300,-300)
goto(-300,-333)
end_fill()

# Triangle 4 (bas droite)
begin_fill()
position(-250,-400)
goto(-200,-383)
goto(-250,-366)
goto(-250,-400)
end_fill()

# Triangle 5
begin_fill()
position(-250,-366)
goto(-200,-350)
goto(-250,-333)
goto(-250,-366)
end_fill()

# Triangle 6 (haut droite)
begin_fill()
position(-250,-333)
goto(-200,-316)
goto(-250,-300)
goto(-250,-333)
end_fill()



# Figure de 4 carrés collés

# carré rose (fond)
position(0,-400)                 # coin inférieur gauche du carré de fond
fillcolor("pink")                # couleur du fond
begin_fill()
carre(100)                       # carré rose de 100x100
end_fill()

# 1er carré (en bas à gauche)
fillcolor("cornflowerblue")      # couleur bleue pour les petits carrés
begin_fill()
position(-25,-400)               # position du premier carré
setheading(45)                   # inclinaison à 45° pour le rendre en losange
carre(35)                        # petit carré bleu
end_fill()

# 2e carré (en bas à droite)
fillcolor("cornflowerblue")
begin_fill()
position(-75,-400)               # décalage vers la droite
setheading(45)
carre(35)
end_fill()

# 3e carré (en haut à gauche)
fillcolor("cornflowerblue")
begin_fill()
position(-25,-350)               # même principe, mais déplacé vers le haut
setheading(45)
carre(35)
end_fill()

# 4e carré (en haut à droite)
fillcolor("cornflowerblue")
begin_fill()
position(-75,-350)               # dernier carré, en haut à droite
setheading(45)
carre(35)
end_fill()

setheading(0)                    # remet l’orientation de la tortue à 0° pour la suite du dessin


# Figure à trois triangles colorés

# carré du quadrillage
position(-100, -300)          # coin inférieur gauche du carré
color("black")                # contour noir
carre(100)                    # carré principal du quadrillage

# moitié haute rose
fillcolor("pink")
begin_fill()
position(-100, -250)          # ligne horizontale à mi-hauteur
goto(0, -250)
goto(0, -200)
goto(-100, -200)
goto(-100, -250)
end_fill()                    # forme fermée rose (haut)

# moitié basse blanche
fillcolor("white")
begin_fill()
position(-100, -300)          # partie inférieure du carré
goto(0, -300)
goto(0, -250)
goto(-100, -250)
goto(-100, -300)
end_fill()                    # fond blanc (bas)

# triangle jaune (haut gauche)
fillcolor("yellow")
begin_fill()
position(-100, -200)          # coin haut gauche
goto(-50, -225)               # sommet du triangle
goto(-100, -250)              # coin bas gauche
goto(-100, -200)
end_fill()                    # triangle jaune terminé

# triangle bleu (centre)
fillcolor("cornflowerblue")
begin_fill()
position(-100, -250)          # base gauche
goto(-50, -275)               # bas du triangle
goto(-50, -225)               # haut du triangle
goto(-100, -250)
end_fill()                    # triangle bleu terminé

# triangle blanc (à droite du jaune)
fillcolor("white")
begin_fill()
position(-50, -225)           # sommet gauche du triangle blanc
goto(0, -250)                 # pointe vers la droite
goto(-50, -275)               # base du triangle
goto(-50, -225)
end_fill()                    # triangle blanc terminé

# Petite correction pour combler un espace rose en bas à gauche
position(-100,-300)
fillcolor("pink")
begin_fill()
goto(-50, -275)
goto(-100, -250)
goto(-100,-300)
end_fill()


# Figure de 5 arcs de cercles de plus en plus petits

position(-100,-150)  # place la tortue pour tracer la moitié supérieure du carré
setheading(90)       # oriente la tortue vers le haut
fillcolor("pink")    # définit la couleur de remplissage rose
begin_fill()         # commence le remplissage
for i in range(2):   # trace un rectangle (moitié du carré)
    forward(50)
    left(90)
    forward(100)
    left(90)
end_fill()            # termine le remplissage rose

fillcolor("lavender") # couleur du fond de l’autre moitié
position(-100,-200)   # descend d’une moitié de carré
setheading(90)        # oriente vers le haut
begin_fill()          # commence le remplissage
for i in range(2):    # même principe que plus haut
    forward(50)
    left(90)
    forward(100)
    left(90)
end_fill()            # fond lavender terminé

position(-100,-100)   # position pour le premier arc (haut)
fillcolor("cornflowerblue")
begin_fill()
circle(50,-180)       # grand arc bleu (demi-cercle)
end_fill()

position(-125,-100)   # se déplace pour le 2ᵉ arc, plus petit
setheading(90)
fillcolor("lavender")
begin_fill()
circle(25,-180)       # arc lavender (demi-cercle plus petit)
end_fill()

position(-100,-150)   # passe dans la partie inférieure du carré
setheading(90)
fillcolor("white")
begin_fill()
circle(50,-180)       # grand arc blanc (même taille que le premier)
end_fill()

position(-112.5,-150) # position ajustée pour arc moyen
setheading(90)
fillcolor("yellow")
begin_fill()
circle(37.5,-180)     # arc jaune, taille moyenne
end_fill()

position(-128,-150)   # position du plus petit arc
setheading(90)
fillcolor("cornflowerblue")
begin_fill()
circle(22,-180)       # petit arc bleu (dernier)
end_fill()

# Figure d'un grand arc de cercle puis collés à lui 2 1/4 de cercle (figure en haut à droite)

position(-100,0)           # place la tortue pour commencer la figure (en haut à droite)
fillcolor("lavender")      # couleur du fond du carré
begin_fill()
carre(100)                 # dessine le carré d’arrière-plan
end_fill()

position(-50,0)            # se place au centre du carré
fillcolor("yellow")
begin_fill()
setheading(-180)           # oriente la tortue vers la gauche
circle(50,180)             # trace un grand demi-cercle jaune
end_fill()

position(0,0)              # se place à droite du grand arc
fillcolor("white")
begin_fill()
left(180)                  # inverse la direction pour tracer le quart de cercle
circle(50,90)              # trace un quart de cercle blanc
left(90)                   # tourne pour refermer la forme
forward(50)                # ferme la zone de remplissage
right(90)
forward(50)
end_fill()

position(0,-50)            # se place pour le deuxième quart de cercle
setheading(0)              # orientation vers la droite
fillcolor("white")
begin_fill()
left(180)                  # tourne vers la gauche pour tracer le 2e quart
circle(50,90)              # trace un quart de cercle blanc (bas)
left(90)
forward(50)                # referme la forme
right(90)
forward(50)
end_fill()

position(-50,-100)         # revient à la base du grand arc
setheading(90)             # oriente vers le haut
forward(100)               # trace une ligne noire verticale pour fermer la forme





#Paul JULLIARD 1er4 (début le 17/10/2025 fin le 01/11/2025)
#On a crée une fonction position pour placer la tortue sur des coordonnées (x,y)
#On a crée une fontion pour le motif carré et triangle
#On a crée une fonction par figure (J'ai mis paul_figureNB et numéroté du coin en haut à gauche puis par ligne)


def position (x,y):
    """Mettre la turtle dans la position voulue sans laisser de trace visible sur le schéma"""
    up() #lever le stylo
    goto(x,y) #aller aux coordonnées voulues
    down() #baisser le stylo

def carre (longueur):
    """fonction qui trace un carré"""
    for i in range(4): #répéter 4 fois
        forward (longueur) #avancer de la longueur voulue, uitle pour les fonctions d'après
        left(90) #tourner de 90°

def triangle (longueur,x,y,c):
    """fonction qui trace un triangle avec les coordonnées souhaitées"""
    position(x,y) #fait appel à la fonction position
    color(c) #Permet de choisir la couleur voulue (définie avec le paramètre "c")
    for i in range(2): #répéter 2 fois
        left(90) #tourner de 90°
        forward (longueur) #avancer de la longueur voulue, uitle pour les fonctions d'après
    left(45)
    goto (x,y)

#***************************************************************************
#Test des motifs triangle et carré
#***************************************************************************
#triangle(100,10,10,"pink")
#carre(100)

#***************************************************************************
#Code des 16 figures
#***************************************************************************

#J'ai effectué tout mes calcul à l'aide de géogébra afin d'obtenir les valeurs les plus précises possibles
#Aprés avoir fait des mesures, j'ai dessiné toutes mes figures à la main pour mieux visualiser (voir dans mon dossier)
#Chaque figure est un carre de taille 2*lx2*l (Cf commentaire ligne 468), on considère le référenciel en bas à gauche du carré,
#chaque figure est une fonction qui prend en entrée 3 paramètres: longueur du carré, positions du coin en bas à gauche
#Dans plusieurs figures, les motifs intérieurs sont situés à l'intérieur d'un carré plus petit non tracé. Dans certaines fonctions on code ce carré pour mieux placer ces motifs. Ce carré est toujours appelé "carre_int"
#le code de chaque figure commence par se positionner en (0,0); puis trace le contour du carré
#La logique est toujours la même : si un motif se répète, je fais une boucle selon la direction (horizontale/ verticale)
#Je remets régulièrement l'angle du crayon à 0° avec la commande setheading pour simplifier les tracés
#J'ai codé les figures 11, 15 et 16 en premier. Au début elles étaient codés en dur mais à partir de la figure 9 je l'ai ait toutes mises en relatives
#Les premières figures que j'ai codé été moins bien faite, à force de coder il s'améliore
#Je vais expliquer en détail les figures 1 et 2, des commentaires spécifiques seront fait sur les autres

def paul_figure1 (longueur,position_x,position_y):
    """6 arcs de cercle à l'intérieur d'un carré"""
    position(position_x,position_y) #Fait appel à la fonction ci-dessus. Permet de choisir la position de départ de la figure avec les valeurs mises en entrée
    fillcolor("Lavender") #Tous les prochains remplissages seront de couleur lavender (=lavande)
    begin_fill() #début du remplissage de couleur du carré
    carre (longueur) #fait appel à la fonction ci-dessus, trace un carré de côté de la valeur de "longueur" saisie en entrée
    end_fill() #fin du remplissage du carré
    carre_int = 1.25/1.8*longueur #Dimensionne un carré intérieur imaginaire qui délimite les petites figures
    r = 0.3/1.8*longueur #Défini le rayon des demi-cercles proportionnelement aux mesures effectuées sur géogébra
    espace_x = (carre_int-3*r)/2 #Espace entre les demi-cercles horizontal (calcul : (longueur total du carré intérieur - les trois rayons des demi-cercles)/nombre d'espaces espaces)
    espace_y = (carre_int-4*r) #Espace entre les demi-cercles horizontal (calcul : (longueur total du carré intérieur - les trois rayons des demi-cercles)/nombre espace(-ici il y a seulement 1 espace))
    for i in range(3): #triple bouble (i=0 puis i=1 puis i=2). Ici il y a 3 colonnes
      for j in range (2): #double boucle (i=0 puis i=1). Il y a deux motifs (demi-cercles) par colonne
        fillcolor("pink")#Tous les prochains remplissages seront de couleur rose
        position(position_x+(longueur-carre_int)/2+(i+1)*r+espace_x*i,position_y+(longueur-carre_int)/2+j*(2*r+espace_y)) #Position du point de départ en bas du demi-cecle
        setheading(0) #remet l'angle du crayon à 0°
        begin_fill() #début du remplissage de couleur des demi-cercles
        circle(r,-180) #Trace un demi-cercle de rayon defini ligne 41
        end_fill()#fin du remplissage des demi-cercles
        goto(position_x+(longueur-carre_int)/2+(i+1)*r+espace_x*i,position_y+(longueur-carre_int)/2+j*(2*r+espace_y))#Revient en bas de chaque demi-cercles pour finir des les compléter

def paul_figure2 (longueur,position_x,position_y):
    """16 petits cercle jaunes dans un carré bleu"""
    position(position_x,position_y) #Fait appel à la fonction ci-dessus. Permet de choisir la position de départ de la figure avec les valeurs mises en entrée
    fillcolor("cornflowerblue") #Tous les prochains remplissage seront de couleur cornfolwer (=bleuet)
    begin_fill() #début du remplissage de couleur de la figure
    carre (longueur) #fait appel à la fonction précédente, trace un carré de côté de la valeur de "longueur" saisie en entrée
    end_fill() #fin du remplissage de la figure
    position(position_x+longueur*0.15,position_y+longueur*0.15) #déplacement du stylo pour se mettre sur la position du premier rond, en haut à gauche
    carre_int=longueur-longueur*0.30 #Dimensionne un carré intérieur imaginaire qui délimite les petites figures
    for i in range(4): #Motifs (cercles) recopié 4 fois sur la première colonne
      r=(0.5/6.79)*longueur #valeur du rayon des 16 cercles en fonction de la longueur. J'ai calculé les valeur à l'aide de géogébra
      esp = carre_int - 8*r
      position(position_x+longueur*0.15+r+ i*(esp+r),position_y+longueur*0.15) #La tortue avance sans laisser de trace jusqu'au prochain rond. La tortue avance de deux rayons + l'espace entre chaque cercle multiplié par le nombre de cercle avant
      fillcolor("yellow")
      begin_fill() #début du remplissage de couleur de la figure
      circle(r) #trace un cercle complet (360°) avec pour rayon la valeur de "r" définit précédemment
      end_fill() #fin du remplissage de la figure
      for j in range (3): #La colonne initiale est recopié sur les 3 autres colonnes
        position(position_x+longueur*0.15+r+ i*(esp+r),position_y+longueur*0.15+r+esp+ j*(esp+r))
        begin_fill() #début du remplissage de couleur de la figure
        circle(r) #trace un cercle complet (360°) avec pour rayon la valeur de "r" définit précédemment
        end_fill() #fin du remplissage de la figure

def paul_figure3 (longueur,position_x,position_y):
  """trace un losange dans un carré"""
  pos_car=0.55/1.75*longueur #position du début de tracé du petit carré (sur la diagonale)
  position(position_x,position_y)
  carre (longueur)
  fillcolor("pink")
  begin_fill()
  #Trace le quart de carré gauche point à point et le remplit en rose
  goto(position_x+longueur/2,position_y+longueur/2)
  goto(position_x,position_y+longueur)
  #fin du tracé du quart de carré
  end_fill()
  #quart de carré haut
  position(position_x+longueur/2,position_y+longueur/2)
  goto(position_x+longueur,position_y+longueur)
  #fin du tracé du quart de carré
  #quart de carré droite
  position(position_x+longueur/2,position_y+longueur/2)
  goto(position_x+longueur,position_y)
  #fin du tracé du quart de carré
  fillcolor("Lavender")
  begin_fill()
  #quart de carré bas remplit couleur lavande
  goto(position_x+longueur/2,position_y+longueur/2)
  goto(position_x,position_y)
  #fin du tracé du quart de carré
  end_fill()
  position(position_x+pos_car,position_y+pos_car) #position de départ (sur la diagonal) du premier des quatres carrés qui forment le losange
  long_car = 0.475/1.8*longueur #longueur des côtés des petits carrés avec rapport de proportionalité
  setheading(45)
  fillcolor("CornFlowerBlue")
  begin_fill()
  carre(long_car) #Tracé du petit carré de gauche
  end_fill()
  setheading(-45)
  fillcolor("pink")
  begin_fill()
  carre(long_car) #Tracé du petit carré du bas
  end_fill()
  position(position_x+longueur-pos_car,position_y+longueur-pos_car)#position de départ du carré du haut
  setheading(135)
  fillcolor("Lavender")
  begin_fill()
  carre(long_car)#Tracé du petit carré du haut
  end_fill()
  setheading(-135)
  fillcolor("pink")
  begin_fill()
  carre(long_car)#Tracé du petit carré à droite
  end_fill()


def paul_figure9 (longueur,position_init_x, position_init_y):
    position(position_init_x,position_init_y)
    fillcolor("pink")
    for i in range(2): #double boucle
      position(position_init_x+i*longueur,position_init_y) #Décalage sur l'axe des abscisses (x) de longueur à chaque itération de i
      for j in range(2): #double boucle (j=0 puis j=1)
        setheading(0) #remet l'angle du crayon à 0°
        begin_fill() #début du remplissage de couleur de la figure
        circle(longueur,-90) #Trace un quart de cercle de rayon longueur. (Le - devant le 90 permet de changer le sens dans lequel le cercle est tracé)
        left(90) #Le crayon tourne de 90° à gauche
        triangle (longueur, position_init_x+i*longueur,position_init_y+j*longueur,"pink")#Décalage sur l'axe des ordonnées (y) de longueur à chaque itération de j. Fait appel à la fonction triangle définie ci-dessus et permet de pourvoir remplir les quarts de cercle
        end_fill()#fin du remplissage de la figure
        color("black") #couleur de remplissage = noire
        left(225)#Le crayon tourne de 225° à gauche
        carre(longueur)#Fait appel à la fonction carré définie plus haut. Le côté du carré = longueur
        forward(longueur) #avance tout droit de la valeur de longueur
    up() #J'ai fait un "up" pour éviter de laisser des traces de marquages

def paul_figure4 (longueur,position_init_x,position_init_y):
  """trace un triangle sur un demi-cercle"""
  position(position_init_x,position_init_y)
  fillcolor("lavender")
  begin_fill()
  carre(longueur)
  end_fill()
  fillcolor("cornflowerblue")
  begin_fill()
  forward(longueur)
  left(90)
  circle(longueur/2,180)#trace un demi-cercle, dont la valeur du rayon est égal à la moitié de la longueur du carré (ainsi 2*r = d et donc le diamètre du cercle est bien égal à la valeur de la longueur du carré)
  end_fill()
  fillcolor("white")
  position(position_init_x,position_init_y+longueur/2) #La tortue se déplace en (0,longueur/2)
  begin_fill()
  setheading(0) #remet l'angle du crayon à 0° et me permet de mieux me réperer
  forward(longueur)
  goto(position_init_x+longueur/2,position_init_y+longueur)# Tracé du sommet du triangle de coordonnées (longueur/2,longueur) et complète ainsi le triangle blanc
  end_fill()

def paul_figure6 (longueur,position_init_x, position_init_y): #Dans cette figure j'ai voulu testé une proportionalité mais c'était une mauvaise idée (c'est pour cela qu'il y a des *10 partout dans  cette fonction)
    """trace la sixième figure du quart inférieur droit : un cercle dans un cercle dans un carré"""
    position(position_init_x,position_init_y)
    setheading(0)
    fillcolor("pink")
    begin_fill()
    carre(10*longueur)
    end_fill()
    position(position_init_x+5*longueur,position_init_y) #position de départ pour tracer le grand cercle
    fillcolor("cornflowerblue") #couleur de remplissage = cornflowerblue("bleuet" en français)
    begin_fill()
    circle(10*longueur/2,360) #trace un cercle, dont le rayon est la moitié de la longueur du carré
    end_fill()
    position (position_init_x+5*longueur,position_init_y+2*longueur) #position de départ du petit cercle calculé à l'aide de géogebra
    fillcolor("LightSkyBlue")
    begin_fill()#début du remplissage de couleur du petit cercle
    circle (longueur*3,360) #Trace un cercle de rayon trois fois plus grands que la valeur de longueur (à cause de la proportionalité)
    end_fill()#fin du remplissage du second cercle


def paul_figure5 (longueur,position_init_x, position_init_y):
    """trace un carre fond bleue, avec 5 points blancs à l'intérieur"""
    position(position_init_x,position_init_y)
    fillcolor("cornflowerblue")
    begin_fill()
    carre(longueur)
    end_fill()
    r=(0.4/1.75)*longueur*0.5 #Je definis la longueur du rayon des 5 cercles (valeur précise trouvée avec geogebra)
    position(position_init_x+longueur/2,position_init_y+longueur/2-r) #position de départ pour tracer le premier cercle (J'enlève un rayon car la fonction cercle démarre en bas du cercle afin de bien le centrer)
    fillcolor("white")
    begin_fill()
    circle(r) #trace un cercle complet (360°), la valeur du rayon est définie plus haut
    end_fill()
    esp=0.8/1.8*longueur #esp représente l'espace entre deux cercle et peut s'adapter à la taille de la figure
    for j in range(2): # La variable 'i' représente le nombre de cercle par ligne. Ici il y a deux cercles par ligne
      for i in range(2): #La variable 'j' représente le nombre de cercle par colonne. Idem il y a 2 cercles par colonne
        position(position_init_x+0.48/1.75*longueur+i*esp,position_init_y+0.48/1.75*longueur+j*esp-r) #position de départ pour tracer les 4 autres cercle, calculé à l'aide de geogebra. Ici on mutliplie le nombre
        begin_fill()
        circle(r) #trace un cercle complet de rayon r (défini au dessus)
        end_fill()

def paul_figure8 (longueur,position_init_x,position_init_y):
  position(position_init_x,position_init_y)
  fillcolor("cornflowerblue")
  begin_fill()
  carre(longueur)
  end_fill()
  fillcolor("LightSkyBlue")
  begin_fill()
  right(90)
  circle(longueur/2,-180) #Tracé du grand demi-cercle en bas
  position(position_init_x+0.8*longueur,position_init_y) #Position de départ du plus petit cercle en bas
  circle(longueur/2*0.6,180) #Tracé du petit demi-cercle en bas
  end_fill()
  position(position_init_x+longueur,position_init_y+longueur) #Position de départ du grand cercle en haut
  setheading(90)
  begin_fill()
  circle(longueur/2,-180) #Tracé du grand demi-cercle en haut
  position(position_init_x+0.2*longueur,position_init_y+longueur) #Position de départ du plus petit cercle en haut
  circle(longueur/2*0.6,180) #Tracé du petit demi-cercle en haut
  end_fill()

def paul_figure15 (longueur,position_x,position_y):
  position(position_x,position_y)
  fillcolor("pink")
  begin_fill()
  carre(longueur)
  end_fill()
  fillcolor("LightSlateBlue")
  position(position_x+longueur*0.2,position_y+longueur*0.2) #Position de départ du plus grand carré intérieur
  begin_fill()
  carre(longueur*0.6) #Tracé du grand carré intérieur
  end_fill()
  fillcolor("pink")
  position(position_x+longueur*0.3,position_y+longueur*0.3) #Position de départ du plus petit carré intérieur
  begin_fill()
  carre(longueur*0.4) #tracé du petit carré intérieur
  end_fill()


def paul_figure16 (longueur,position_x,position_y):
  position(position_x,position_y)
  fillcolor("yellow") #couleur de remplissage = jaune
  begin_fill()
  carre(longueur)
  end_fill()
  position(position_x,position_y+longueur/2)#La turtle se positionne en (0,50)
  fillcolor("pink") #couleur de remplissage = rose
  begin_fill()
  forward(longueur)#trace la ligne du milieur du carré
  left(90)
  circle(longueur/2,-180)#trace un demi-cercle, du rayon de la moitié de la valeur de "longueur" (ainsi 2*r = d et donc le diamètre du cercle est bien égal à la valeur de la longueur)
  end_fill()


def paul_figure13 (longueur,position_x,position_y):
  position(position_x,position_y)
  fillcolor("cornflowerblue")
  begin_fill()
  carre(longueur)
  end_fill()
  position(position_x+longueur/2,position_y+longueur/8) #position de départ pour tracer le triangle (point en bas)
  fillcolor("pink")
  begin_fill()
  left(60)
  forward (longueur/2+longueur/4) #coté droit du trianle
  up() #lever le stylo
  goto(position_x+longueur/2,position_y+longueur/8) #revient au point en bas pour tracer le deuxieme coté du triangle
  down() #baisser le stylo
  left(60)
  forward (longueur/2+longueur/4) #coté gauche du trianle
  right(120)
  forward (longueur/2+longueur/4) #relie les deux points en haut du triangle
  end_fill()


def paul_figure11 (longueur,position_x,position_y):
    """Trace la onzième figue du carré inférieur droit : un petit carré dans un carré qui se relient avec une diagonale"""
    position(position_x,position_y)
    carre (longueur)
    fillcolor("cornflowerblue")
    begin_fill()
    forward (longueur*(5/11)) #La tortue se déplace sur la position de départ du petit carré
    carre(longueur*(6/11)) #Trace le petit carré de couleur conrflowerblue (=bleuet)
    end_fill()
    fillcolor("LightSkyBlue")
    left(90)
    begin_fill()
    forward(longueur*(6/11)) #La tortue se place en haut à gauche du carré, au point de départ du trait diagonal
    left(45) #s'oriente dans la bonne direction pour tracer le trait diagonal
    goto(position_x,position_y+longueur) #Trace le trait diagonal jusqu'en haut à droite du carré
    left(45)
    goto(position_x,position_y) #se déplace au début pour terminer le remplissage
    end_fill()


def paul_figure12 (longueur,position_x,position_y):
    """Trace deux ronds au-dessus de 4 diagonales"""
    position(position_x,position_y)
    carre (longueur)
    for i in range (2):
      position(position_x+i*longueur/2,position_y+longueur*1/2) #position de départ du petit carré en haut à gauche quand i = 0 et celui de droite quand i =1
      if i == 0:
        fillcolor("LightSkyBlue") #Le premier carré (quand i = 0) sera rempli en bleu ciel très clair
      else :
        fillcolor("pink") #Les autres carrés (quand i != 0) seront remplis en rose(il n'y a qu'un seul autre carré dans cette figure)
      begin_fill()
      carre (longueur*1/2) #construction des carrés
      end_fill()
      position(position_x+longueur*1/4+i*longueur/2,position_y+longueur*5/8)
      if i == 1:
        fillcolor("LightSkyBlue") #Le second cercle sera rempli de couleur bleu ciel très clair
      else :
        fillcolor("white") #L'autre cercle sera blanc
      begin_fill()
      circle(longueur/7)#tracé des cercles
      end_fill()
    fillcolor("pink")
    for i in range (4): #Il y a quatre diagonales
      setheading(0)
      if i < 3: #ce premier if détermine la position de départ
        position(position_x+i*longueur*2.8/8,position_y) #les 3 premieres diagonales partent du bas
      else:
        position(position_x,position_y+longueur*3/8) #la dernière diagonal commence plus haut que les autres (C'est la bande la plus à gauche sur le dessin)
      begin_fill()
      left(45) #oriente les diagonales
      if i < 2: # ce deuxième if trace une diagonale
        forward(longueur*(8.5/12)) #Tracé des deux grandes diagonales
      elif i==3:
        forward(longueur*(0.18)) #Cas de la diagonal à gauche
      else:
        forward(longueur*(0.42)) #cas de la diagonal à droite
      if i ==2: #ce 3 if trace la petite distance horizontale pour les 3 bandes à gauche, verticale pour la plus a droite, i==2 cas le plus à droite
        right(135) #vertical
        forward(longueur*(1/7))
        left(90)
      else:# pour les autres
        right(45) #horitontale
        forward(longueur*(1/7))
      right(135) # on oriente pour redesecendre en parallèle de la montée
      if i<2: #pour les 2 premières bandes
        forward(longueur*(7.8/11))
      elif i==3: #la plus a gauche
        forward(longueur*(0.4))
      else: #la plus a droite
        forward(longueur*(0.21))
      if i < 2: # déplacement sur la position suivante
        goto(position_x+i*longueur*2.8/8,position_y)
      end_fill()


def paul_figure10 (longueur,position_x,position_y):
    position(position_x,position_y)
    carre (longueur)
    fillcolor("LightSkyBlue")
    begin_fill()
    for i in range(2):
      forward (longueur/2)
      left(90)
      forward (longueur)
      left(90)
    end_fill()
    position(position_x+longueur*0.5,position_y) #position de départ du triangle
    fillcolor("yellow")
    #début du tracé du triangle et du remplissage
    begin_fill()
    left(90)
    forward (longueur)
    left(135)
    forward (longueur*0.71)
    left(90)
    forward (longueur*0.71)
    end_fill()
    #fin du tracé du triangle et du remplissage
    for i in range(2): #double bouble car il y a deux cercles sur la colonne
      position(position_x+longueur*(0.68),position_y+longueur*(0.6)-i*longueur*0.4) #Position de départs des deux cercles
      begin_fill()
      circle(longueur/8) #tracé des cercles (rayon = longueur du carré/8 mesuré grâce à géogebra)
      end_fill()


def paul_figure7 (longueur,position_init_x,position_init_y):
  position(position_init_x,position_init_y)
  fillcolor("yellow")
  begin_fill()
  carre(longueur)
  end_fill()
  position(position_init_x,position_init_y)#La tortue revient à la position de départ de la figure
  setheading(0)
  fillcolor("white")
  for i in range(3): #triple boucle car il y a trois triangle par ligne
    #J'ai fais cette figure dans les premières, ce code est assez long et peut être améliorer
    if i <=1: # if est une instruction conditionnelle. Ici si i est inférieur ou égal à 1 (donc i=0 ou i=1) alors on effectue le code si-dessous. Trace les deux premiers triangles
      begin_fill()
      forward(longueur/3+longueur/3*i) #Avance de la longueur totale divisée par 3 car il y a trois triangles. On rajoute une nouvelle longueur divisée par 3 pour tracer le second triangle
      goto(position_init_x+longueur/6+i*longueur/3,position_init_y+longueur/2) #trace les sommets des deux premiers triangles
      goto(position_init_x+longueur/3*i,position_init_y)
      end_fill()
    else: # Instruction conditionelle. Le code s'effectuera si i est strictement supérieur à 1. Trace le troisième triangle
      begin_fill()
      goto(position_init_x+longueur,position_init_y)
      goto(position_init_x+longueur/6+i*longueur/3,position_init_y+longueur/2)
      goto(position_init_x+longueur*2/3,position_init_y)
      end_fill()
  position(position_init_x,position_init_y+longueur/2)
  setheading(0)
  fillcolor("lavender")
  for i in range(2): #cette boucle trace le rectangle du haut et permet ainsi de pourvoir remplir ce rectangle de la couleur voulue (lavender ici)
    begin_fill()
    forward(longueur)
    left(90)
    forward(longueur/2)
    left(90)
    end_fill()
  fillcolor("pink") #couleur de remplissage = rose
  position(position_init_x,position_init_y+longueur/2) #la tortue se positionne en (0,50) pour pouvoir tracer la 2eme ligne de triangle
  setheading(0)
  for i in range (3): #Exactement le même code pour la ligne du haut
    if i <=1:
      begin_fill()
      forward(longueur/3+longueur/3*i)
      goto(position_init_x+longueur/6+i*longueur/3,position_init_y+longueur)
      goto(position_init_x+longueur/3*i,position_init_y+longueur/2)
      end_fill()
    else:
      begin_fill()
      goto(position_init_x+longueur,position_init_y+longueur/2)
      goto(position_init_x+longueur/6+i*longueur/3,position_init_y+longueur)
      goto(position_init_x+longueur*2/3,position_init_y+longueur/2)
      end_fill()


def paul_figure14(longueur,position_x,position_y):
  position(position_x,position_y)
  carre(longueur)
  nb_tri=3 #Il y a trois lignes de triangle
  base = longueur/nb_tri #la base d'un triangle est égal à la longueur totale divisée par le nombre de triangle (il y a 3 triangles ici)
  for i in range (nb_tri): #on boucle sur le nombre de ligne de trangle
    position(position_x,position_y+i*base) #on construit point à point la ligne de triangles à partir de leur coordonnées dans le carré
    fillcolor("Lavender")
    begin_fill() #construction du premier demi triangle coloré
    goto(position_x,position_y+(i+1)*base)
    goto(position_x+base/2,position_y+(i+1)*base)
    goto(position_x,position_y+i*base)
    end_fill()
    goto(position_x+base,position_y+i*base)#construction du premier triangle blanc
    goto(position_x+base/2,position_y+(i+1)*base)
    begin_fill()#construction du second triangle coloré
    goto(position_x+base+base/2,position_y+(i+1)*base)
    goto(position_x+base,position_y+i*base)
    end_fill()
    goto(position_x+2*base,position_y+i*base)#construction du second triangle blanc
    goto(position_x+base+base/2,position_y+(i+1)*base)
    begin_fill()#construction du troisieme triangle coloré
    goto(position_x+2*base+base/2,position_y+(i+1)*base)
    goto(position_x+2*base,position_y+i*base)
    end_fill()
    goto(position_x+longueur,position_y+i*base)#construction du troisième triangle blanc
    goto(position_x+longueur-base/2,position_y+(i+1)*base)
    begin_fill()#construction du quatrieme demi triangle coloré
    goto(position_x+longueur,position_y+(i+1)*base)
    goto(position_x+longueur,position_y+i*base)
    end_fill()

speed(60)

p_x=50 #Position en x (abscisses) de la figure 9 (première figure que j'ai faite)
p_y=-300 #Position en y (ordonnées) de la figure 9
l=50 #Chaque figure est un carré de 100 sur 100. l représente la moitié de cette longueur
#toutes les figures (autre que 9) sont placées relativement à la figure 9 et a longueur l

#Modifier la valeur de p_x revient à déplacer l'entiereté des figures sur l'axe des abscisses
#Modifier la valeur de p_y revient à déplacer l'entiereté des figures sur l'axe des ordonnées
#Modifier la valeur de l revient à modifier l'espacement entre les figures


#***************************************************************************
#Tests des fonctions
#***************************************************************************
setheading(0)
paul_figure1(100,p_x-l,p_y+4*l)
setheading(0)
paul_figure2(100,p_x+l,p_y+4*l)
setheading(0)
paul_figure3(100,p_x+3*l,p_y+4*l)
setheading(0)
paul_figure4(100,p_x+5*l,p_y+4*l)
setheading(0)
paul_figure5(100,p_x-l,p_y+2*l)
setheading(0)
paul_figure6(10,p_x+l,p_y+2*l)
setheading(0)
paul_figure7(100,p_x+3*l,p_y+2*l)
setheading(0)
paul_figure9(50,p_x,p_y)
setheading(0)
paul_figure15 (100,p_x+3*l,p_y-2*l)
setheading(0)
paul_figure16 (100,p_x+5*l,p_y-2*l)
setheading(0)
paul_figure10(100,p_x+l,p_y)
setheading(0)
paul_figure13 (100,p_x-l,p_y-2*l)
setheading(0)
paul_figure11(100,p_x+3*l,p_y)
setheading(0)
paul_figure12 (100,p_x+5*l,p_y)
setheading(0)
paul_figure8(100,p_x+5*l,p_y+2*l)
setheading(0)
paul_figure14(100,p_x+l,p_y-2*l)









#Gomez-Roca Santiago 1ère6
# Configuration initiale de la fenêtre Turtle
from turtle import*
speed(15)# Vitesse maximale de dessin
width(1.1)# Épaisseur du trait
setup(800,800)# Taille de la fenêtre graphique

#  Fonction pour dessiner un carré de côté donné
def carre(longueur):
    for i in range(4):
        forward(longueur)
        right(90)

#  Fonction pour déplacer la tortue sans dessiner(Santiago)
def position(x,y):
    up()
    goto(x,y)
    down()

#  Fonction pour dessiner une case de 100x100 à une position donnée(Santiago)
def carreau(x,y):
    position(x,y)
    setheading(0)
    carre(100)

#  Fonction pour commencer à remplir une forme avec une couleur(Santiago)
def remplir(couleur):
    fillcolor(couleur)
    begin_fill()

#  FIGURES DE LA LIGNE 8
#figureA8
def A_Huit():
    #premier demi-cercle
    carreau(-400,400)
    remplir('cornflowerblue')
    circle(-50,180)
    right(90)
    forward(25)
    right(90)
    circle(25,180)
    end_fill()
    #deuxième demi-cercle
    position(-300,400)
    remplir('lavender')
    circle(50,180)
    right(90)
    forward(-25)
    right(90)
    circle(-25,180)
    end_fill()
A_Huit()

#figueB8
def B_Huit():
    #ajoute un fond rose
    remplir('pink')
    carreau(-300,400)
    end_fill()
    remplir('yellow')
    forward(50)
    #crée 3 petits demi-cercles
    for i in range(3):
        circle(-100/6,180)
        setheading(0)
    left(180)
    forward(50)
    right(90)
    forward(100)
    end_fill()

B_Huit()

#figureC8
def C_Huit():
    carreau(-200,400)
    remplir('lavender')
    #fait un rectangle bleu clair
    for i in range(2):
        forward(100)
        right(90)
        forward(50)
        right(90)
    end_fill()
    position(-200,350)
    forward(100)
    #crée un cercle rose
    position(-150,315)
    remplir('pink')
    circle(35,-360)
    end_fill()
    #ajoute un demi-cercle bleu par dessus le rose
    position(-115,350)
    setheading(90)
    remplir('cornflowerblue')
    circle(35,-180)
    end_fill()
    #permet de tracer le trait qui sépare le rose et le bleu
    position(-200,350)
    setheading(0)
    forward(100)

C_Huit()

#figureD8
def D_Huit():
    #fait un fond bleu
    remplir('cornflowerblue')
    carreau(-100,400)
    end_fill()
    #crée le premier triangle
    remplir('lavender')
    goto(0,350)
    goto(-100,300)
    end_fill()
    left(90)
    forward(25)
    #crée le deuxième petit triangle
    remplir('pink')
    goto(-50,350)
    goto(-100,375)
    end_fill()
    #ajoute un trait qui sépare deux figures
    position(-100,300)
    forward(100)

D_Huit()

#  FIGURES DE LA LIGNE 7
#figureA7
def A_Sept():
    #fait un fond jaune
    remplir('yellow')
    carreau(-400,300)
    end_fill()
    forward(50)
    right(45)
#dessine deux carrés, l'un dans l'autre
    remplir('pink')
    carre(50*(2**(1/2)))#valeur calculée avec Pythagore
    end_fill()
    position(-350,275)
    remplir('cornflowerblue')
    carre(25*(2**(1/2)))#valeur calculée avec Pythagore
    end_fill()

A_Sept()

#figureB7
def B_Sept():
    carreau(-300,300)
    # Petits carrés jaunes
    forward(25)
    right(45)
    remplir('yellow')
    carre(25*(2**(1/2)))
    end_fill()
    position(-225,300)
    remplir('yellow')
    carre(25*(2**(1/2)))
    end_fill()
    position(-275,250)
    remplir('yellow')
    carre(25*(2**(1/2)))
    end_fill()
    position(-225,250)
    remplir('yellow')
    carre(25*(2**(1/2)))
    end_fill()
    # Petits cercles bleus
    position(-275,267)
    setheading(0)
    remplir('lavender')
    circle(7,-360)
    end_fill()
    position(-225,267)
    remplir('lavender')
    circle(7,-360)
    end_fill()
    position(-275,218)
    remplir('lavender')
    circle(7,-360)
    end_fill()
    position(-225,218)
    remplir('lavender')
    circle(7,-360)
    end_fill()
    position(-250,245)
    remplir('lavender')
    circle(7,-360)
    end_fill()

B_Sept()

#figureC7
def C_Sept():
    #crée un fond rose
    remplir('pink')
    carreau(-200,300)
    end_fill()
    #trace un demi-disque
    remplir('beige')
    circle(-50,180)
    end_fill()
    #trace un deuxième demi-disque
    position(-100,300)
    remplir('beige')
    circle(50,180)
    end_fill()
    carreau(-200,300)

C_Sept()

#figureD7
#presque la même figure que la précédente
def D_Sept():
    remplir('pink')
    carreau(-100,300)
    end_fill()
    remplir('lavender')
    circle(-50,180)
    end_fill()
    position(0,300)
    remplir('lavender')
    circle(50,180)
    end_fill()
    carreau(-100,300)


D_Sept()

#figureA6
def A_Six():
    carreau(-400,200)
    setheading(180)
    #trace un quart de disque en haut à gauche
    position(-350,200)
    remplir('lavender')
    forward(50)
    left(90)
    forward(50)
    left(90)
    circle(50,90)
    end_fill()
    #trace un quart de disque en bas à gauche
    position(-350,100)
    setheading(180)
    remplir('lavender')
    forward(50)
    right(90)
    forward(50)
    right(90)
    circle(-50,90)
    end_fill()
    #trace un quart de disque en haut à droite
    position(-350,200)
    setheading(0)
    remplir('lavender')
    forward(50)
    right(90)
    forward(50)
    right(90)
    circle(-50,90)
    end_fill()
    #trace un quart de disque en bas à droite
    position(-350,100)
    setheading(0)
    remplir('lavender')
    forward(50)
    left(90)
    forward(50)
    right(90)
    circle(-50,-90)
    end_fill()

A_Six()


#figureB6
def B_Six():
    carreau(-300,200)
    x=-270
    y=185
    #trace les trois petits demi-cercles roses de la ligne du dessus en alternant de coordonnées
    for i in range(3):
        position(x,y)
        setheading(180)
        remplir('pink')
        circle(15,180)
        end_fill()
        goto(x,y)
        x+=25

    x=-270
    y=145
    #trace les trois petits demi-cercles roses de la ligne du dessous en alternant de coordonnées
    for i in range(3):
        position(x,y)
        setheading(180)
        remplir('pink')
        circle(15,180)
        end_fill()
        goto(x,y)
        x+=25


B_Six()

#figureC6
def C_Six():
    #peint un fond jaune
    remplir('yellow')
    carreau(-200,200)
    end_fill()
    #crée 3 cercles de même centre mais de rayons différents
    position(-150,115)
    setheading(0)
    remplir('cornflowerblue')
    circle(35,360)
    end_fill()
    position(-150,125)
    setheading(0)
    remplir('pink')
    circle(25,360)
    end_fill()
    position(-150,140)
    setheading(0)
    remplir('white')
    circle(10,360)
    end_fill()


C_Six()

#figureD6
def D_Six():
    carreau(-100,200)
    #trace les deux petits carrés du dessus
    for i in range(2):
        #le premier en bleu
        if i==0:
            remplir('cornflowerblue')
            carre(50)
            forward(50)
            end_fill()
        #le deuxième en jaune
        else:
            remplir('yellow')
            carre(50)
            forward(50)
            end_fill()
    x=-75
    y=160
    #trace les yeux roses du robot
    for i in range(2):
        position(x,y)
        setheading(0)
        remplir('pink')
        circle(15,360)
        end_fill()
        x+=50
    position(-100,150)
    #crée un rectangle en bas
    remplir('lavender')
    for i in range(2):
        forward(100)
        right(90)
        forward(50)
        right(90)
    end_fill()
    x=0
    y=100
    r=50
    #trace le premier arc de cercle
    for i in range(2):
        position(x,y)
        remplir('pink')
        setheading(90)
        circle(r,180)
        end_fill()
        x-=20
        r-=20
    #rajoute le demi-disque bleu
    position(-20,100)
    remplir('cornflowerblue')
    setheading(90)
    circle(30,180)
    right(90)
    forward(60)
    end_fill()
D_Six()

#figureA5
def A_Cinq():
    #fait un fond bleu
    remplir('cornflowerblue')
    carreau(-400,100)
    end_fill()
    #ajoute le carré jaune et le carré rose
    position(-400,100)
    remplir('yellow')
    carre(50)
    end_fill()
    position(-350,50)
    remplir('pink')
    carre(50)
    end_fill()
    left(135)
    #crée les carrés imbriqués
    position(-350,15)
    remplir('lavender')
    carre(50)
    end_fill()
    position(-350,35)
    remplir('pink')
    carre(20)
    end_fill()
A_Cinq()

#figureB5
def B_Cinq():
    #trace un quart de disque à chaque angle, chacun à une couleur différente
    carreau(-300,100)
    setheading(180)
    position(-250,100)
    remplir('lavender')
    forward(50)
    left(90)
    forward(50)
    left(90)
    circle(50,90)
    end_fill()
    position(-250,0)
    setheading(180)
    remplir('yellow')
    forward(50)
    right(90)
    forward(50)
    right(90)
    circle(-50,90)
    end_fill()
    position(-250,100)
    setheading(0)
    remplir('cornflowerblue')
    forward(50)
    right(90)
    forward(50)
    right(90)
    circle(-50,90)
    end_fill()
    position(-250,0)
    setheading(0)
    remplir('pink')
    forward(50)
    left(90)
    forward(50)
    right(90)
    circle(-50,-90)
    end_fill()
B_Cinq()

#figureC5
def C_Cinq():
    #fait un fond rose
    remplir('pink')
    carreau(-200,100)
    end_fill()
    forward(50)
    right(45)
    #crée deux carrés imbriqués
    remplir('cornflowerblue')
    carre(50*(2**(1/2)))
    end_fill()
    position(-150,75)
    remplir('white')
    carre(25*(2**(1/2)))
    end_fill()
C_Cinq()

#figureD5
def D_Cinq():
    carreau(-100,100)
    position(-100,0)
    setheading(45)
    remplir('lavender')
    #trace le premier triangle bleu clair
    for i in range(2):
        forward((20000**(1/2))/2)#valeur calculée grâce à Pythagore
        right(90)
    setheading(180)
    forward(50)
    end_fill()
    #trace le deuxième triangle rose
    position(-50,50)
    setheading(45)
    remplir('pink')
    forward((20000**(1/2))/2)#valeur calculée grâce à Pythagore
    setheading(-90)
    forward(100)
    right(135)
    forward((20000**(1/2))/2)#valeur calculée grâce à Pythagore
    end_fill()

D_Cinq()



# Giraud Patino Jacques 1°4
# Programme Turtle : création d’un motif graphique divisé en 16 cases colorées

from turtle import *   # importe les fonctions de dessin Turtle
from math import *     # importe les fonctions mathématiques (ici pour sqrt par exemple)

speed(999)             # vitesse maximale du dessin (plus rapide)
setup(800, 800)        # taille de la fenêtre graphique
width(1)             # épaisseur du trait

# ---------------------------------------------------------------
# FONCTION carre(n) : dessine un carré de côté n
# ---------------------------------------------------------------
def carre(n):
    for i in range(4):
        forward(n)
        left(90)

# ---------------------------------------------------------------
# FONCTION quadrillage() : dessine le cadre principal (400x400)
# et les lignes internes pour séparer les 16 cases (4x4)
# ---------------------------------------------------------------
def quadrillage():
    carre(400)  # carré principal
    # traits verticaux
    for i in range(3):
        position(100+100*i,0)
        setheading(90)
        forward(400)
    # traits horizontaux
    for i in range(3):
        position(0,100+100*i)
        setheading(0)
        forward(400)

# ---------------------------------------------------------------
# FONCTION position(x,y) : déplace la tortue sans dessiner
# ---------------------------------------------------------------
def position(x,y):
    up()        # stylo levé
    goto(x,y)   # aller aux coordonnées (x,y)
    down()      # stylo abaissé

# ---------------------------------------------------------------
# FONCTION remplir(couleur) : commence un remplissage coloré
# ---------------------------------------------------------------
def remplir(couleur):
    fillcolor(couleur)
    begin_fill()

# ---------------------------------------------------------------
# FONCTION carreau(x,y) : trace une case de 100x100 à partir de (x,y)
# ---------------------------------------------------------------
def carreau(x,y):
    position(x,y)
    setheading(0)
    carre(100)

# ---------------------------------------------------------------
# FONCTION rayures(x,y,couleur_1,couleur_2)
# crée un motif rayé dans une case donnée
# ---------------------------------------------------------------
def rayures(x,y,couleur_1,couleur_2):
    # grande bande de fond
    position(x,y)
    remplir(couleur_2)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    end_fill()

    # plusieurs bandes diagonales de couleur_1
    position(x,y+50)
    remplir(couleur_1)
    goto(x,y+35)
    goto(x+15,y+50)
    end_fill()

    position(x,y+20)
    remplir(couleur_1)
    goto(x+30,y+50)
    position(x+50,y+50)
    goto(x,y)
    end_fill()

    position(x+15,y)
    remplir(couleur_1)
    goto(x+65,y+50)
    position(x+85,y+50)
    goto(x+35,y)
    end_fill()

    position(x+50,y)
    remplir(couleur_1)
    goto(x+100,y+50)
    position(x+100,y+30)
    goto(x+70,y)
    end_fill()

    position(x+85,y)
    remplir(couleur_1)
    goto(x+100,y+15)
    goto(x+100,y)
    end_fill()

# ---------------------------------------------------------------
# CASE 1
# ---------------------------------------------------------------
def un():  # première case
    carreau(0,0)
    # carré lavande incliné
    position(50,0)
    left(45)
    remplir('lavender')
    carre(50*(2**(1/2)))
    end_fill()
    # petit carré jaune
    position(25,50)
    right(90)
    remplir('yellow')
    carre(25*(2**(1/2)))
    end_fill()
un()

# ---------------------------------------------------------------
# CASE 2
# ---------------------------------------------------------------
def deux():  # deuxième case
    carreau(100,0)
    # sous-fonction pour dessiner un rectangle vertical
    def rectangle(n):
        setheading(0)
        remplir(n)
        forward(20)
        left(90)
        forward(50)
        left(90)
        forward(20)
        left(90)
        forward(50)
        left(90)
        end_fill()
    # alterne les couleurs pour créer un motif rayé vertical
    def suite_rectengles(couleur_1, couleur_2):
        for i in range(5):
            if i % 2 == 0:
                rectangle(couleur_1)
            else:
                rectangle(couleur_2)
            forward(20)
    suite_rectengles('yellow','lavender')
    position(100,50)
    suite_rectengles('lavender','yellow')
deux()

# ---------------------------------------------------------------
# CASE 3
# ---------------------------------------------------------------
def trois():  # troisième case
    carreau(200,0)
    # forme décorative jaune au centre
    position(230, 20)
    remplir('yellow')
    goto(250, 40)
    goto(270, 20)
    goto(280, 30)
    goto(260, 50)
    goto(280, 70)
    goto(270, 80)
    goto(250, 60)
    goto(230, 80)
    goto(220, 70)
    goto(240, 50)
    goto(220, 30)
    goto(230, 20)
    end_fill()
trois()

# ---------------------------------------------------------------
# CASE 4
# ---------------------------------------------------------------
def quatre():  # quatrième case
    remplir('pink')   # fond rose
    carreau(300,0)
    end_fill()
    # sous-fonction pour créer un motif en zigzag
    def zigzag(n, z):
        goto(n, 100 / 6)
        goto(z, 100 / 6 * 2)
        goto(n, 100 / 6 * 3)
        goto(z, 100 / 6 * 4)
        goto(n, 100 / 6 * 5)
        goto(z, 100)
    # zigzag beige clair
    remplir('cornflowerblue')
    zigzag(350, 300)
    end_fill()
    position(350, 0)
    remplir('cornflowerblue')
    zigzag(400, 350)
    position(350,0)
    goto(350, 100)
    end_fill()
quatre()

# ---------------------------------------------------------------
# CASE 5
# ---------------------------------------------------------------
def cinq():  # cinquième case
    remplir('lavender')      # fond lavande
    carreau(0,100)
    end_fill()
    position(0, 150)
    goto(100, 150)         # ligne horizontale
    # carré bleu
    position(0, 100)
    remplir('white')
    carre(50)
    end_fill()
    # petits cercles colorés
    position(25, 110)
    remplir('yellow')
    circle(15)
    end_fill()
    position(75, 110)
    remplir('yellow')
    circle(15)
    end_fill()
    # demi-cercles superposés
    position(0, 200)
    right(90)
    remplir('yellow')
    circle(50, 180)
    end_fill()
    goto(20, 200)
    right(180)
    remplir('white')
    circle(30, 180)
    end_fill()
    right(90)
cinq()

# ---------------------------------------------------------------
# CASE 6
# ---------------------------------------------------------------
def six():  # sixième case
    remplir('pink')
    carreau(100,100)
    end_fill()
    position(200,100)
    remplir('cornflowerblue')
    goto(150,100)
    goto(150,200)
    goto(200,200)
    end_fill()
    # demi-cercle jaune
    position(150, 110)
    remplir('yellow')
    circle(40,180)
    goto(150, 110)
    end_fill()
    # demi-cercle bleu fonce inversé
    setheading(180)
    remplir('cornflowerblue')
    position(150,190)
    circle(40,180)
    end_fill()
    position(150, 100)
    goto(150, 200)
six()

# ---------------------------------------------------------------
# CASE 7
# ---------------------------------------------------------------
def sept():  # septième case
    remplir('yellow')
    carreau(200,100)
    end_fill()
    # quatre petits carrés de couleurs différentes
    position(217.5, 117.5)
    remplir('lavender')
    carre(25)
    end_fill()
    position(257.5, 117.5)
    remplir('white')
    carre(25)
    end_fill()
    position(217.5, 157.5)
    remplir('white')
    carre(25)
    end_fill()
    position(257.5, 157.5)
    remplir('pink')
    carre(25)
    end_fill()
sept()

# ---------------------------------------------------------------
# CASE 8
# ---------------------------------------------------------------
def huit():  # huitième case
    remplir('cornflowerblue')
    carreau(300,100)
    end_fill()
    # motif central en forme d’étoile jaune
    position(357,153.5)
    left(45)
    remplir('yellow')
    for i in range(8):
        forward(15)
        right(60)
        circle(7,360/9*7.5)
        right(60)
        forward(15)
        right(135)
    end_fill()
    setheading(0)
huit()

# ---------------------------------------------------------------
# CASE 9
# ---------------------------------------------------------------
def neuf():  # neuvième case
    remplir('lavender')
    carreau(0,200)
    end_fill()
    position(0, 250)
    goto(100, 250)
    # demi-cercles violet et rose
    position(0, 300)
    remplir('pink')
    right(90)
    circle(50, 180)
    end_fill()
    goto(20, 300)
    right(180)
    remplir('cornflowerblue')
    circle(30, 180)
    end_fill()
    right(90)
    # motif rayé bleu et rose
    rayures(0,200,'cornflowerblue','pink')
neuf()

# ---------------------------------------------------------------
# CASE 10
# ---------------------------------------------------------------
def dix():  # dixième case
    remplir('yellow')
    carreau(100,200)
    end_fill()
    # motifs lavande et jaunes
    position(150,200)
    remplir('lavender')
    goto(100,250)
    goto(150,300)
    goto(100,300)
    goto(150,250)
    goto(100,200)
    goto(150,200)
    end_fill()
    # cercles jaunes décoratifs
    position(115,300)
    right(90)
    remplir('yellow')
    circle(10,180)
    end_fill()
    position(125,240)
    right(90)
    remplir('yellow')
    circle(10)
    end_fill()
    position(135,200)
    left(90)
    remplir('yellow')
    circle(10,180)
    end_fill()
    left(90)
    # partie rose
    position(200,200)
    remplir('pink')
    goto(150,200)
    goto(150,300)
    goto(200,300)
    end_fill()
    # trois cercles bleus alignés
    position(175,265)
    remplir('lavender')
    circle(10)
    end_fill()
    position(175,240)
    remplir('lavender')
    circle(10)
    end_fill()
    position(175,215)
    remplir('lavender')
    circle(10)
    end_fill()
dix()

# ---------------------------------------------------------------
# CASE 11
# ---------------------------------------------------------------
def onze():  # onzième case
    carreau(200,200)
    # drapeau tricolore rose / jaune / lavande
    position(200, 200)
    remplir('pink')
    goto(200, 300)
    position(200 + 100 / 3, 300)
    goto(200 + 100 / 3, 200)
    end_fill()
    remplir('yellow')
    position(200 + 100 / 3, 200)
    goto(200 + 100 / 3, 300)
    position(200 + 100 / 3 * 2, 300)
    goto(200 + 100 / 3 * 2, 200)
    end_fill()
    remplir('lavender')
    position(200 + 100 / 3 * 2, 200)
    goto(200 + 100 / 3 * 2, 300)
    position(300, 300)
    goto(300, 200)
    end_fill()
onze()

# ---------------------------------------------------------------
# CASE 12
# ---------------------------------------------------------------
def douze():  # douzième case
    carreau(300,200)
    # grands carrés et cercles colorés
    position(350, 200)
    remplir('white')
    carre(50)
    end_fill()
    goto(300,200)
    remplir('yellow')
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    end_fill()
    position(350, 250)
    setheading(0)
    remplir('cornflowerblue')
    carre(50)
    end_fill()
    position(375,260)
    remplir('lavender')
    circle(15)
    end_fill()
    position(375,210)
    left(45)
    remplir('lavender')
    carre(sqrt(450))
    end_fill()
    right(45)
douze()

# ---------------------------------------------------------------
# CASE 13
# ---------------------------------------------------------------
def treize():  # treizième case
    carreau(0,300)
    # deux carrés doré et argenté
    position(0, 350)
    remplir('white')
    carre(50)
    end_fill()
    position(50,350)
    remplir('pink')
    carre(50)
    end_fill()
    # deux cercles verts et rouges
    position(25, 360)
    remplir('lavender')
    circle(15)
    end_fill()
    position(75, 360)
    remplir('white')
    circle(15)
    end_fill()
    up()
    # motif rayé en fond
    rayures(0,300,'yellow','white')
treize()

# ---------------------------------------------------------------
# CASE 14
# ---------------------------------------------------------------
def quatorze():  # quatorzième case
    # bandes horizontales jaune / rose / lavande
    position(100,300)
    remplir('yellow')
    goto(200,300)
    position(200, 300 + 100 / 3)
    goto(100, 300 + 100 / 3)
    end_fill()
    position(100, 300 + 100 / 3)
    remplir('pink')
    goto(200, 300 + 100 / 3)
    position(200, 300 + 100 / 3 * 2)
    goto(100, 300 + 100 / 3 * 2)
    end_fill()
    position(100, 300 + 100 / 3 * 2)
    remplir('lavender')
    goto(200, 300 + 100 / 3 * 2)
    position(200, 400)
    goto(100, 400)
    end_fill()
    carreau(100,300)
quatorze()

# ---------------------------------------------------------------
# CASE 15
# ---------------------------------------------------------------
def quinze():  # quinzième case
    carreau(200,300)
    # losanges rose et cercles lavende
    position(225,300)
    remplir('pink')
    goto(300,375)
    goto(275,400)
    goto(200,325)
    goto(225,300)
    position(275,300)
    goto(200,375)
    goto(225,400)
    goto(300,325)
    goto(275,300)
    end_fill()
    # cercles lavende aux intersections
    position(225,316.5)
    remplir('lavender')
    circle(7)
    end_fill()
    position(275,316.5)
    remplir('lavender')
    circle(7)
    end_fill()
    position(275,366.5)
    remplir('lavender')
    circle(7)
    end_fill()
    position(225,366.5)
    remplir('lavender')
    circle(7)
    end_fill()
    position(250,341.5)
    remplir('lavender')
    circle(7)
    end_fill()
quinze()

# ---------------------------------------------------------------
# CASE 16
# ---------------------------------------------------------------
def seize():  # seizième case
    remplir('lavender')
    carreau(300,300)
    end_fill()
    # carrés bleu fonce
    position(350, 300)
    remplir('cornflowerblue')
    carre(50)
    end_fill()
    position(350, 350)
    remplir('cornflowerblue')
    carre(50)
    end_fill()
    # demi-cercles roses autour
    position(350, 400)
    right(180)
    remplir('cornflowerblue')
    circle(50, 180)
    end_fill()
    position(400, 400)
    left(180)
    remplir('pink')
    circle(50, 90)
    position(400,350)
    end_fill()
    position(400, 350)
    right(90)
    remplir('pink')
    circle(50, 90)
    position(400,300)
    end_fill()
    # redessine la bordure
    position(350, 400)
    goto(350,300)
    goto(350,350)
    goto(400,350)
    end_fill()
seize()








































exitonclick()