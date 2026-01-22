# TP3 - Moteur de recherche


## Objectif
Développer un moteur de recherche qui utilise les index créés précédemment pour retourner et 
classer des résultats pertinents.

## Input

Le jeu de données fourni est un fichier **JSONL** contenant 150 documents. Chaque ligne correspond à un produit et contient les champs suivants :

- `URL`  
- `Title` (titre du produit)  
- `Description` (description textuelle)  
- `Features` (marque, origine, etc.)  
- `Reviews` (liste des notes et commentaires)  
- `Links` (liens internes et externes)

## Output

Objet Json contenant :
 - query : la requête
 - metadata : dictionnaire ayant comme clé :
    - nb_total_docs - le nombre total de documents dans la base de données
    - nb_docs_filtered - le nombre de document ayant passé le premier filtre de la recherche
- results : liste des documents classés par score avec pour chaque document:
    - title : le titre du produit
    - url : l’URL du produit
    - description : description textuelle du produit
    - score : score de pertinence calculé pour la requête


## Fonctionnement 

Pour chaque reqûete, on supprime la ponctuation, transforme le texte en minuscule, supprime les stop words, sépare chaque mot au niveau des espaces et remplace certains mot de pays par leur synonyme selon le dictionnaire origin_synonyms pour simplifier la recherche. Les mots sont remplacés et non ajouter pour permettre une meilleure recherche sur tous les termes.

A partir de la requête, les documents contenant au moins un mot de la requête sont filtrés.
Un score est ensuite calculé selon plusieurs signaux, chaque signaux a un poid différent.
On ne récupère qu'un variant pour chaque page, pour éviter trop de répétitions.
Les résultats avec les méta données sont ensuite enregistré dans un json.

Un fichier test a été créé pour comparer les résultats pour différents types de query selon les poids.

## Signaux utilisés

- Score bm25
- Présence ou non d'un match exact entre les mots dans la requête et les mots dans les pages
- Présence des mots de la reqûete dans le titre de la page, avec bonus s'ils sont présents en début de texte
- Présence des mots de la reqûete dans la description de la page, avec bonus s'ils sont présents en début de texte
- Nombre de reviews de la page
- Note moyenne
- Dernière note

## Observation

 Les couleurs ou origin peuvent cependant induire en erreur la recherche en faisant ressortir des pages de la bonne origine mais n'ayant rien à voir avec la recherche. Cela est particulièrement vrai avec des longues recherchers. Ils seraient pertinent de reduire l'influence des mots dans la feature origins. On remarque qu'un fort impact du titre aide également à réduire ce problème et a mieux cibler les pages, et est donc plus pertinent que la présence de mot dans la description.
 Le score bm25 permet également d'amléiorer les résultats du rankong en évaluant la pertinence textuelle.
 La recherche par mot exact est particulièrement efficace pour trier, mais ne marche réellement qu'en cas de requête assez courte et bien orthographié.
 Puisque les variantes ont été retiré, les reviews n'ont pas un impact très fort sur la pertinence de la requête.



## Installation

Créer et activer l'environnement virtuel

```python
cd TP3
.\.venv\Scripts\Activate.ps1                                                      

```

Installer les dépendances

```python

pip install -r requirements.txt

```

Lancer le programme

```python

python src/main.py

``` 