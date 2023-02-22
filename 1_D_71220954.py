#Input
curah_hujan = float(input("Masukkan nilai curah hujan : "))

#Ternary Operator
print("Cuaca Terang/Berawan") if curah_hujan == 0 else print("Curah hujan ringan") if curah_hujan >= 0.5 and curah_hujan <= 20 else print("Curah hujan sedang") if curah_hujan >= 21 and curah_hujan <= 50 else print("Curah hujan lebat") if curah_hujan >= 51 and curah_hujan <= 100 else print("Curah hujan ekstrem") if curah_hujan > 100 else print("Periksa nilai curah hujan anda kembali")