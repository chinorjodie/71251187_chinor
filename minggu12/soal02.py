def menggabung(a,b):
    nyaw = {}
    if len(a) == len(b):
        for i in range(len(a)):
            nyaw[a[i]] = b[i]
        print(nyaw)
    else:
        print("List Harus Sama Panjang!")

list1 = eval(input())
list2 = eval(input())
menggabung(list1,list2)