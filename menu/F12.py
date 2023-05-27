import menu.function as funct

def Top_up(user):
  username = input("Masukkan username: ")
  if funct.username_exist(user, username):
    saldo = int(input("Masukkan saldo: "))
    for row in user:
      if row[1]==username:
        if (int(row[5])+saldo) >= 0:
          row[5] = str(int(row[5])+saldo)
          print(f"Top up berhasil. Saldo {username} menjadi {row[5]}")
        else:
          print("Masukan tidak valid")
  else:
    print(f"Username {username} tidak ditemukan.")