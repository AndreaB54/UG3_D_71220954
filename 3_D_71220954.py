#input angka
angka_awal = int(input("Masukkan awal deret: "))
angka_akhir = int(input("Masukkan akhir deret: "))

#proses perulangan + ternary operator
for deret_angka in range(angka_awal, angka_akhir):
    print(deret_angka, end =" ") if (deret_angka % 6 != 0) and (deret_angka % 8 != 0) else None