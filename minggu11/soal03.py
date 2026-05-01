import re

def ambil_kata_unik(beritaw):
    with open(beritaw, encoding='utf-8') as f:
        isi = f.read()
    semua = re.findall(r'[^\s]+', isi)
    uniklu = list(dict.fromkeys(semua))
    return isi, uniklu


if __name__ == "__main__":
    beritaw = input("Masukkan nama file txt: ")
    isi_berita, kata_unik = ambil_kata_unik(beritaw)
    print("======= ISI BERITA =======")
    print(isi_berita)
    print("======= KATA UNIK PADA BERITA =======")
    print(kata_unik)