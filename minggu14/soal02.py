print("List → Set")
n = int(input("Jumlah elemen:"))
list_awal = []
for i in range(n):
    elemen = input(f"  Elemen ke-{i+1}: ")
    list_awal.append(elemen)

set_dari_list = set(list_awal)
print(f"List awal  : {list_awal}")
print(f"Set hasil  : {set_dari_list}")
print(f"Duplikat dihapus: {len(list_awal) - len(set_dari_list)} elemen\n")

print("Set → List")
m = int(input("Jumlah elemen: "))
set_awal = set()
for i in range(m):
    elemen = input(f"  Elemen ke-{i+1}: ")
    set_awal.add(elemen)

list_dari_set = list(set_awal)
print(f"Set awal   : {set_awal}")
print(f"List hasil : {list_dari_set}\n")

print("Tuple → Set")
p = int(input("Jumlah elemen: "))
tuple_awal = []
for i in range(p):
    elemen = input(f"  Elemen ke-{i+1}: ")
    tuple_awal.append(elemen)
tuple_awal = tuple(tuple_awal)

set_dari_tuple = set(tuple_awal)
print(f"Tuple awal : {tuple_awal}")
print(f"Set hasil  : {set_dari_tuple}")
print(f"Duplikat dihapus: {len(tuple_awal) - len(set_dari_tuple)} elemen\n")


print("Set → Tuple")
q = int(input("Jumlah elemen: "))
set_awal2 = set()
for i in range(q):
    elemen = input(f"  Elemen ke-{i+1}: ")
    set_awal2.add(elemen)

tuple_dari_set = tuple(set_awal2)
print(f"Set awal   : {set_awal2}")
print(f"Tuple hasil: {tuple_dari_set}\n")

