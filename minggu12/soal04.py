import re

def carilagi(file):
    m = {}
    for l in file:
        em = re.findall(r"From \b\S+@(\S+\b)", l)
        for i in em:
            m.update({i : m.get(i, 0) + 1})

    print(m)
 
fname = input("Nama File : ")
file = open(fname)
carilagi(file)