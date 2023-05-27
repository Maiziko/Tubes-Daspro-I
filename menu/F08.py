import datetime
from menu.function import length, validasi_id_game

def buy_game(login,user,game,kepemilikan,riwayat):
    id = input("Masukkan ID game: ")
    if validasi_id_game(game,id) == True:
        if cek_kepemilikan(id,login,kepemilikan) == True :
            print("Anda sudah memiliki game tersebut!")
        else:
            if cek_saldo(login, id, user, game) == True:
                if cek_stok(id,game) == True:
                    kepemilikan += [[id,login[0]]] # kepemilikan ditambah
                    temp = False
                    for row in user:
                        if login[0] == row[0]: # baris dimana id user yang ingin beli ditemukan
                            for row1 in game:
                                if row1[0] == id: # baris dimana id game yang ingin dibeli ditemukan
                                    row1[5] = str(int(row1[5])-1) # stok game dikurang
                                    row[5] = str(int(row[5]) - int(row1[4])) # saldo user dikurang
                                    riwayat += [[id,row1[1],row1[4],login[0],str(datetime.date.today().year)]] 
                                    temp = True
                                    print('Game "'+str(row1[1]+'" berhasil dibeli!'))
                                    break
                        if temp == True:
                            break
                else:
                    print("Stok game tersebut sedang habis")
            else:
                print("Saldo anda tidak cukup untuk membeli game tersebut")
    else:
        print("Game tidak ditemukan")
      
def cek_stok(gameid, game):
    buy = False
    for row in game:
        if row[0] == gameid:
            if int(row[5]) > 0:
                buy = True
                break
    return buy

def cek_saldo(login, id, user, game):
    saldo = False
    for row in game:
        if row[0] == id: # id game yang ingin dibeli ditemukan
          for baris in user:
            if baris[0] == login[0]: # user yang ingin beli ditemukan
              if int(baris[5]) > int(row[4]):
                  saldo = True
                  break
    return saldo

def cek_kepemilikan(gameid, login, kepemilikan):
    owned = False
    for row in kepemilikan:
        if row[0] == gameid:
            if login[0] == row[1]:
                owned = True
                break
    return owned