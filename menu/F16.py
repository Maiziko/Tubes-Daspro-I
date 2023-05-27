import os
from menu.function import list_to_string

def save(user,game,kepemilikan,riwayat):
    directory = input("Masukkan nama folder penyimpanan: ")
    # cek apakah folder ada/tidak ada
    if os.path.isdir(os.path.join(os.getcwd(),directory)) == False: # folder tidak ada
        os.makedirs(os.path.join(os.getcwd(),directory))
        path_to_new_directory = os.path.join(os.getcwd(),directory)
        path_to_users_file = path_to_new_directory + "\\user.csv"
        path_to_game_file = path_to_new_directory + "\\game.csv"
        path_to_kepemilikan_file = path_to_new_directory + "\\kepemilikan.csv"
        path_to_riwayat_file = path_to_new_directory + "\\riwayat.csv"
        with open(path_to_users_file,"w") as userfile:
            userfile.write(list_to_string(user))
        with open(path_to_game_file,"w") as gamefile:
            gamefile.write(list_to_string(game))
        with open(path_to_kepemilikan_file,"w") as kepemilikanfile:
            kepemilikanfile.write(list_to_string(kepemilikan))
        with open(path_to_riwayat_file,"w") as riwayatfile:
            riwayatfile.write(list_to_string(riwayat))
        print("Saving...")
        print("Data sudah tersimpan pada folder "+str(directory)+"!")
      
        
    else : # folder ada
        path_to_users_file = os.path.join(os.getcwd(),directory,"user.csv")
        path_to_game_file = os.path.join(os.getcwd(),directory,"game.csv")
        path_to_kepemilikan_file = os.path.join(os.getcwd(),directory,"kepemilikan.csv")
        path_to_riwayat_file = os.path.join(os.getcwd(),directory,"riwayat.csv")
        with open(path_to_users_file,"w") as userfile:
            userfile.write(list_to_string(user))
        with open(path_to_game_file,"w") as gamefile:
            gamefile.write(list_to_string(game))
        with open(path_to_kepemilikan_file,"w") as kepemilikanfile:
            kepemilikanfile.write(list_to_string(kepemilikan))
        with open(path_to_riwayat_file,"w") as riwayatfile:
            riwayatfile.write(list_to_string(riwayat))
        print("Saving...")
        print("Data sudah tersimpan pada folder "+str(directory)+"!")
    return