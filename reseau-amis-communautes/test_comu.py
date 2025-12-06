#!/usr/bin/env python

from comu import *

def test_cree_reseau():                                         # création d'une fonction test de la fonction cree_reseau                                
    assert cree_reseau([]) == {}                                # Test avec un réseau vide
    reseau1 = [                                                 # Test avec un petit réseau
        ("Marc", "Julie"), 
        ("Marc", "Thomas"), 
        ("Julie", "Sophie")
    ]
    assert cree_reseau(reseau1) == {
        'Marc': ['Julie', 'Thomas'],
        'Julie': ['Marc', 'Sophie'],
        'Thomas': ['Marc'],
        'Sophie': ['Julie']
    }
    
    reseau2 = [("Emma", "Lucas")]                               # Test avec une seule paire d'amis
    assert cree_reseau(reseau2) == {
        'Emma': ['Lucas'],
        'Lucas': ['Emma']
    }
    
    reseau3 = [                                                 # Test avec un réseau en étoile (une personne centrale)
        ("Sarah", "Paul"),
        ("Sarah", "Marie"),
        ("Sarah", "Pierre")
    ]
    assert cree_reseau(reseau3) == {
        'Sarah': ['Paul', 'Marie', 'Pierre'],
        'Paul': ['Sarah'],
        'Marie': ['Sarah'],
        'Pierre': ['Sarah']
    }
    
    print("Tous les tests de cree_reseau sont passés avec succès") # Affichage du message si tous les tests marchent 

test_cree_reseau()                                                 # Lancement des tests  




def test_liste_personnes():    # création d'une fonction test de la fonction liste_personnes
    # Test avec un réseau vide
    assert liste_personnes({}) == []
    
    # Test avec un petit réseau
    reseau1 = {
        'Marc': ['Julie', 'Thomas'],
        'Julie': ['Marc', 'Sophie'],
        'Thomas': ['Marc'],
        'Sophie': ['Julie']
    }
    assert liste_personnes(reseau1) == ['Marc', 'Julie', 'Thomas', 'Sophie']
    
    # Test avec une seule paire d'amis
    reseau2 = {
        'Emma': ['Lucas'],
        'Lucas': ['Emma']
    }
    assert liste_personnes(reseau2) == ['Emma', 'Lucas']
    
    # Test avec un petit groupe d'amis
    reseau3 = {
        'Leo': ['Nina', 'Max'],
        'Nina': ['Leo'],
        'Max': ['Leo']
    }
    assert liste_personnes(reseau3) == ['Leo', 'Nina', 'Max']
    
    # Test avec un réseau simple à trois personnes
    reseau4 = {
        'Alex': ['Ben'],
        'Ben': ['Alex', 'Chloe'],
        'Chloe': ['Ben']
    }
    assert liste_personnes(reseau4) == ['Alex', 'Ben', 'Chloe']
    
    print("Tests de liste_personnes : ok ")   # message censé etre affiché si les tests sont bons
# Lancement des tests
test_liste_personnes()




def test_sont_amis():       # création de la fonction test pour la fonction sont_amis*

    reseau = {                                   # Création du réseau de test
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    # Test d'amitié réciproque
    assert sont_amis(reseau, 'Alice', 'Bob') == True
    assert sont_amis(reseau, 'Bob', 'Alice') == True

    # Test d'amitié non réciproque
    assert sont_amis(reseau, 'Carl', 'Bob') == True
    assert sont_amis(reseau, 'Bob', 'Carl') == True

    # Test de personnes qui ne sont pas amies
    assert sont_amis(reseau, 'Alice', 'Carl') == False
    assert sont_amis(reseau, 'Carl', 'Dan') == False

    # Test avec un autre réseau plus simple
    petit_reseau = {
        "Marc": ["Julie"],
        "Julie": ["Marc", "Sophie"],
        "Sophie": ["Julie"]
    }
    # Test d'amitié dans le petit réseau
    assert sont_amis(petit_reseau, 'Marc', 'Julie') == True
    assert sont_amis(petit_reseau, 'Julie', 'Sophie') == True
    assert sont_amis(petit_reseau, 'Marc', 'Sophie') == False

    print("Tous les tests de sont_amis sont passés ")  # message censé etre affiché si les tests sont bons

test_sont_amis()                           # Lancement des tests





def test_sont_amis_de() :               # création d'une fonction test de la fonction sont_amis_de 
    reseau = {                          # Création du réseau de test
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Dan"],
        "Dan": ["Alice", "Bob"]
    }
    assert sont_amis_de(reseau, 'Alice', ['Bob', 'Dan']) == True   
    assert sont_amis_de(reseau, 'Bob', ['Alice', 'Dan']) == True
    assert sont_amis_de(reseau, 'Dan', ['Alice', 'Bob']) == True
    assert sont_amis_de(reseau, 'Alice', ['Carl']) == False
    assert sont_amis_de(reseau, 'Alice', ['Bob', 'Carl']) == False
    print("Tests sont_amis_de OK!")
test_sont_amis_de()




def test_est_comu():
    # Réseau de test
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }

    # Test d'un groupe qui forme une communauté
    groupe_1 = ["Alice", "Bob", "Dan"]
    assert est_comu(reseau, groupe_1) == True  # Alice, Bob, et Dan sont amis entre eux

    # Test d'un groupe qui ne forme pas une communauté (Carl n'est pas ami avec Alice)
    groupe_2 = ["Alice", "Bob", "Carl"]
    assert est_comu(reseau, groupe_2) == False  # Carl n'est pas ami avec Alice

    # Test d'un groupe vide (ce n'est pas une communauté)
    groupe_3 = []
    assert est_comu(reseau, groupe_3) == True  # Un groupe vide est considéré comme une communauté
    print("Tous les tests de est_comu sont passés !")

