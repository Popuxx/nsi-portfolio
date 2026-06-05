###Projet réalisé par Paul Julliard, Yanis Francillon, Manel Gordo, Mathias Pignard

###SETUP

from nsi_ui import * # Importe les outils graphiques (boutons, listes...)


#On rentre les données d'entrée
animaux = [] # Création de la liste vide qui servira à stocker les dictionnaires des animaux

Annee_actuelle = 2025 # Année de référence pour savoir si un vaccin est périmé ou non dans la fonction de véerification

Fichier_sante = "sante.txt"   # Fichier de sauvegarde des animaux
Fichier_Limites_poids = "poids_limites_especes.txt" # Fichier de stockage des poids maximum


#On crée un dictionnaire avec une liste d'animaux connus avec comme clé = espèce et pour valeur = poids maximum de l'animal
Limites_poids = {
    "chat": 20.0,
    "chien": 75.0,
    "lapin": 10.0,
    "hamster": 0.5,
    "cheval": 700.0,
    "chinchilla": 0.8,
    "perroquet": 1.5,
    "tortue": 30.0,
    "poisson rouge": 0.3,
    "axolotl": 0.3
}

###FONCTIONS

#on crée la fonction pour charger les données du fichier sante.txt
def charger_donnees():

    animaux.clear() # On vide la liste sans utiliser la fonction open pour éviter d'avoir des doublons si le fichier est rechargé

    #On charge le fichier avec les animaux (sante.txt)
    with open('sante.txt', "r", encoding="utf-8") as f: #on utilise la fonction with pour ouvrir le fichier et c'est mieux d'être en utf-8 car ca permet de gérer les accents (souci rencontré quand on avais mis Félix sans préciser utf-8)
        for ligne in f: #on boucle sur les lignes du fichier
            ligne = ligne.replace("\n", "") # On supprime le caractère de retour à la ligne \n et on le remplace par rien


            if ligne != "": # On vérifie que la ligne n'est pas vide

                infos = ligne.split(";") # On découpe la ligne "Nom;Espèce;Poids;AnneeVaccin" avec la fonction split en utilisant le séparateur ;
                # On crée le dictionnaire avec toutes les informations incluses dans le fichier sante.txt et on convertit les différentes types (float/int)
                animaux.append({
                    "nom": infos[0],          # Type texte
                    "espece": infos[1],       # Type texte
                    "poids": float(infos[2]), # Type float car on peut avoir des virgules
                    "visite": int(infos[3])   # Type integer car l'année est un naturel
                })

##

def sauvegarder_donnees(): #fonction de sauvegarde des données dans un fichier txt. on sauvegarde deux fichiers sante avec la liste des animaux,espece, poids et date de vaccin et un avec les limites de poids par espèce pour garder les données rentrées une fois
    # On sauvegarde la liste des animaux et notamment ceux ajoutés ou supprimés

    with open(Fichier_sante, "w", encoding="utf-8") as f: # on utilise with open en mode "w" (écriture) et on met en utf-8 (plus sur pour les accents)
        for a in animaux: #on boucle sur le dictionnaire d'animaux
            f.write(f"{a['nom']};{a['espece']};{a['poids']};{a['visite']}\n") # On reconstruit la chaine de caractères pour le mettre dans le fichier avec le saut de ligne \n à la fin

    # on sauvegarde le fichier de limite des poids
    with open(Fichier_Limites_poids, "w", encoding="utf-8") as f: # on utilise with open en mode "w" (ecriture) et on met en utf-8 (plus sur pour les accents)
        for esp in Limites_poids: #on boucle sur le dictionnaire
            limite = Limites_poids[esp] # On récupère la valeur (la limite) en utilisant la clé
            f.write(f"{esp};{limite}\n") # On écrit dans le fichier et on ajouter le \n a la fin pour le saut de ligne
    set_text(lbl_message, "Tout est sauvegardé normalement!") #on affiche un message non modifiable pour dire que les données sont sauvegardées

##

