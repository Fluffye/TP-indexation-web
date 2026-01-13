from traitement_url import data
from enregistrer_json import enregistrer_json

def creer_index_review(data):
    index_review = {}
    for dico in data:
        url = dico["url"]
        nb_review = len(dico["product_reviews"])
        if nb_review == 0:
            note = None
            note_total = None
        else:
            note_total = 0
            for review in dico["product_reviews"]:
                note = review["rating"]
                note_total += note
            note_total = note_total/nb_review
        index_review[url] = {"nb_review" : nb_review, "note_total" : note_total, "derniere_note" : note}
    return index_review


index_review = creer_index_review(data)
enregistrer_json("reviews_index.json", index_review)
