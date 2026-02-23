def delete_product(products):
    product_id = input("Nhập ID cần xóa: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Đã xóa.")
            return

    print("Không tìm thấy sản phẩm.")