def verifier_poids(espece, poids, limite_saisie): # On veut vérifier que les poids rentrés sont  ni négatifs ni trop grands
    if poids <= 0:
        return False, "Poids négatif interdit." #On fait le cas pour un poids négatif ou nul ce qui est impossible
    if poids > 1000:
        return False, "Poids trop important (une tonne me parait trop pour un animal)." #On fait le cas pour un poids trop important. On a mis ici 1000kg pour la référence mais cela varie en fonction du poids maximum qui a été fixé par expèce

    espece = espece.lower() #pour éviter que des majuscules soient vues comme un autre animal (chat -> Chat)

    # on a fait deux cas selon si on connait ou pas l'espèce de l'animal et on fait un cas differencié sur le poids maximum selon l'espèce. le poids max d'un chien est différent du poids max d'un hamster
    if espece in Limites_poids: #on vérifie si l'espèce existe déjà dans la base de données des limites de poids
        limite = Limites_poids[espece] #on recupère le poids limite
        if poids > limite: #on vérifie le poids
            return False, f"Trop lourd pour {espece} (Max {limite}kg)" #on affiche un message d'erreur pour dire que le poids donné doit être erroné
        return True, "OK" #on affiche un message de confirmation

    # Si on ne connait pas l'espèce, il faut rentrer le poids maximum a vérifier
    else:
        if limite_saisie > 0: # on vérifie que l'utilisateur a rempli la case "Limite Max"
            Limites_poids[espece] = limite_saisie # on ajoute l'espèce dans le dictionnaire
            return True, f"Nouvelle espèce : {espece}" #on affiche un message confirmant l'ajout d'une nouvelle espèce
        return False, f"Espèce inconnue. Remplissez 'Limite Max'." #on affiche un message d'erreur

##

def choisir_un_animal(selection_texte): #c'est la fonction qui permet de récuperer les données du dictionnaire quand je clique sur un animal qui existe
    if selection_texte == "": #on vérifie si c'est vide ou pas
        return

    if " (" in selection_texte: #dans l'affichage on a mis nom(espèce)
        parts = selection_texte.split(" (") #on récupère seulement le nom avant la parenthèse
        nom_rech = parts[0] # On garde juste le nom

    # Recherche linéaire avec drapeau
    trouve = False
    for a in animaux: #on boucle sur le dictionnaire pour trouve l'animal
        if trouve == False and a["nom"] == nom_rech: # Si on n'a pas encore trouvé le nom mais que le nom correspond
            set_text(ent_nom, a["nom"]) #on récupère le nom de l'animal dans le dictionnaire
            set_text(ent_espece, a["espece"]) #on récupère l'espèce de l'animal dans le dictionnaire
            set_text(ent_poids, str(a["poids"])) #on récupère le poids de l'animal dans le dictionnaire et on le convertit en string
            set_text(ent_visite, str(a["visite"])) #on récupère l'année du vaccin de l'animal dans le dictionnaire et on le convertit en string
            trouve = True # On arrête de chercher

##

def ajouter_un_animal(): #fonction pour ajouter un animal
    n = get_string(ent_nom) #on récupère le nom rentré par l'utilisateur (on nomme la variable n car la variable nom existe deja)
    e = get_string(ent_espece).lower() #on récupère l'espèce rentrée par l'utilisateur et on met tout en miniscule pour eviter les soucis miniscule majuscule (on nomme la variable e car la variable espece existe deja)

    poids = get_string(ent_poids) #on récupère le poids rentré par l'utilisateur (ent est l'abréviation pour entrée car si on met entree_poids, python confond la variable avec une fonction)
    vaccin = get_string(ent_visite) #on récupère l'année de vaccination rentrée l'utilisateur (ent est l'abréviation pour entrée car si on met entree_visite, python confond la variable avec une fonction)

    if n == "" or e == "" or poids == "" or vaccin == "": #on vérifie que l'utilisateur a bien tout rempli
        set_text(lbl_message, "Remplissez tous les champs !") #message d'erreur si une case n'a pas été remplie
        return

    p = float(poids) #on convertit en float pour être en accord avec le dictionnaire (on nomme la variable p car la variable poids existe déjà)
    v = int(vaccin) #on convertit en integer pour être en accord avec le dictionnaire (on nomme la variable v car la variable vaccin existe déjà)

    # Gestion de la limite max optionnelle
    txt_lim = get_string(ent_limite_nouvelle) #on récupère le texte dans la case de la nouvelle limite de poids (ent est l'abreviation pour entrée car si on met entrée, python confond la variable avec une fonction)
    if txt_lim != "":  #s'il y a qqchose je l'ajoute et je le convertis en float
        lim_user = float(txt_lim)
    else:
        lim_user = 0.0 #s'il n'y a rien c'est mis à 0 sinon cela fait un bug

    valide, msg = verifier_poids(e, p, lim_user) #on fait appel à notre fonction de vérification de poids et on récupère le statut true/false et le message
    #print(valide,msg) #TEST A NE PAS DECOMMENTER

    if not valide: #si ce n'est pas valide
        set_text(lbl_message, msg) #on affiche le texte d'erreur dans l'interface
        return

    animaux.append({"nom": n, "espece": e, "poids": p, "visite": v}) #si tout est bon on ajoute l'animal au dictionnaire
    mise_a_jour_menus_especes() #on fait appel a la fonction de mise a jour du menu
    sauvegarder_donnees() #on sauvegarde les données avec la fonction
    afficher_liste() #on appelle la fonction d'affichage des listes

    set_text(lbl_message, f"Animal ajouté : {n}") #message confirmant l'ajout de l'animal
    set_text(ent_poids, "") #Réinitialise la case
    set_text(ent_espece, "") #Réinitialise la case
    set_text(ent_nom, "") #Réinitialise la case
    set_text(ent_visite, "2025") #Réinitialise la case
    set_text(ent_limite_nouvelle, "") #Réinitialise la case

