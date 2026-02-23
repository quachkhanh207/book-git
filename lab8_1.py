def thong_ke_diem():
    so_luong = 0
    tong_diem = 0
    so_dat = 0

    try:
        with open("diem_thi.txt", "r", encoding="utf-8") as f:
            for dong in f:
                dong = dong.strip()
                if dong == "":
                    continue  # bỏ qua dòng trống

                diem = float(dong)
                so_luong += 1
                tong_diem += diem

                if diem >= 5:
                    so_dat += 1

        if so_luong > 0:
            diem_trung_binh = tong_diem / so_luong
        else:
            diem_trung_binh = 0

        with open("thong_ke.txt", "w", encoding="utf-8") as f_out:
            f_out.write(f"So luong sinh vien: {so_luong}\n")
            f_out.write(f"Diem trung binh: {diem_trung_binh:.2f}\n")
            f_out.write(f"So sinh vien dat (>=5): {so_dat}\n")

        print("Da ghi thong ke vao file thong_ke.txt")

    except FileNotFoundError:
        print("Khong tim thay file diem_thi.txt")

thong_ke_diem()
