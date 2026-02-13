# Input
tinggi = float(input("Masukkan tinggi badan (meter): "))
bmi = float(input("Masukkan BMI yang diharapkan: "))

# Proses
berat = bmi * (tinggi ** 2)

# Output
print("\nBerat badan yang diperlukan adalah:", berat, "kg")