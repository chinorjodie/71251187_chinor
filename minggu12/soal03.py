import re

def cariwoi(file):
    m = {}
    for l in file:
        emel = re.findall(r"From (\b\S+@\S+\b)", l)
        for i in emel:
            m.update({i : m.get(i, 0) + 1})

    print(m) 
fname = input("Nama File : ")
file = open(fname)
cariwoi(file)