##

def changer_poids_animal(): #fonction de correction de changement de poids de l'animal
    sel = get_string(lst_animaux) #On utilise la fonction de nsi_ui get_string pour récupérer l'animal qui est sélectionné (sel est l'abréviation de sélection car si on met selection, python confond avec une fonction)
    if sel == "": #on gère le cas ici du cas où il n'ya rien de sélectionné (sel est l'abréviation de sélection car si on met selection, python confond avec une fonction)
        set_text(lbl_message, "CLIQUEZ SUR UN ANIMAL D'ABORD !") #on affiche le message d'erreur demandant à l'utilisateur de sélectionner un animal
        return


    parts = sel.split(" (") # on récupère les différentes parties nom;espece (sel est l'abréviation de selection car si on met selection, python confond avec une fonction)
    nom_cible = parts[0] #on récupère le nom de l'animal cible dont on veut changer le nom
    espece_cible = parts[1][:-1] # On enlève la parenthèse fermante de la fin après le nom de l'espèce

    new_p = float(get_string(ent_poids)) #on récupère ici le nouveau poids rentré par l'utilisateur avec la fonction get_string de nsi_ui (p est l'abréviation de poids car la variable poids existe deja)

    trouve = False
    for a in animaux: #on va maintenant parcourir le dictionnaire pour touver le nom et l'espce
        if trouve == False and a["nom"] == nom_cible and a["espece"] == espece_cible: #on cherche dans le dictionnaire l'animal à changer et on arrête quand l'animal a été trouvé
            valide, msg = verifier_poids(a["espece"], new_p, 0) #on vérifie  si le poids est dans la norme attendue et on met 0 car ce n'est pas une nouvelle espèce
            if valide:
                a["poids"] = new_p # on modifie le poids avec les nouvelles données utilisateur
                sauvegarder_donnees() # on sauvegarde le fichier
                set_text(lbl_message, f"Poids modifié : {new_p}kg") #on affiche un message pour dire à l'utilisateur que le poids a été modifié
                afficher_liste() #on met a jour l'affichage
            else:
                set_text(lbl_message, msg) #si le poids n'est pas dans la fourchette attendue on affiche le message d'erreur
            trouve = True

##

def supprimer_animal(): #fonction pour supprimer un animal
    sel = get_string(lst_animaux) #On utilise la fonction de nsi_ui get_string pour récupérer l'animal qui est sélectionné (sel est l'abréviation de selection car si on met selection, python confond avec une fonction)
    if sel == "":  #on gère le cas ici du cas où il n'ya rien de sélectionné (sel est l'abréviation de selection car si on met selection, python confond avec une fonction)
        set_text(lbl_message, "Sélectionnez un animal !") #on affiche le message d'erreur
        return

    parts = sel.split(" (") # on récupère les differentes parties nom;espece (sel est l'abréviation de selection car si on met selection, python confond avec une fonction)
    nom_cible = parts[0] #on récupère le nom de l'animal cible dont on veut changer le nom
    espece_cible = parts[1][:-1] # On enlève la parenthèse fermante de la fin après le nom de l'espèce

    i = 0
    trouve = False
    while i < len(animaux) and trouve == False: #on cherche l'animal à supprimer dans le dictionnaire et tant qu'il n'est pas trouvé on continue
        a = animaux[i] #on parcourt le dictionnaire des animaux
        if a["nom"] == nom_cible and a["espece"] == espece_cible:
            del animaux[i] # On supprime l'élément à l'index i
            trouve = True  # On arrète la boucle
        else:
            i = i + 1 # On cherche l'élément suivant seulement si on n'a rien supprimé

    if trouve:
        sauvegarder_donnees() #on sauvegarde les données avec la fonction
        afficher_liste() #on appelle la fonction de mise à jour de l'affichage des listes
        set_text(ent_nom, "") # Remet les champs à 0
        set_text(ent_poids, "0") # Remet les champs à 0
        set_text(lbl_message, "Supprimé.") # Je mets le message que c'est supprimé
    else:
        set_text(lbl_message, "Erreur : Pas trouvé.")

