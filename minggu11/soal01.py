def cari_bilangan_terbesar(angka):
    if len(angka) < 3:
        raise ValueError("List harus memiliki minimal 3 elemen")
    unik = list(set(angka))

    if len(unik) < 3:
        raise ValueError("List harus memiliki minimal 3 elemen unik")
    unik.sort(reverse = True)
    return unik[0:3]

if __name__ == "__main__":
    angka = list(map(int, input().split()))
    hasil = cari_bilangan_terbesar(angka)
    print(hasil)
