def save_data(products):
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)