from menu.function import read_csv, count_user_id, username_unik, validasi_username, validasi_input
import menu.cipher

def register(user):
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    id = str(count_user_id(user))
    role = "user"
    saldo = "0"

    if username_unik(username,user) == False:
        print("Username "+username+" sudah terpakai, silakan menggunakan username lain.")
    elif validasi_username(username) == False:
        print("Username hanya boleh mengandung huruf kecil(a-z), huruf besar(A-Z), angka 0-9, '-', dan '_'")
    elif validasi_input(nama) == False or validasi_input(password) == False:
        print("Input tidak boleh mengandung ';'")
    else:
        L = [id,username,nama,menu.cipher.cipher(password, False),role,saldo]
        user += [L]
        print("Username "+username+" telah berhasil register ke dalam binomo.")
    return