##

def especes_existantes(): #pour éviter les doublons (il peut y avoir plusieurs chats, chiens...), on isole chaque espèce une fois
    liste = [] #on crée une liste des especes
    for a in animaux: #on parcourt le dictionnaire
        if a["espece"] not in liste: # On n'ajoute l'espèce que si elle n'est pas déjà présente pour éviter les doublons
            liste.append(a["espece"]) #on ajoute l'espèce a la liste avec append
    return liste #on retourne la liste

##

def mise_a_jour_menus_especes(): #on utilise cette fonction pour mettre à jour les différentes listes des espèces notamment quand on ajoute des nouvelles espèces
    liste = especes_existantes() #on appelle la fonction des especes existantes
    update_options(menu_filtre, liste) #on met à jour les menus déroulants avec la fonction de nsi_ui qui permet de remplacer la liste des especes
    update_options(menu_especes_1, liste) #on met à jour les menus déroulants avec la fonction de nsi_ui qui permet de remplacer la liste des especes
    update_options(menu_especes_2, liste) #on met à jour les menus déroulants avec la fonction de nsi_ui qui permet de remplacer la liste des especes

##

def noms_animaux_affichage(): #Pour faire un affichage propre nom (espece) dans l'interface on construit une liste à afficher
    liste = [] #création de la liste
    for a in animaux: #on parcourt le dictionnaire animaux
        liste.append(f"{a['nom']} ({a['espece']})") #on ajoute à la liste l'affichage voulu nom (espece) ca permet comme ca de vérifier que le tri par espèce se passe bien par exemple et que le tri de a à z également
    return liste #on renvoie la liste des animaux à afficher

##

def afficher_liste(): #on veut ici mettre à jour l'affichage de l'interface
    update_list(lst_animaux, noms_animaux_affichage()) #on utilise la fonction nsi_ui update_list

##

def critere_tri_nom(animal): #on remet les noms en minuscule pour le tri
    return animal["nom"].lower() #on met les noms en minuscule avec la fonction lower()

##

def trier_nom(): #c'est la fonction de tri
    animaux.sort(key=critere_tri_nom) #on trie la liste par ordre alphabétique des noms
    afficher_liste() #on utilise la fonction d'affichage des listes

##

def filtrer_espece(): #La fonction va trier les animaux d'une espèce voulue
    esp = get_string(menu_filtre) #on récupère ici l'espèce que l'on veut trier
    if esp == "":  #on gère le cas où rien n'est mis
        return
    res = [] #on crée ici la liste des animaux de l'espèce souhaité
    for a in animaux: #on parcourt le dictionnaire
        if a["espece"] == esp: # On garde seulement ceux qui correspondent à l'espèce
            res.append(f"{a['nom']} ({a['espece']})") #on ajoute à la liste les animaux de l'espèce
    update_list(lst_animaux, res) #on met à jour la liste grace à la fonction nsi_ui update list

##

def afficher_tout(): #ca permet de réafficher tous les animaux après un tri
    afficher_liste() #on réaffiche toute la liste

##

def moyenne_une_espece(): #c'est la fonction de calcul de la moyenne des poids pour une espèce
    e1 = get_string(menu_especes_1) #on récupère l'espèce à moyenner
    if e1 == "": #on gère le cas où rien n'est mis
        return

    total = 0 # c'est la somme des poids des animaux de l'espèce choisie
    count = 0 # c'est le nombre d'animaux de l'espèce choisie
    for a in animaux: #on boucle sur le dictionnaire
        if a["espece"] == e1: #si c'est la bonne espèce
            total = total + a["poids"] #on ajoute le poids de l'animal
            count = count + 1 #on rajoute un animal à la somme des animaux de l'espèce

    if count > 0: #s'il y a plus de un animal
        moy = round(total/count, 2) #on calcule la moyenne en laissant deux chiffres après la virgule (on peut modifier ce paramètre par un autre chiffre si on veut plus de chiffres après la virgule)
        set_text(lbl_message, f"Moyenne {e1}: {moy}kg") #on affiche le résultat obtenu avec la fonction set_text de nsi_ui

