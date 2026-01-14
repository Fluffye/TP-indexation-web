from tokenization import clean_text
from read_json import synonyms, data, description_index, title_index, brand_index, origin_index

def augmentation_request_by_synonyms(request):
    tokens = clean_text(request)
    for token in tokens:
        for key, value in synonyms.items():
            if token in value:
                tokens.append(key)
                # We replace the token for the request on all tokens
                tokens.remove(token)

        
    return tokens

def verify_presence_token(index, documents, token):
    if token in index.keys():
        for doc in index[token]:
            if doc not in documents:
                documents.append(doc)
    return(documents)

def verify_presence_all_tokens(tokens):
    dico = {}
    for token in tokens:
        documents = []
        for index in liste_index:
            documents = verify_presence_token(index, documents, token)

        dico[token] = set(documents)

    set1 = dico[token]
    for value in dico.values():
        set1 = set1.intersection(value)
    return(set1)


    

liste_index = [brand_index, description_index, origin_index, title_index]


def filter_doc(request):
    tokens = augmentation_request_by_synonyms(request)
    documents = []
    for token in tokens:
        for index in liste_index:
            documents = verify_presence_token(index, documents, token)
    return documents



def filter_all_doc(request):
    tokens = augmentation_request_by_synonyms(request)
    documents = verify_presence_all_tokens(tokens)
    return(documents)

# print(filter_all_doc("box chocolate america"))




