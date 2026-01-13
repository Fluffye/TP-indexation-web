import nltk
import string
from nltk.corpus import stopwords
from traitement_url import data
from save_json import save_json


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def nettoyer_texte(text):
    text = "".join([char for char in text if char not in string.punctuation])
    tokens = text.split(" ")
    clean = [word for word in tokens if word not in stop_words]
    return(clean)

def create_index_title(data):
    index_title = {}
    for dico in data:
        url = dico["url"]
        mots_title = nettoyer_texte(dico["title"])
        for mot in mots_title:
            if mot in index_title.keys():
                index_title[mot].append(url)
            else:
                index_title[mot] = [url]
    return(index_title)

index_title = create_index_title(data)
save_json("title_index.json", index_title)

def create_index_description(data):
    index_description = {}
    for dico in data:
        url = dico["url"]
        mots_description = nettoyer_texte(dico["description"])
        for mot in mots_description:
            if mot in index_description.keys():
                index_description[mot].append(url)
            else:
                index_description[mot] = [url]
    return(index_description)

index_description = create_index_description(data)
save_json("description_index.json", index_description)