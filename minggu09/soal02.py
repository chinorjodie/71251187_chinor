import re

def hitung_word(s, target):
    huruf = re.findall(r'\b' + re.escape(target) + r'\b', s, re.IGNORECASE)
    return len(huruf)
sentences = input()
cari = input()

print(f"{cari} ada {hitung_word(sentences, cari)} buah")