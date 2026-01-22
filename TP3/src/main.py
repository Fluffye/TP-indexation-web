
from ranking import create_dict_ranking
from save_json import save_json

if __name__ == "__main__":
    dict_ranking = create_dict_ranking("chocolate")
    save_json("query.json", dict_ranking)