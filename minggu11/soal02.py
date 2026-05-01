
def berhenti(angka):
    result = []

    for i in angka:
        if i != "done":
            result.append(float(i))
    if result:
        rata2 = sum(result) / len(result)
        return result, rata2
    else:
        return result, None

angka = []
while True:
    user_input = input("Masukkan angka (ketik 'done' untuk berhenti): ")
    
    angka.append(user_input)

    if user_input == "done":
        break
hasil, avg = berhenti(angka)
if avg is not None:
    print(f"List: {hasil}")
    print(f"Average: {avg}")