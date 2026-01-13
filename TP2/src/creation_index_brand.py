from traitement_url import data
from save_json import save_json


def create_index_brand(data):
    index_brands = {}
    for dico in data:
        url = dico["url"]
        if "brand" in dico["product_features"].keys():
            brand = dico["product_features"]["brand"]
            if brand in index_brands.keys():
                index_brands[brand].append(url)
            else:
                index_brands[brand] = [url]
    return(index_brands)

index_brands = create_index_brand(data)
print(index_brands.keys())
save_json("brand_index.json", index_brands)



#['material', 'flavors', 'sizes', 'brand', 'care instructions', 'purpose', 'flavor', 'caffeine_content', 'sugar_content', 'care_instructions', 'container', 'light', 'closure', 'comfort', 'durability', 'colors', 'safety', 'made in', 'design', 'size', 'versatility', 'season', 'traction', 'fit', 'heel'])