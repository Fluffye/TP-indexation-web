import json
from urllib.parse import urlparse

def parser_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            data.append(obj)
    return(data)

def extract_id_url(url):
    parsed_url = urlparse(url)
    id = parsed_url.path.split("/")[-1]
    return(id)

def extract_variant_url(url):
    parsed_url = urlparse(url)
    if len(parsed_url.query) != 0 :
        variant = parsed_url.query.split("=")[-1]
    else:
        variant = None
    return(variant)

def add_infos_ligne(dico):
    url = dico['url']
    parsed_url = urlparse(url)
    if parsed_url.path.split("/")[1] == "product":
        dico["product_id"] = extract_id_url(url)
        dico["variant"] = extract_variant_url(url)
    return(dico)
 
def add_infos_data(data):
    data_ameliorer = []
    for i, dico in enumerate(data):
        dico['id'] = i
        data_ameliorer.append(add_infos_ligne(dico))

    return(data_ameliorer)



data_brute = parser_jsonl("TP2/input/products.jsonl")
data = add_infos_data(data_brute)
