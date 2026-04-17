import re
# hi.strftime('%d-%m-%Y')
from datetime import datetime
def hai(s):
    baca = re.findall(r'\d{4}-\d{2}-\d{2}', s)
    hari_ini = datetime.now()
    hasil = []
    for i in baca:
        hi = datetime.strptime(i, '%Y-%m-%d')
        selisih = (hari_ini - hi).days
        mantap = hi.strftime('%d-%m-%Y')
        hasil.append(f'{mantap} {hi.time()} selisih {selisih} hari')

    return hasil

text = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."

for j in hai(text):
    print(j)

