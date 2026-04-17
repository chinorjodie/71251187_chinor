import re

def hapus_spasi(s):
    s = re.sub(r'\s+', ' ', s).strip()
    return s
    


print(hapus_spasi("saya tidak suka memancing ikan "))