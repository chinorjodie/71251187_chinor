def ips_lu():
    jumlah_mk = int(input("Berapa jumlah mata kuliah? "))
    total_sks = jumlah_mk * 3
    total_nilai = 0
    
    for i in range (1, jumlah_mk + 1):
        nilai = input(f"Nilai MK {i}: ")

        if nilai =="A":
            bobot = 4
        elif nilai == "B":
            bobot = 3
        elif nilai == "C":
            bobot = 2
        elif nilai == "D":
            bobot = 1
        else:
            pass
        total_nilai += bobot * 3

    ips = total_nilai/total_sks
    print(f"IPS Anda semester ini {ips:.2f}")

ips_lu()