
def data(dataku):
    nim = dataku[1]
    nama = dataku[0]
    alamat =  dataku[2]

    print(f"NIM     : {nim}")
    print(f"Nama    : {nama}")
    print(f"Alamat  : {alamat}\n")

    ambil = nama.split()
    nama_depan = ambil[0]
    print(f"NIM: {tuple(nim)}\n")
    print(f"NAMA DEPAN: {tuple(nama_depan[1:])}\n")
    print(f"NAMA TERBALIK: {tuple(ambil[::-1])}")

datacinoy = ("Benedictina Andhika Chinor Jodie Soesila", "71251187", "Suryowijayan, Mantrijeron")
data(datacinoy)