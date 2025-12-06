#!/usr/bin/env python

def cree_reseau(couples_amis):
    """
    Crée un réseau d'amis à partir d'une liste de paires d'amis.
    
    Paramètres : 
        couples_amis : liste de paires (a, b) où `a` et `b` sont des amis.
    
    Retourne : 
        Un dictionnaire représentant le réseau où :
        - Les clés sont les noms des personnes.
        - Les valeurs sont des listes contenant les noms de leurs amis.
    """
    reseau = {}                              # Initialisation du dictionnaire pour représenter le réseau
    i = 0                                    # Initialisation de l'indice pour parcourir la liste `couples_amis`
    while i < len(couples_amis):             # Tant qu'il reste des paires à traiter
        a, b = couples_amis[i]               # On extrait les deux noms de la paire d'amis à l'indice `i`

        if a not in reseau:                  # Si `a` n'existe pas encore comme clé dans le dictionnaire
            reseau[a] = []                   # On l'ajoute avec une liste vide pour ses amis

        if b not in reseau:                  # Si `b` n'existe pas encore comme clé dans le dictionnaire
            reseau[b] = []                   # On l'ajoute avec une liste vide pour ses amis

        if b not in reseau[a]:               # On ajoute `b` comme ami de `a` s'il n'est pas déjà présent
            reseau[a].append(b)

        if a not in reseau[b]:               # On ajoute `a` comme ami de `b` s'il n'est pas déjà présent
            reseau[b].append(a)

        i += 1                               # On passe à la paire suivante dans la liste

    return reseau                            # Retourne le dictionnaire qui représente le réseau
cree_reseau([("Dan", "Bob")])                # exemple d'appel de la fonction 





def liste_personnes(reseau):
    """
    Renvoie un tableau contenant les noms des membres du réseau.

    paramètre : un dictionnaire représentant le réseau social.
    
    retourne : un Tableau des membres du réseau.

    """
    personnes = []                  # Initialisation d'un tableau vide pour stocker les membres
    cles = list(reseau.keys())      # Conversion des clés du dictionnaire en tableau
    i = 0                           # Initialisation du compteur 
    while i < len(cles):            # Parcours des clés
        personnes.append(cles[i])   # Ajout de chaque clé (nom de personne) dans le tableau
        i += 1                      # Incrémentation du compteur 
    return personnes                # Retourne le tableau des membres





def sont_amis(reseau, personne1, personne2):
    """
    Vérifie si deux personnes sont amis dans un réseau social donné.
    
    Paramètres :
        reseau : Dictionnaire représentant le réseau social où les clés sont des prénoms, et les valeurs sont des listes des amis correspondants.
        personne1 : Nom de la première personne.
        personne2 : Nom de la deuxième personne.
        
    Retourne un booléen : True si personne2 est dans la liste des amis de personne1, sinon False.
    
    """
                                        # Vérifie si personne2 est dans la liste des amis de personne1
    if personne2 in reseau[personne1]:  # Condition pour vérifier si les deux personnes sont amis
        return True                     # Retourne True si personne2 est un ami de personne1
    else:                               # Sinon
        return False                    # Retourne False si personne2 n'est pas un ami de personne1

                                        # Exemple d'utilisation
reseau = {                              # Initialisation du réseau social
    "Alice": ["Bob", "Dan"],            # Les amis d'Alice
    "Bob": ["Alice", "Carl", "Dan"],    # Les amis de Bob
    "Carl": ["Bob"],                    # Les amis de Carl
    "Dan": ["Alice", "Bob"]             # Les amis de Dan
}
sont_amis(reseau, 'Alice', 'Bob')       # Vérifie si 'Alice' et 'Bob' sont amis




