
from filter_document import filter_doc
from read_json import data
from algo_scoring import score_doc, review
import math as m
import numpy as np

weights = [30, 30, 20, 5, 1, 10, 5] 

# Function to find a page in rearranged_products with it's URL
def get_document_by_url(url):
    for doc in data:
        if doc["url"] == url:
            return doc
    return None


def ranking(query, docs, weights = weights):

    seen_titles = set()

    ranking_list = []
    for doc in docs:
        page = get_document_by_url(doc)
        title = page['title'].split("-")[0] # We get the title without it's variant

        if title in seen_titles:
            continue  # we ignore the variant of a page already there
        seen_titles.add(title)


        score = score_doc(query, weights, doc)

        description = page['description']
        dict = {"title" : title, "url" : doc, "description" : description, "score" : score}
        ranking_list.append(dict)

        ranking_list = sorted(
            ranking_list,
            key=lambda x: x["score"],
            reverse=True
        )
    return ranking_list

# Creation of a dictionary with the metadata and results from a query
def create_dict_ranking(query, weights = weights):
    docs = filter_doc(query)

    nb_docs_total = len(data)
    nb_docs_filtered = len(docs)
    metadata = {"nb_docs_total" : nb_docs_total, "nb_docs_filtered" : nb_docs_filtered}

    results = ranking(query, docs)

    dict = {"query" : query, "metadata" : metadata, "results" : results}

    return dict






