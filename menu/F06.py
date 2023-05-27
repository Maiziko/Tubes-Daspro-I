import menu.function as funct

def ubah_stok(game):
  game_id = input("Masukkan ID Game: ")
  if funct.validasi_id_game(game,game_id)==False:
    print("Tidak ada game dengan ID tersebut!")
  else: # ID Game ditemukan
    jumlah = input("Masukkan jumlah: ")
    for row in game:
      if row[0]==game_id.upper():
        if (int(row[5])+int(jumlah))<0:
          print(f"Stok game {row[1]} gagal dikurangi karena stok kurang. Stok sekarang: {row[5]} (< {-int(jumlah)})")
        else:
          row[5] = str(int(row[5])+int(jumlah))
          if int(jumlah)<0:
            print(f"Stok game {row[1]} berhasil dikurangi. Stok sekarang: {row[5]}")
          elif int(jumlah)>0:
            print(f"Stok game {row[1]} berhasil ditambah. Stok sekarang: {row[5]}")
          else:
            print(f"Stok game {row[1]} tidak diubah. Stok sekarang: {row[5]}" )