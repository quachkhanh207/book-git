def update_product(products):
    product_id = input("Nhập ID cần sửa: ")

    for product in products:
        if product["id"] == product_id:
            product["name"] = input("Tên mới: ")
            product["brand"] = input("Thương hiệu mới: ")
            product["price"] = int(input("Giá mới: "))
            product["quantity"] = int(input("Số lượng mới: "))
            print("Cập nhật thành công!")
            return
    
    print("Không tìm thấy sản phẩm.")