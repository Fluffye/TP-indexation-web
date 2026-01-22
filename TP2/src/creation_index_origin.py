from treatement_url import data
from save_json import save_json


def create_index_origin(data):
    index_origins = {}
    for dico in data:
        url = dico["url"]
        if "made in" in dico["product_features"].keys():
            origin = dico["product_features"]["made in"]
            if origin in index_origins.keys():
                index_origins[origin].append(url)
            else:
                index_origins[origin] = [url]
    return(index_origins)

index_origins = create_index_origin(data)
print(index_origins.keys())
save_json("origin_index.json", index_origins)



#['material', 'flavors', 'sizes', 'brand', 'care instructions', 'purpose', 'flavor', 'caffeine_content', 'sugar_content', 'care_instructions', 'container', 'light', 'closure', 'comfort', 'durability', 'colors', 'safety', 'made in', 'design', 'size', 'versatility', 'season', 'traction', 'fit', 'heel'])