import menu # mengimport function yang ada pada file menu 
import os
import time

menu.F15.load()
print("!! SELAMAT DATANG DI ANTARMUKA BNMO !!\n")
print("Berikut Adalah Ketentuan permainannya\n")
print("=====================================\n")
print("User harus melakukan login terlebih dahulu sebelum bisa memilih menu lain\n")
print("=====================================\n")

game = menu.funct.read_csv('game.csv') # memanggil membaca dan membuka file yang bernama game.csv
kepemilikan = menu.funct.read_csv('kepemilikan.csv') # memanggil membaca dan memproses file kepemilikan.csv dengan fungsi pembuka dan membaca file kepemilikan.csv
riwayat = menu.funct.read_csv('riwayat.csv') # Memanggil membaca dan memproses file riwayat.csv 
user = menu.funct.read_csv('user.csv') # memanggil membaca dan memproses file user.csv
active_user = [] # Array kosong yang digunakan untuk menyimpan informasi aktivitas user 
arrayofkerangajaib =[round(time.time())]

while True:

  pilihan = input("Silahkan Masukkan Pilihan : ")
  if pilihan=="register":
    if menu.funct.length(active_user) == 0:  
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else: # 
      if active_user[4] == "user":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
      else:
        menu.F02.register(user)
    
  elif pilihan=="login":
    if menu.funct.length(active_user) == 0:
      menu.F03.login(user,active_user)
    else:
      print("Anda sedang login")
    
  elif pilihan=="tambah_game":
    if menu.funct.length(active_user) == 0 :
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      if active_user[4] == "user":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
      else:
        menu.F04.tambah_game(game)
  
  elif pilihan=="ubah_game":
    if menu.funct.length(active_user) == 0 :
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      if active_user[4] == "user":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
      else:
        menu.F05.ubah_game(game)

  elif pilihan=="ubah_stok":
    if menu.funct.length(active_user) == 0 :
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      if active_user[4] == "user":
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
      else:
        menu.F06.ubah_stok(game)

  elif pilihan=="list_game_toko":
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      menu.F07.list_toko(game)

  elif pilihan=="buy_game":
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      if active_user[4] == "admin":
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
      else:
        menu.F08.buy_game(active_user,user,game,kepemilikan,riwayat)

  elif pilihan=="list_game": 
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      if active_user[4] == "admin":
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
      else:
        menu.F09F10.list_game(active_user[0], game, kepemilikan, False)
        
  elif pilihan == "search_my_game":
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      if active_user[4] == "admin":
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
      else:
        menu.F09F10.search_my_game(active_user[0], kepemilikan, game)

  elif pilihan=="search_game_at_store":
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      menu.F11.search_game_at_store(game)

  elif pilihan=="top_up":
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    elif active_user[4] == "user":
      print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    else:
      menu.F12.Top_up(user)

  elif pilihan=="riwayat":
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    elif active_user[4] == "admin":
      print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    else:
      menu.F13.riwayatpembelian(active_user[0],riwayat) 

  elif pilihan=="help": #kalau di spesifikasi tuh kan katanya gaperlu login, tapi help admin sama user dipisah. Jadi kayak gimana yahh? :(
    if menu.funct.length(active_user) == 0:
      menu.F14.Help_Guest()
    elif active_user[4] == "admin":
      menu.F14.Help_Admin()
    elif active_user[4] == "user":
      menu.F14.Help_User()

  elif pilihan=="save":
    if menu.funct.length(active_user) == 0:
      print("Anda harus melakukan login terlebih dahulu untuk mengirim perintah selain login.")
    else:
      menu.F16.save(user,game,kepemilikan,riwayat)

  elif pilihan=="exit": 
    menu.F17.out("", user, game, kepemilikan, riwayat)
  elif pilihan=="kerangajaib": 
    menu.kerangajaib.jawabankerang(arrayofkerangajaib)
  elif pilihan=="tictactoe":
    menu.tictactoe.tictactoe()