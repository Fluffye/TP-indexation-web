import bm25s
from filter_document import augmentation_request_by_synonyms, liste_index, filter_all_doc, filter_doc, verify_presence_token
from read_json import synonyms, data, description_index, title_index, brand_index, origin_index, reviews_index
import math as m
import numpy as np


N = len(data)

avgdl = 0
for page in data:
    avgdl += len(page["description"])   
avgdl = avgdl/N


def frequency_token_document(token, doc):
    freq_token = 0
    if token in description_index and doc in description_index[token]:
        freq_token += len(description_index[token][doc])
    if token in title_index and doc in title_index[token]:
        freq_token += len(title_index[token][doc])
    return freq_token


def document_frequency(token):
    doc_freq = 0
    if token in description_index:
        doc_freq += len(description_index[token])
    if token in title_index:
        doc_freq += len(title_index[token])
    return doc_freq

    
def length_doc(doc):
    for page in data:
        if doc == page["url"]:
            return(len(page["description"]))
        
def bm25_score(query, doc, k1=1.2, b=0.75):
    tokens = augmentation_request_by_synonyms(query)
    score = 0
    dl = length_doc(doc)
    for token in tokens:
        tf = frequency_token_document(token, doc)
        df = document_frequency(token)
        if df == 0: 
            continue
        idf = m.log((N - df + 0.5) / (df + 0.5) + 1)
        score += idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * dl / avgdl))
    return score

def exact_match(query, doc):
    docs = filter_all_doc(query)  # documents contenant tous les tokens
    return 1 if doc in docs else 0



def score_text(query, doc, index, window, max_position):
    tokens = augmentation_request_by_synonyms(query)
    score = 0
    positions = []
    for token in tokens:
        if token in index and doc in index[token]:
            score += 1
            position = index[token][doc]
            positions.extend(position)
            if min(position) < max_position:
                score += 1

    return score


def review(doc):
    total_reviews = reviews_index[doc]['total_reviews']
    mean_mark = reviews_index[doc]['mean_mark']
    last_rating = reviews_index[doc]['last_rating']
    return [total_reviews, mean_mark, last_rating]
    
def score_doc(query, weights, doc):
    
    score = 0
    signals = [
        bm25_score(query, doc),
        exact_match(query, doc),
        score_text(query, doc, title_index, window= 5, max_position=3),
        score_text(query, doc, description_index, window=10, max_position=20),
    ] + review(doc) 
    for w, s in zip(weights, signals):
        score += w * s

    return(np.round(score, 2))