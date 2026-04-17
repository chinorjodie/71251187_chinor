import re

def perbandingan(s):
    huruf = re.findall(r'\b\w+\b', s)
    minimum = min(huruf, key=len)
    maksimum = max(huruf, key=len)
    return f"terpendek : {minimum}, terpanjang : {maksimum}"
    
    


print(perbandingan("red snakes and a black frog in the pool"))
        
