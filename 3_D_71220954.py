angka_awal = int(input("Masukkan awal deret: "))
angka_akhir = int(input("Masukkan akhir deret: "))

for deret_angka in range(angka_awal, angka_akhir):
    print(deret_angka, end =" ") if (deret_angka % 6 != 0) and (deret_angka % 8 != 0) else None

# for deret_angka in range(angka_awal, angka_akhir):
#     if (deret_angka % 6 != 0) and (deret_angka % 8 != 0) :
#         print(deret_angka, end =" ")
#     else:
#         None
