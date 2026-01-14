import bm25s
from filter_document import augmentation_request_by_synonyms, liste_index
from read_json import synonyms, data, description_index, title_index, brand_index, origin_index
import math as m
# donner plus de poids à ce qui est dans features et dans le titre, prendre les avis en compte, 
N = len(data)

avgdl = 0
for page in data:
    avgdl += page["description"]
avgdl = avgdl/N


def frequency_token_document(token, doc):
    if token in description_index:
        freq_token = len(description_index[token][doc])
    if token in title_index:
        freq_token += len(title_index[token][doc])

def document_frequency(token):
    if token in description_index:
        doc_freq = len(description_index[token])
    if token in title_index:
        doc_freq += len(title_index[token])
    
def lenght_doc(doc):
    for page in data:
        if doc == page["url"]:
            return(len(page["description"]))
        

        


def bm25_score(query, doc, k1 = 1.2, b = 0.75):
    tokens = augmentation_request_by_synonyms(query)
    sum = 0
    for token in tokens:
        tf = frequency_token_document(token, doc)
        df = document_frequency(token)
        dl = lenght_doc(doc)

        idf = m.log((N - df + 0.5) / (df + 0.5) + 1)
        sum += idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * dl / avgdl))

    return(sum)