# Lancement des tests
test_est_comu()




def test_comu():
    # création d'un réseau d'amis avec plusieurs personnes
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }

    # Test 1: Un groupe qui forme une communauté
    groupe_1 = ["Alice", "Bob", "Dan"]
    # Alice, Bob et Dan sont tous amis entre eux, donc ce groupe doit former une communauté.
    assert comu(groupe_1, reseau) == ["Alice", "Bob", "Dan"]

    # Test 2: Un groupe où une personne n'est pas amie avec un autre membre
    groupe_2 = ["Alice", "Bob", "Carl"]
    # Carl n'est pas ami avec Alice, donc ce groupe ne forme pas une communauté complète.
    assert comu(groupe_2, reseau) == ["Alice", "Bob"]

    # Test 3: Un groupe avec une seule personne
    groupe_3 = ["Alice"]
    # Une seule personne est toujours une communauté.
    assert comu(groupe_3, reseau) == ["Alice"]

    # Test 4: Un groupe vide
    groupe_4 = []
    # Un groupe vide est aussi une communauté.
    assert comu(groupe_4, reseau) == []

    print("Tous les tests de comu sont bons")
# Lancement des tests
test_comu()
 



def test_tri_popu():
    reseau = {                                                             # Réseau de test
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    # Test 1: Un groupe avec des personnes ayant différentes popularités
    groupe_1 = ["Alice", "Bob", "Dan", "Carl"]                                                                     
    assert tri_popu(reseau, groupe_1) == ["Bob", "Alice", "Dan", "Carl"]  # Bob a le plus grand nombre d'amis (3), suivi d'Alice et Dan (2), puis Carl (1)
    # Test 2: Un groupe avec une personne ayant aucun ami
    groupe_2 = ["Alice", "Carl", "Eve"]
    assert tri_popu(reseau, groupe_2) == ["Alice", "Carl", "Eve"]         # Eve n'a aucun ami dans le réseau, donc elle devrait être en dernier dans le tri
    # Test 3: Un groupe vide
    groupe_3 = []
    assert tri_popu(reseau, groupe_3) == []                               # Un groupe vide reste vide après le tri
    print("Tous les tests de tri_popu sont passés avec succès!")
# Lancement des tests
test_tri_popu()





def test_comu_dans_reseau():
    # Test 1 : Vérification du résultat correct pour la fonction comu_dans_reseau
    assert comu_dans_reseau({
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }) == ['Bob', 'Alice', 'Dan']  # Vérifie que la communauté retournée est correcte
    # Test 2 : Vérification de la communauté incorrecte
    assert not comu_dans_reseau({
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }) == ['Alice', 'Dan']  # Vérifie qu'une communauté incorrecte ne passe
    print("Tous les tests de comu_dans_reseau sont bons !")
test_comu_dans_reseau()




def test_comu_dans_amis():
    # Test 1 : Vérification de la communauté pour "Dan"
    assert comu_dans_amis("Dan", {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }) == ["Dan", "Bob", "Alice"]  # Vérifie que la communauté pour "Dan" est correcte
    # Test 2 : Vérification d'une communauté incorrecte pour "Bob"
    assert not comu_dans_amis("Bob", {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }) == ["Dan", "Bob", "Alice"]  # Vérifie que la communauté de "Bob" est incorrecte
    # Test 3 : Vérification de la communauté pour "Alice"
    assert comu_dans_amis("Alice", {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }) == ["Alice", "Bob", "Dan"]  # Vérifie que la communauté de "Alice" est correcte
    print("Tous les tests de comu_dans_amis_simple sont réussis.")
# Lancer les tests
test_comu_dans_amis()




def test_comu_max():
    reseau = {
        "Alice": ["Bob", "Dan"],
        "Bob": ["Alice", "Carl", "Dan"],
        "Carl": ["Bob"],
        "Dan": ["Alice", "Bob"]
    }
    # Test 1: Vérifier que la plus grande communauté est ["Alice", "Bob", "Dan"]
    assert comu_max(reseau) == ["Alice", "Bob", "Dan"]
    # Test 2: Vérifier que la plus grande communauté n'est pas ["Alice", "Carl"]
    assert comu_max(reseau) != ["Alice", "Carl"]
    # Test 3: Vérifier que la plus grande communauté n'est pas ["Bob", "Carl"]
    assert comu_max(reseau) != ["Bob", "Carl"]
    # Test 4: Vérifier que la plus grande communauté n'est pas ["Alice", "Bob"]
    assert comu_max(reseau) != ["Alice", "Bob"]
    # Test 5: Vérifier que la plus grande communauté n'est pas ["Carl", "Dan"]
    assert comu_max(reseau) != ["Carl", "Dan"]
    print("Tous les tests de comu_max sont passés avec succès.")
# Lancer les tests
test_comu_max()

