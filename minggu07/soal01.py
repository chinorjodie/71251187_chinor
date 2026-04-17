n = int(input("input n = "))

def bilangan_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def cari_woy(n):
    for i in range (n - 1, 1, -1):
        if bilangan_prima(i):
            return i
    return None

hasil = cari_woy(n)

if hasil:
    print(f"maka prima terdekat < {n} adalah {hasil} ")
else:
    print("Tidak ada bilangan prima di bawah", n)   
