import json

def load_data():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []