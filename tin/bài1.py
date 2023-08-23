def main():
    while True:
        try:
            chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: "))
            chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))
            
            if chieu_dai > chieu_rong:
                break
            else:
                print("Lỗi: Chiều dài phải lớn hơn hoặc bằng chiều rộng. Vui lòng nhập lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ.")

    chu_vi = 2 * (chieu_dai + chieu_rong)
    dien_tich = chieu_dai * chieu_rong

    print(f"Chu vi của hình chữ nhật là: {chu_vi}")
    print(f"Diện tích của hình chữ nhật là: {dien_tich}")

if __name__ == "__main__":
    main()
    
str(9)





