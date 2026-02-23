def add_product(products):
    new_id = f"LT{len(products)+1:02d}"

    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    quantity = int(input("Nhập số lượng: "))

    product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Thêm sản phẩm thành công!")
    return products