import string

def baca_kata(filename):
    handle = open(filename)  
    kata_set = set()
    for baris in handle:
        baris_bersih = baris.lower()
        for tanda in string.punctuation:
            baris_bersih = baris_bersih.replace(tanda, ' ')
        for kata in baris_bersih.split():
            kata_set.add(kata)
    handle.close()
    return kata_set

filename1 = input("Masukkan nama file pertama : ")
filename2 = input("Masukkan nama file kedua   : ")
try:
    kata_file1 = baca_kata(filename1)
except IOError:
    print(f"Error: File '{filename1}' tidak ditemukan atau tidak bisa dibaca.")
    exit()

try:
    kata_file2 = baca_kata(filename2)
except IOError:
    print(f"Error: File '{filename2}' tidak ditemukan atau tidak bisa dibaca.")
    exit()


print(f"\nKata-kata di '{filename1}' ({len(kata_file1)} kata unik):")
print(sorted(kata_file1))

print(f"\nKata-kata di '{filename2}' ({len(kata_file2)} kata unik):")
print(sorted(kata_file2))

kata_bersama = kata_file1 & kata_file2

print(f"\n{'='*45}")
print(f"Kata yang muncul di KEDUA file ({len(kata_bersama)} kata):")
print(sorted(kata_bersama))