def sont_amis_de(reseau, personne, groupe):
    """
    Vérifie si une personne est amie avec tous les membres d'un groupe donné.
    
    Paramètres :
        reseau : Dictionnaire représentant le réseau social.
                       Les clés sont des prénoms, et les valeurs sont des listes des amis correspondants.
        personne : Nom de la personne à vérifier.
        groupe : Liste des noms des personnes appartenant au groupe.
        
    Retourne un booléen : True si la personne est amie avec tous les membres du groupe, sinon False.
    
    """
    for ami in groupe:                           # Parcours de chaque membre du groupe
        if ami not in reseau[personne]:          # Vérifie si le membre n'est pas dans la liste d'amis
            return False                         # Retourne False si un membre n'est pas un ami
    return True                                  # Retourne True si tous les membres sont amis




def est_comu(reseau, groupe):
    """
    Vérifie si un groupe de personnes constitue une communauté dans un réseau social.
    Une communauté est définie comme un groupe où chaque membre est ami avec tous les autres.
    
    Paramètres :
        reseau : Dictionnaire représentant le réseau social.
                       Les clés sont des prénoms, et les valeurs sont des listes des amis correspondants.
        groupe : Liste des noms des personnes appartenant au groupe.
        
    Retourne un booléen : True si le groupe forme une communauté, sinon False.
    
    """
    i = 0                                                   # Initialisation de l'indice pour parcourir le groupe
    while i < len(groupe):                                  # Tant qu'il reste des personnes à vérifier dans le groupe
        personne = groupe[i]                                # Récupération de la personne actuelle
        j = 0                                               # Initialisation de l'indice pour comparer avec d'autres membres
        while j < len(groupe):                              # Vérifie si la personne est amie avec tous les autres membres
            autre_personne = groupe[j]                      # Récupération de l'autre personne à comparer
            if personne != autre_personne:                  # On ne vérifie pas si une personne est amie avec elle-même
                if autre_personne not in reseau[personne]:  # Vérifie si l'autre personne n'est pas dans la liste d'amis
                    return False                            # Ce n'est pas une communauté si la condition échoue
            j += 1                                          # Passe à la prochaine personne à comparer
        i += 1                                              # Passe à la prochaine personne dans le groupe
    return True                                             # Si toutes les vérifications passent, c'est une communauté 




def comu(groupe, reseau):
    """
    Détermine les personnes qui forment une communauté parmi un groupe donné en vérifiant si chaque membre
    est ami avec tous les autres membres de la communauté.

    Paramètres :
        groupe : Liste des personnes à vérifier.
        reseau : Dictionnaire représentant le réseau social, où les clés sont des prénoms et les valeurs
                       des listes des amis correspondants.

    Retourne une liste des personnes qui forment une communauté.

    """
    communauté = []                                                         # Initialisation de la liste des membres de la communauté
    for personne in groupe:                                                 # Parcours de chaque personne dans le groupe
        amis_requis_ok = True                                               # Variable pour vérifier si la personne est amie avec tous les autres
        for ami in communauté:                                              # Vérifie si la personne est amie avec ceux déjà dans la communauté
            if ami not in reseau[personne] or personne not in reseau[ami]:  # Si une personne n'est pas amie avec un autre membre
                amis_requis_ok = False                                      # La personne ne peut pas faire partie de la communauté
                break                                                       # On arrête la vérification dès qu'une condition échoue
        if amis_requis_ok:                                                  # Si la personne est amie avec tous les autres dans la communauté
            communauté.append(personne)                                     # On l'ajoute à la communauté
    return communauté                                                       # Retourne la liste des membres de la communauté




def tri_popu(reseau, groupe):
    """
    Trie un groupe de personnes en fonction de leur popularité, définie par le nombre d'amis dans le réseau social.

    Paramètres :
        reseau : Dictionnaire représentant le réseau social.
                       Les clés sont des prénoms, et les valeurs sont des listes des amis correspondants.
        groupe : Liste des personnes à trier.

    Retourne une liste où le groupe trié par popularité décroissante.

    """
    popularite = {}                                                     # Création d'un Dictionnaire pour stocker la popularité de chaque personne
    for personne in groupe:                                             # Parcours de chaque personne dans le groupe
        if personne in reseau:                                          # Si la personne est présente dans le réseau
            popularite[personne] = len(reseau[personne])                # La popularité est le nombre d'amis
        else:
            popularite[personne] = 0                                    # Si la personne n'a pas d'amis, sa popularité est 0

    n = len(groupe)                                                     # Nombre de personnes dans le groupe
    for i in range(n):                                                  # Boucle pour trier le groupe par popularité
        for j in range(i + 1, n):                                       # Comparaison entre les membres du groupe
            if popularite[groupe[i]] < popularite[groupe[j]]:           # Si la personne i a moins d'amis que la personne j
                groupe[i], groupe[j] = groupe[j], groupe[i]             # Échange de place entre les deux personnes
    return groupe                                                       # Retourne le groupe trié par popularité décroissante





