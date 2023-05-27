from menu.function import validasi_input, length, validasi_id_game

def ubah_game(game):
    id = input("Masukkan ID game: ")

    if id == '':  # id tidak diinput
        print("Anda wajib memasukkan ID game yang ingin diubah")
    else:  # id telah diinput
        # mengecek eksistensi id game di data
        if validasi_id_game(game, id) == True:  # id game ditemukan
            nama_game = input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun_rilis = input("Masukkan tahun rilis: ")
            harga = input("Masukkan harga: ")
            if validasi_input(nama_game) == False or validasi_input(
                    kategori) == False or validasi_input(
                        tahun_rilis) == False or validasi_input(
                            harga) == False:  # ada input yang mengandung ';'
                print("Anda tidak dapat menambahkan ';' pada input")
            else:  # semua input tidak ada yang mengandung ';'
                L = [id, nama_game, kategori, tahun_rilis, harga]
                for i in range(
                        1, length(game)
                ):  # traversal mulai dari baris selain baris judul dalam read_csv(game.csv)
                    if id == game[i][0]:  # baris dimana id sesuai ditemukan
                        kolom = length(
                            game[i]
                        ) - 1  # jumlah kolom read_csv(game.csv) selain kolom stok
                        for j in range(
                                1, kolom
                        ):  # traversal kolom mulai dari kolom selain kolom id dan stok
                            if L[j] != '':  # diubah sesuai input jika input tidak kosong, dibiarkan(tidak diubah) jika input kosong
                                game[i][j] = L[j]
        else:  # id game tidak ditemukan
            print("Game Anda tidak ditemukan.")
    return
