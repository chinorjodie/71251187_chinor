import re
import random
import string

def buat_password(length=8):
    karakter = string.ascii_letters + string.digits
    return "".join(random.choice(karakter) for _ in range(length))

def ekstraksi(s):
    emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', s)
    hasil = []
    for i in emails:
        useruput = i.split('@')[0]
        passwer = buat_password()
        hasil.append(f'{i} username: {useruput} password: {passwer}')
    return hasil

teks = "Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari"

nyam = ekstraksi(teks)

for yyi in nyam:
    print(yyi)
