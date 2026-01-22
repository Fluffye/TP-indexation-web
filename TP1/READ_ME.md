
# TP1-- Développement d'un web crawler

## Objectif
Créer un crawler en python qui explore les pages d’un site web en priorisant certaines pages.

## Utilisation

Fonction prenant en entrée un url et le nombre de documents maximus à récupérer, modifiable dans le fichier config.
Et produit en sortie un fichier JSON contenant pour chaque page : 
•Titre 
•URL 
•Premier paragraphe 
•Liste des liens pertinents 

## Installation

Créer et activer l'environnement virtuel

```python
cd TP1
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