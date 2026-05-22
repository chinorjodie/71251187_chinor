
n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi
print(data_aplikasi)
daftar_aplikasi_set = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_set.append(set(aplikasi))


hasil_semua = daftar_aplikasi_set[0]
for i in range(1, len(daftar_aplikasi_set)):
    hasil_semua = hasil_semua.intersection(daftar_aplikasi_set[i])
print('\nAplikasi yang muncul di SEMUA kategori:')
print(hasil_semua if hasil_semua else '(tidak ada)')


hitung_kemunculan = {}
for nama_kategori, aplikasi in data_aplikasi.items():
    for app in aplikasi:
        if app not in hitung_kemunculan:
            hitung_kemunculan[app] = set()
        hitung_kemunculan[app].add(nama_kategori)  


hanya_satu = {app for app, kat in hitung_kemunculan.items() if len(kat) == 1}
print('\nAplikasi yang hanya muncul di SATU kategori:')
print(hanya_satu if hanya_satu else '(tidak ada)')

if n > 2:
    tepat_dua = {app for app, kat in hitung_kemunculan.items() if len(kat) == 2}
    print('\nAplikasi yang muncul di TEPAT DUA kategori:')
    print(tepat_dua if tepat_dua else '(tidak ada)')