import time                                 # Importation du module time pour mesurer le temps d'exécution

                                            # Liste des relations d'amitié sous forme de tuples (personne1, personne2)
amis = [("Alice", "Bob"),
        ("Alice", "Dan"),
        ("Bob", "Carl"),
        ("Bob", "Dan")] * 1000              # Répétition de la liste 1000 fois pour augmenter la taille du réseau

                                            # Création du réseau social à partir de la liste d'amitiés
new_tab = cree_reseau(amis)
def comu_dans_reseau(reseau):
    """
    Trouve la communauté formée par les personnes du réseau social, en triant les membres par popularité.

    Paramètre :
        reseau : Dictionnaire représentant le réseau social, où les clés sont des prénoms et les valeurs
                 sont des listes des amis correspondants.

    Retourne une liste des membres de la communauté triée par popularité.
    """
    groupe = list(reseau.keys())          # Récupère la liste des personnes dans le réseau
    groupe_trie = tri_popu(reseau, groupe)  # Trie les personnes par popularité
    return comu(groupe_trie, reseau)      # Retourne la communauté formée
# Mesure du temps d'exécution de la fonction comu_dans_reseau avec un petit réseau
comu_dans_reseau({
    "Alice": ["Bob", "Dan"],
    "Bob": ["Alice", "Carl", "Dan"],
    "Carl": ["Bob"],
    "Dan": ["Alice", "Bob"]
})
# Mesure du temps d'exécution de la fonction comu_dans_reseau avec le grand réseau
debut = time.time()                     # Enregistre le temps de début
comu_dans_reseau(new_tab)               # Exécute la fonction
temps = time.time() - debut             # Calcule le temps écoulé

# Affiche le temps d'exécution en millisecondes
print("comu_dans_reseau met", temps * 1000, "millisecondes")





def comu_dans_amis(personne, reseau):
    """
    Trouve la communauté d'une personne dans le réseau social, en triant ses amis par popularité.

    Paramètres :
        personne : Nom de la personne de départ.
        reseau : Dictionnaire représentant le réseau social.

    Retourne une liste des membres de la communauté formée par la personne et ses amis.

    """
    amis = reseau[personne]                          # Récupère les amis de la personne
    amis_tries = tri_popu(reseau, amis)              # Trie les amis par popularité
    groupe = [personne] + amis_tries                 # Crée un groupe avec la personne et ses amis triés
    return comu(groupe, reseau)                      # Trouve et retourne la communauté formée
comu_dans_amis("Carl", {                                                             
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    })





def comu_max(reseau):
    """ 
    Trouve la plus grande communauté parmi tous les membres du réseau social.

    Paramètre : un dictionnaire représentant le réseau social 

    Retourne une liste de la plus grande communauté. 
    
    """
    communauté_max = []                                         # Initialisation de la communauté maximale                       
    
                                                                # Appliquer comu_dans_amis à chaque membre du réseau
    for personne in reseau:                                     # Parcours de chaque personne dans le réseau
        communauté = comu_dans_amis(personne, reseau)           # On récupère la communauté de la personne 

        if len(communauté) > len(communauté_max):               # Si la communauté de cette personne est plus grande que la communauté maximale actuelle
            communauté_max = communauté                         # On la met à jour
    
    return communauté_max                                       # On retourne la plus grande communauté 
                        




                        



