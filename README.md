# Détection de communautés dans un réseau d'amis (Python)

Projet de SAE réalisé en binôme : **détection de communautés dans un réseau social d'amis**, modélisé sous forme de graphe non orienté.

L'objectif est de représenter un réseau d'amis à l'aide d'un dictionnaire Python et d'implémenter différentes fonctions pour :
- construire le réseau à partir d'une liste de couples d'amis,
- vérifier les relations d'amitié,
- identifier des communautés (groupes où tout le monde est ami avec tout le monde),
- trouver la communauté maximale dans le réseau,
- comparer les performances des différentes approches.

---

## Objectifs du projet

- Manipuler des **structures de données** en Python (dictionnaires, listes).
- Modéliser un **réseau social** comme un graphe non orienté.
- Implémenter des **fonctions d'analyse de graphe** :
  - test d'amitié,
  - appartenance à une communauté,
  - construction d'une communauté autour d'une personne,
  - recherche de la plus grande communauté.
- Mesurer le **temps d'exécution** et analyser la complexité des fonctions.

---

## Fonctionnalités principales

Le réseau est représenté par un dictionnaire :

```python
reseau = {
    "Alice": ["Bob", "Dan"],
    "Bob": ["Alice", "Carl", "Dan"],
    "Carl": ["Bob"],
    "Dan": ["Alice", "Bob"]
}
```
Les fonctions principales sont :

- cree_reseau(couples_amis)
Crée un réseau d'amis à partir d'une liste de couples (a, b).

- liste_personnes(reseau)
  - Renvoie la liste des membres du réseau.

- sont_amis(reseau, personne1, personne2)
  - Vérifie si deux personnes sont amies.

- sont_amis_de(reseau, personne, groupe)
  - Vérifie si une personne est amie avec tous les membres d'un groupe.

- est_comu(reseau, groupe)
  - Vérifie si un groupe forme une communauté (clique) : chaque membre est ami avec tous les autres.

- comu(groupe, reseau)
  - Construit une communauté à partir d'un groupe donné, en ne gardant que les personnes qui sont toutes amies entre elles.

- tri_popu(reseau, groupe)
  - Trie les personnes d’un groupe par popularité décroissante (nombre d'amis).

- comu_dans_reseau(reseau)
  - Construit une communauté en considérant tout le réseau, après avoir trié les personnes par popularité.

- comu_dans_amis(personne, reseau)
  - Construit une communauté autour d'une personne donnée, à partir de ses amis triés par popularité.

- comu_max(reseau)
  - Parcourt tout le réseau et renvoie la plus grande communauté trouvée.
