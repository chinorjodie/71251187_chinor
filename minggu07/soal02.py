def fak(n):
    hasil = 1
    for i in range(1, n+ 1):
        hasil *= i
    return hasil

def deret_cuy(n):
    for i in range(n, 0, -1):
        print(fak(i), end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print( )

n = int(input("n =  "))

deret_cuy(n)
