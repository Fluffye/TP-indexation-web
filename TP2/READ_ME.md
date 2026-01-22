
# TP2 – Indexation Web

## Objectif
Créer différents types d’index à partir d’un jeu de données produits e-commerce afin de préparer la construction d’un moteur de recherche.

---

## Structure du projet

```text
TP2/
├── input/                   # Fichiers JSONL d’entrée (produits)
├── output/                  # Index JSON générés
├── src/                     # Scripts Python
│   ├── creation_index_brand.py
│   ├── creation_index_origin.py
│   ├── creation_index_inverse.py
│   ├── creation_index_inverse_position.py
│   ├── creation_index_review.py
│   ├── treatement_url.py
│   └── save_json.py
├── README.md
└── TP2 Indexation web ENSAI 2025.pdf
```

## Input

Le jeu de données fourni est un fichier **JSONL** contenant 150 documents. Chaque ligne correspond à un produit et contient les champs suivants :

- `URL`  
- `Title` (titre du produit)  
- `Description` (description textuelle)  
- `Features` (marque, origine, etc.)  
- `Reviews` (liste des notes et commentaires)  
- `Links` (liens internes et externes)


A partir de ce fichier, l'url et le variant s'il existe est extrait. L'url servira d'id pour chaque page dans la suite du TP

---

## Output

### Index inversé pour les titres et les documents

A partir du json d'entrée, on parcourt tous les titres/documents. Pour chaque texte récupéré, on tokenise en séparant chaque mot au niveau des espaces. Puis on retire les stop words et la ponctuation. On parcourt ensuite chaque mot, chaque mot est ajouté à l'index comme clé d'un dictionnaire et l'url du document où il se trouve est ajouté en valeur comme liste de'url.

Les index inversé sont renvoyés sous la forme d'un fichier json au format:

```json
{
  "token1": ["url1", "url2", "url3"],
  "token2": ["url2", "url5"]
}
```

Ces fichiers json ont été remplacé par ceux avec positions dans output

### Index des reviews

ON parcourt le json d'entrée. Pour chaque document, l'url du document est associé comme clé d'un dictionnaire à l'index, la valeur du dictionnaire est un autre dictionnaire ayant comme clé : nb_reviexs, rating, derniere_note. Les notes étant déjà trié par ordre chronologique, la dernière note des reviex est renvoyé pour cette dernière catégorie.

Pour les page ne comprenant pas de reviews, None est renvoyé.

L'index des reviews sont renvoyés sous la forme d'un fichier json au format:

```json
{
  "url1": {
    "nb_reviews": 10,
    "total_score": 4.5,
    "last_score": 5
  }
}

```

Cet index est le fichier json reviews_index dans output

### Index inversé pour les features

A partir du json d'entrée, pour chaque document comprenant la feature recherché dans product_feature, chaque type de cette feature est ajouté à l'index comme clé d'un dictionnaire et l'url du document où il se trouve est ajouté en valeur comme liste de'url.

Les index inversé sont renvoyés sous la forme d'un fichier json au format:

```json
{
  "BrandX": ["url1", "url3"],
  "BrandY": ["url2", "url5"]
}

Ces indexs ont été créé pour l'origine et la marque.

```
Ces index sont les fichiers brand_index.json et origin_index.json dans output

### Index inversé pour les titres et les documents avec position

A partir du json d'entrée, on parcourt tous les titres/documents. Pour chaque texte récupéré, on tokenise en séparant chaque mot au niveau des espaces. Puis on retire les stop words et la ponctuation. On parcourt ensuite chaque mot, chaque mot est ajouté à l'index comme clé d'un dictionnaire. Ce dictionnaire a comme valeur un autre dictionnaire ayant comme clé l'url du document contenant le mot, et comme valeur la liste de position ou se trouve le mot dans le document.

Les index inversé sont renvoyés sous la forme d'un fichier json au format:

```json
{
  "token1": {
    "url1": [0, 3],
    "url2": [2]
  },
  "token2": {
    "url2": [1, 5]
  }
}

```

Ces index sont les fichiers description_index.json et title_index.json dans output



## Installation

Créer et activer l'environnement virtuel

```python
cd TP2
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

## Exemples d’utilisation

Ce qui suit montre comment utiliser les fonctions pour créer et sauvegarder les différents types d’index à partir des données de produits.

```python
# Import des fonctions depuis les modules
from creation_index_inverse import create_index_inverse
from creation_index_inverse_position import create_index_inverse_position
from creation_index_review import create_index_review
from creation_index_brand import create_index_brand
from creation_index_origin import create_index_origin
from save_json import save_json
from treatement_url import data  # variable contenant la liste des produits

# -----------------------------
# 1. Index inversé avec positions pour le titre
# -----------------------------
index_title = create_index_inverse_position(data, field="title")
# Exemple de vérification : afficher les positions du mot "coffee"
print(index_title.get("coffee", {}))
# Sauvegarde
save_json("output/index_title_positions.json", index_title)

# -----------------------------
# 2. Index inversé avec positions pour la description
# -----------------------------
index_description = create_index_inverse_position(data, field="description")
# Exemple de vérification
print(index_description.get("organic", {}))
# Sauvegarde
save_json("output/index_description_positions.json", index_description)

# -----------------------------
# 3. Index des features : marques
# -----------------------------
index_brands = create_index_brand(data)
# Vérification
print(list(index_brands.keys())[:5])
# Sauvegarde
save_json("output/index_brands.json", index_brands)

# -----------------------------
# 4. Index des features : origine
# -----------------------------
index_origin = create_index_origin(data)
# Vérification
print(list(index_origin.keys())[:5])
# Sauvegarde
save_json("output/index_origin.json", index_origin)

# -----------------------------
# 5. Index des reviews
# -----------------------------
index_reviews = create_index_review(data)
# Vérification
print(list(index_reviews.items())[:3])  # afficher 3 premières entrées
# Sauvegarde
save_json("output/index_reviews.json", index_reviews)
```