fullname = str(input("Masukkan Nama Lengkap Anda: "))
program_studi = str(input("Masukkan Prodi Anda: "))
nilai_huruf = str(input("Masukkan Nilai (dalam Huruf) yang Anda Dapat: "))

try : 
    if nilai_huruf == "A":
        print("Nilai anda adalah 4.0, tbl tbl serem bgt lohh")
    elif nilai_huruf == "A-":
        print("Nilai anda adalah 3.75, kamu keren!")
    elif nilai_huruf == "B+":
        print("Nilai anda adalah 3.0, ayo semangat !!!")
    elif nilai_huruf == "B-":
        print("Nilai anda adalah 2.75, kurang semangat belajar nihh")
    elif nilai_huruf == "C+":
        print("Nilai anda adalah 2.25, kok bisa sihh ??")
    elif nilai_huruf == "C":
        print("Nilai anda adalah 2.0, butuh Aqua ?")
    elif nilai_huruf == "D":
        print("Nilai anda adalah 1, apakah sudah ada pikiran untuk pindah jurusan?")
    elif nilai_huruf == "E":
        print("Nilai anda adalah 0, niat kuliah nggak sih???")
    else:
        print("Inputan nilai yang anda masukkan tidak valid")

except :
    print("Nilai harus dalam bentuk huruf")
