def deret_ribet(tinggi, lebar):
    angka = 1
    for i in range(tinggi): 
        for j in range(lebar):
            print(angka, end = " ")
            angka += 1
        print()

tinggi = int(input("tinggi: "))
lebar = int(input("lebar: "))

deret_ribet(tinggi,lebar)







