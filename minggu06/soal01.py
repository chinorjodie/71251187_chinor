def perkalian_cuy(a, b):
    hasil = 0
    ekspresi = []
    for i in range(a):
        hasil += b
        ekspresi.append(str(b))
    penjumlahan_str = " + ".join(ekspresi)
    print(f"{a} x {b} = {penjumlahan_str} = {hasil}")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

perkalian_cuy(a,b) 
