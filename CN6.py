def search_product_by_name(products):
    keyword = input("Nhập từ khóa: ").lower()

    found = False
    for product in products:
        if keyword in product["name"].lower():
            print(product)
            found = True

    if not found:
        print("Không tìm thấy sản phẩm.")