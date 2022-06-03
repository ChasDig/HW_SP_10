import requests


def candidates_list():  # loads a dictionary with information about candidates in json file
    """
    :return: load_json_candidates: json file with data about candidates
    """

    load_candidates = requests.get("https://jsonkeeper.com/b/E6FT")
    load_json_candidates = load_candidates.json()

    return load_json_candidates