##

def comparer_deux_especes(): #fonction pour comparer deux espèces de la liste
    e1 = get_string(menu_especes_1) #on récupère l'espèce n°1 à moyenner
    e2 = get_string(menu_especes_2) #on récupère l'espèce n°2 à moyenner

    if e1 == "" or e2 == "":  #on gère le cas où rien n'est mis
        set_text(lbl_message, "Il faut sélectionner 2 espèces !") #on met un message pour signaler qu'il faut sélectionner deux espèces
        return

    # Calcul de la moyenne  de l'espece n°1
    total1 = 0 # c'est la somme des poids des animaux de l'espèce n°1 choisie
    count1 = 0 # c'est le nombre d'animaux de l'espèce n°1 choisie
    for a in animaux: #on boucle sur le dictionnaire
        if a["espece"] == e1: #on vérifie si c'est la bonne espèce
            total1 = total1 + a["poids"]  #on ajoute le poids de l'animal de l'espèce n°1
            count1 = count1 + 1 #on rajoute un animal à la somme des animaux de l'espèce n°1
    if count1 > 0: # s'il y a plus de un animal
        moy1 = round(total1 / count1, 2) #on calcule la moyenne en laissant deux chiffres après la virgule (on peut modifier ce paramètre par un autre chiffre si on veut plus de chiffres après la virgule)
    else: #s'il n'y a pas d'animaux on met la moyenne à 0
        moy1 = 0 #on met la moyenne à 0

    # Calcul de la moyenne  de l'espèce n°2
    total2 = 0 # c'est la somme des poids des animaux de l'espèce n°2 choisie
    count2 = 0 # c'est le nombre d'animaux de l'espèce n°2 choisie
    for a in animaux: #on boucle sur le dictionnaire
        if a["espece"] == e2: #on vérifie si c'est la bonne espèce
            total2 = total2 + a["poids"] #on ajoute le poids de l'animal de l'espèce n°2
            count2 = count2 + 1 #on rajoute un animal à la somme des animaux de l'espèce n°2
    if count2 > 0:  # s'il y a plus de un animal
        moy2 = round(total2 / count2, 2) #on calcule la moyenne en laissant deux chiffres après la virgule (on peut modifier ce paramètre par un autre chiffre si on veut plus de chiffres après la virgule)
    else:  #s'il n'y a pas d'animal on met la moyenne à 0
        moy2 = 0

    set_text(lbl_message, f"{e1}: {moy1}kg  VS  {e2}: {moy2}kg") #message affiché avec les deux moyennes avec la fonction set_text

##

def alertes_vaccin(): #on veut vérifier ici les animaux qui doivent être vaccinés
    res = [] #on crée la liste qui va récupérer les animaux devant être vaccinés
    for a in animaux: #on parcourt le dictionnaire des animaux

        if Annee_actuelle - a["visite"] >= 1: # on vérifie si la visite date de plus d'un an (2025 - Année >= 1) en prenant la variable année du début du programme
            res.append(f"! {a['nom']} ({a['visite']})") #on ajoute les animaux devant être vaccinés à la liste avec le nom animal (année vaccination)

    if len(res) > 0: # Si la liste a au moins un animal
        update_list(lst_animaux, res) #on met à jour l'affichage des animaux devant être vaccinés
        set_text(lbl_message, "Attention : vaccins plus à jour!") #on affiche un message pour prévenir qu'il faut faire les vaccins
    else:
        afficher_liste() #on met a jour avec une liste vide
        set_text(lbl_message, "Tout est à jour pour les vaccins.") #on met un message que tout est à jour


###CONSTRUCTION DE L'INTERFACE

# on construit l'interface avec nsi_ui
begin_horizontal() #on démarre une ligne horizontale

#on commence à faire une colonne a gauche pour mettre les noms des animaux
begin_vertical() #on débute une colonne
label(" LISTE DES ANIMAUX ") #on affiche "LISTE DES ANIMAUX"
# on récupère la liste liée à la fonction 'def choisir_un_animal'
lst_animaux = listbox("Animaux", [], choisir_un_animal) #on crée une liste des animaux
set_height(lst_animaux, 100) # on impose la hauteur de la fenêtre


