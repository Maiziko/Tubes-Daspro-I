from menu.function import length
import menu.cipher
def login(a,e): # fungsi yang digunakan untuk login dengan parameter a sebagai array dari user dan e sebagai array dari active_user 
    username = input("Masukkan username : ")
    password = input("Masukkan Password : ")
    temp = False
    idx = 0
    for i in range(length(a)) : 
        if a[i][1] == username and menu.cipher.cipher(a[i][3], True) == password : # Jika username benar dan password benar maka password akan di chipper atau pasword yang masuk ke database yang ditampilkan bukan pasword sebenar.__doc__
            e += a[i] # username dan pasword di simpan ke dalam array yang akan digunakan untuk login 
            idx = i
            temp = True 
    if temp == True :
        print("Halo "+a[idx][2]+"! Selamat datang di “Binomo”!")  
    else :
        print("Password atau username salah atau tidak ditemukan.") 