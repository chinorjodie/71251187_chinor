def apalah(d):
    a = 0
    print("Key     Values    Item")
    for i, j in d.items():
        a += 1
        print(f"{i}       {j}        {a}")

d = dict(eval(input()))
apalah(d)