from products_manager import*
FILENAME = "products.json"
products = load_products(FILENAME)
while True:
    print("========== POLYlAP ==========")
    print("1. THÊM SẢN PHẨM")
    print("2. HIỂN THỊ SẢN PHẨM")
    print("3. TÌM SẢM PHẨM")
    print("4. LƯU VÀ THOÁT")

    choice = input(" CHỌN CHỨC NĂNG: ")
    
    if choice == "1":
        add_product(products)
    elif choice == "2":  
        show_products(products)
    elif choice == "3":
        find_product(products)
    elif choice == "4":
        save_products(FILENAME,products)
        print("TẠM BIỆT")
        break
    else:
        print("LỰA CHỌN KHÔNG HỢP LỆ !!!")