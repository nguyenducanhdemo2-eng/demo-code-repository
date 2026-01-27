# FILE NÀY NƠI CHỨA CÁC HÀM DỮ LIỆU  THÊM , TÌM  , LƯU ,...
import json 
def load_products(filename):# tải chương trình từ file máy tính lên
    try: # ngăn chương trình không bị carsh
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return[]
def save_products(filename, products):
    with open(filename, "w", encoding="utf-8")as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
def add_product(products):
    print("=== THÊM SẢN PHẨM ===")
    product = {
        "id": int(input("NHẬP MÃ SẢN PHẨM: ")),
        "name": input("NHẬP TÊN SẢN PHẨM: "),
        "brand": input("NHẬP THƯƠNG HIỆU: "),
        "price": int(input("NHẬP GIÁ: ")),
        "quantity": int(input("NHẬP SỐ LƯỢNG: "))
    }
    products.append(product)
    print("ĐÃ THÊM SẢN PHẨM")
def show_products(products):
    print("---------- DANH SÁCH SẢN PHẨM ----------")
    if len(products) == 0:
        print(" KHO ĐANG TRỐNG")
    else:
        for p in products:
            print(p)
def find_product(products):
    code =int( input("NHẬP MÃ SẢN PHẨM CẦN TÌM : "))
    for p in products:
        if p["id"] == code:
            print(p)
            return
    print("TÌM KHÔNG THẤY")

    