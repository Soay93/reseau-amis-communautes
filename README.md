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
