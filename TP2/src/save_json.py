import json
import os

def save_json(nom, data):
    path = os.path.join("TP2/output", nom)
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)