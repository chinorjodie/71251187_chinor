def sama(tA):
    n = set(tA)
    if len(n) == 1:
        return True
    else:
        return False
    
tA = eval(input("tA= "))
print(sama(tA))