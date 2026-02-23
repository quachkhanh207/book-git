def display_all_products(products):
    if not products:
        print("Kho hàng trống.")
        return

    for product in products:
        print("------------------------")
        print("ID:", product["id"])
        print("Tên:", product["name"])
        print("Hãng:", product["brand"])
        print("Giá:", product["price"])
        print("Số lượng:", product["quantity"])