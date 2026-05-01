def buka_file(nama_file):
    with open(nama_file, encoding='utf-8') as handle:
        baris = handle.readlines()
    return baris

def bandingkan_file(file1,file2):
    baris1 = buka_file(file1)
    baris2 = buka_file(file2)

    jumlah_baris = max(len(baris1), len(baris2))
    print(f"File 1 : {len(baris1)} baris")
    print(f"File 2 : {len(baris2)} baris")

    beda_cuy = False

    for i in range(jumlah_baris):
        if i < len(baris1):
            isi1 = baris1[i].rstrip()
        else:
            isi1 = "BARIS TIDAK ADA"
        
        if i < len(baris2):
            isi2 = baris2[i].rstrip()   
        else:
            isi2 = "BARIS TIDAK ADA"

        if isi1 != isi2:
            beda_cuy = True
            print(f"Baris {i+1} berbeda:")
            print(f" < {file1}: {isi1}")
            print(f" > {file2}: {isi2}")
            print()

    if not beda_cuy:
        print("File 1 dan File 2 sama persis.")
    
if __name__ == "__main__":
    try:
        file1 = input("File 1 : ")
        file2 = input("File 2 : ")
        bandingkan_file(file1, file2)
    except FileNotFoundError as e:
        print(f"File tidak ditemukan: {e}")

