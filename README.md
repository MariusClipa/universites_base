
Gestion des Universités

Ce projet est une application simple en Python permettant de gérer une bibliothèque d'universités. Elle permet d'ajouter des universités, de visualiser la liste des universités et de mettre à jour leurs notes.

Fonctionnalités : 

- Ajouter une nouvelle université avec ses détails (nom, année de création, ville et note).
- Afficher la liste des universités disponibles dans la bibliothèque.
- Mettre à jour la note d'une université spécifique.
- Calculer la note moyenne d'une université lorsqu'une nouvelle note est ajoutée.

Structure du Projet : 

Le projet est contruit avec l'architecture MVC (model view controller). Le projet est organisé en plusieurs fichiers pour séparer les différentes responsabilités :

Bibliotheque_universites.py : Contient la classe BibliothequeUniversite qui gère la liste des universités et leurs opérations.
class_universite.py : Définit la classe Universite avec ses propriétés et méthodes.
controler_universite.py : Gère la logique métier, comme la création des objets et l'interaction avec la bibliothèque.
main.py (ou équivalent) : Le fichier principal contenant une boucle interactive pour interagir avec l'utilisateur.

Exemple d'Utilisation : 

Voici un exemple des actions possibles avec le programme :

Ajouter une université :
- Nom : Université Lyon 3
- Année : 1875
- Ville : Lyon
- Note : 10
  
Afficher toutes les universités : Affiche une liste formatée des universités avec leurs détails.

Mettre à jour une note :
- Nom de l'université : Université Lyon 3
- Nouvelle note : 9.0
La nouvelle note moyenne sera automatiquement calculée.
