a = input("Masukkan sisi:")
b = input("Masukkan sisi:")
c = input("Masukkan sisi:")

try:
    a = int(a)
    b = int(b)
    c = int(c)

    if a == b and b ==c:
        print("3 sisi sama")
    elif a ==b or b ==c or a == c:
        print("2 sisi sama")
    elif a!=b and b!= c and a!=c:
        print("Tidak ada yang sama")

except:
    print("Input tidak valid. Harap masukkan angka.")