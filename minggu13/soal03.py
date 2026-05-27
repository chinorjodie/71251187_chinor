import re
fname = input("Enter a file name: ")
fopen = open(fname)


hitung = {}

for i in fopen:
    if not i.startswith("From "):
        continue
    ambil = re.findall(r"(\d{2}):\d{2}:\d{2}", i)
    jam = ambil[0]
    if jam not in hitung:
        hitung[jam] = 1
    else:
       hitung[jam] += 1 

for jam in sorted(hitung):
    print(jam, hitung[jam])