begin_horizontal() #on démarre une ligne horizontale pour mettre les boutons Voir Tout Les Animaux
button("Voir tous les animaux", afficher_tout) #on affiche le bouton et on lui associ la fonction afficher_tout qui permet de voir tous les animaux
button("Trier les animaux de A-Z", trier_nom) #on affiche le bouton et on lui associe la fonction de tri des noms par ordre alphabétique
end_horizontal() #on termine la ligne horizontale avec les deux boutons

label(" FILTRES PAR ESPECE ") #on affiche ce "FILTRE PAR ESPECES"
begin_horizontal() #on démarre une ligne horizontale pour mettre les boutons Espece
menu_filtre = option_menu("Filtre une espèce :", []) #on crée un menu déroulant avec une liste vide et on met a jour quand on charge les données (maj_menusespeces) grace a la fonction update_options
button("Filtrer espèce", filtrer_espece) #on crée un bouton avec l'action de filtrer les espèces
end_horizontal() #on termine cette ligne

end_vertical() #on termine la première ligne verticale


begin_vertical() #on commence une nouvelle colonne
label(" SAISIE DE L'ANIMAL ") #on affiche un texte pour l'utilisateur
ent_nom = entry("Nom animal:") #on crée une zone de saisie pour entrer le nom de l'animal
ent_espece = entry("Espèce animal:") #on créée une zone de saisie pour entrer l'espèce de l'animal
ent_poids = entry("Poids (kg) :")#on crée une zone de saisie pour entrer le poids de l'animal
ent_visite = entry("Année visite :") #on crée une zone de saisie pour entrer l'année de vaccination de l'animal
set_text(ent_visite, str(Annee_actuelle)) #on affiche par défaut l'année actuelle dans l'affichage si on crée un nouvel animal
ent_limite_nouvelle = entry("Limite Max (si nouvelle espèce) :") #si on rentre une nouvelle espèce (cheval par exemple), il faut rentrer le poids max à vérifier

begin_horizontal() #on commence une nouvelle ligne
button("AJOUTER", ajouter_un_animal) #On crée le bouton ajouter qui permet d'ajouter l'animal et la fonction associée à l'ajout
button("MISE A JOUR DU POIDS", changer_poids_animal) #on crée un bouton mise a jour du poids et on associe la fonction de mise a jour du poids
button("SUPPRIMER", supprimer_animal) #on crée un nouveau bouton qui permet de supprimer un animal et on associe la fonction supprimer
end_horizontal() #on termine la nouvelle ligne

label(" MOYENNES UNE ESPECE ou COMPARAISON DEUX ESPECES ") #on affiche pour aider l'utilisateur
begin_horizontal() #on commence une nouvelle ligne
menu_especes_1 = option_menu("Espèce n°1", []) #on crée un menu déroulant qui est mis a jour au chargement des données (update_options)
menu_especes_2 = option_menu("Espèce n°2", []) #on crée un menu déroulant qui est mis a jour au chargement des données (update_options)
end_horizontal() #on termine la nouvelle ligne

begin_horizontal() #on commence une nouvelle ligne
button("Moyenne espece n°1", moyenne_une_espece) #on crée un bouton pour faire la moyenne d'une espèce et on lui associe la fonction moyenne espece
button("Comparer deux especes", comparer_deux_especes) #on crée un bouton pour ajouter une seconde espèce et comparer la moyenne de poids de deux espèces
end_horizontal()  #on termine la nouvelle ligne

label(" VACCINS A FAIRE") #on affiche pour aider l'utilsateur
button("Alertes Vaccin", alertes_vaccin) #on affiche le bouton qui permet de voir les animaux qui doivent être vaccinés et on lui associe la fonction associée
label(" SAUVEGARDER DONNES ESPECES") #on affiche pour aider l'utilisateur
button("SAUVEGARDER", sauvegarder_donnees) #on affiche le bouton de sauvegarde des données et on lui associe la fonction de sauvegarde

lbl_message = label("Prêt") #on crée un zone de texte non modifiable par l'utilisateur sur laquelle on va afficher les informations non modifiables à l'utilisateur
set_width(lbl_message, 45) #on définit la largeur du texte

end_vertical() #on termine la colonne
end_horizontal() #on termine la ligne

charger_donnees() #on lance la fonction de chargement des données
start_ui() #on démarre l'interface graphique