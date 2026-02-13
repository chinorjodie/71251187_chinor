
# Input
gaji_per_jam = float(input("Masukkan gaji per jam: "))
jam_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))

# Proses
minggu = 5

# 1. Pendapatan sebelum pajak
pendapatan_kotor = gaji_per_jam * jam_per_minggu * minggu

# 2. Pajak 14%
pajak = 0.14 * pendapatan_kotor
pendapatan_bersih = pendapatan_kotor - pajak

# 3. Pengeluaran setelah pajak
baju_aksesoris = 0.10 * pendapatan_bersih
alat_tulis = 0.01 * pendapatan_bersih

# Sisa setelah belanja
sisa_uang = pendapatan_bersih - baju_aksesoris - alat_tulis

# 4. Sedekah 25% dari sisa
sedekah = 0.25 * sisa_uang

# 5. Pembagian sedekah
anak_yatim = 0.30 * sedekah
kaum_dhuafa = 0.70 * sedekah

# Output
print("\n--- HASIL PERHITUNGAN ---")
print("1. Pendapatan sebelum pajak: Rp", pendapatan_kotor)
print("2. Pendapatan setelah pajak: Rp", pendapatan_bersih)
print("3. Uang untuk baju & aksesoris: Rp", baju_aksesoris)
print("4. Uang untuk alat tulis: Rp", alat_tulis)
print("5. Jumlah uang yang disedekahkan: Rp", sedekah)
print("6. Untuk anak yatim: Rp", anak_yatim)
print("7. Untuk kaum dhuafa: Rp", kaum_dhuafa)
