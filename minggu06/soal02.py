def ganjil_cuy(bawah,atas):
    hasil = []
    if bawah < atas:
        ket_1 = "dari kecil ke besar"
        ket_2 = "bawah < atas"
        for i in range(bawah, atas + 1):
            if i % 2 == 1:
                hasil.append(str(i))
    elif bawah > atas:
        ket_1 = "dari besar ke kecil"
        ket_2 = "bawah > atas"
        for i in range(bawah, atas - 1, -1):
            if i % 2 == 1 :
                hasil.append(str(i))
    else:
        print(f"bawah = {bawah}, atas = {atas}. Karena bawah = atas, tidak ada bilangan ganjil di antara.")
        return

    if hasil:
        print(f"bawah = {bawah}, atas = {atas}. Karena {ket_2}, berarti {ket_1}, maka hasilnya adalah: {', '.join(hasil)}")

bawah = int(input("bawah = "))
atas = int(input("atas = "))

ganjil_cuy(bawah,atas) 
