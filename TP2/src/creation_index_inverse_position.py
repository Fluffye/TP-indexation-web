import nltk
import string
from nltk.corpus import stopwords
from TP2.src.treatement_url import data
from save_json import save_json


nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_texte(text):
    text = "".join([char for char in text if char not in string.punctuation])
    tokens = text.split(" ")
    clean = [word for word in tokens if word not in stop_words]
    return(clean)

def create_index_title_position(data):
    index_title = {}
    for dico in data:
        url = dico["url"]
        mots_title = clean_texte(dico["title"])
        for i in range (len(mots_title)):
            if mots_title[i] in index_title.keys():
                index_title[mots_title[i]].append((url, i))
            else:
                index_title[mots_title[i]] = [(url, i)]
    return(index_title)

index_title = create_index_title_position(data)
save_json("title_index.json", index_title)

def create_index_description_position(data):
    index_description = {}
    for dico in data:
        url = dico["url"]
        mots_description = clean_text(dico["description"])
        for i in range(len(mots_description)):
            if mots_description[i] in index_description.keys():
                index_description[mots_description[i]].append((url, i))
            else:
                index_description[mots_description[i]] = [(url, i)]
    return(index_description)

index_description = create_index_description_position(data)
save_json("description_index.json", index_description)