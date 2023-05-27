from menu.F16 import save

def out(simpan, user, game, kepemilikan, riwayat):
  if simpan=="":
    while (simpan.lower()!="n")&(simpan.lower()!="y"):
      simpan = input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
  if simpan.lower()=="y":
    save(user,game,kepemilikan,riwayat)
    exit()
  else:
    exit()