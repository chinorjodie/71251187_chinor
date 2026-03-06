def digit_belakang(x,y,z): 
    x = x % 10  
    y = y % 10 
    z = z % 10 
    if x == y or x == z or y == z: 
        return True 
    else: 
        return False 

a = int(input("Masukkan bilangan pertama: ")) 
b = int(input("Masukkan bilangan kedua: ")) 
c = int(input("Masukkan bilangan ketiga: ")) 
hasil = digit_belakang(a,b,c) 
print ("Hasil:", hasil) 
