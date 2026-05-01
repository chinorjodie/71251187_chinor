file = input("Masukkan nama file: ")
handle = open(file)
for i in handle:
    line= i.strip()
    index = line.split("||")
    question = index[0].strip()
    jawaban = index[1].strip()
    print(question)
    jawab = input("Jawab: ")
    if jawab.lower() == jawaban.lower():
        print("Benar!")
    else:
        print(f"Jawaban salah!")

handle.close()