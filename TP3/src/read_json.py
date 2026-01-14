import json

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return(data)
synonyms = read_json("TP3/input/origin_synonyms.json")
brand_index = read_json("TP3/input/brand_index.json")
origin_index = read_json("TP3/input/origin_index.json")
reviews_index = read_json("TP3/input/reviews_index.json")
title_index = read_json("TP3/input/title_index.json")
description_index = read_json("TP3/input/description_index.json")


def parser_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            data.append(obj)
    return(data)

data = parser_jsonl("TP3/rearranged_products.jsonl")

