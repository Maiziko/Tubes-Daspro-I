from menu.function import count_game_id, length
def tambah_game(game): # fungsi tambah game digunakan untuk menambahkan persediaan game ke dalam sebuah array yang nanti akan di masukan ke dalam database , fungsi menggunakan parameter game sebagai array yang aan
    id = count_game_id(game)
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = str(input("Masukkan tahun rilis: "))
    harga = str(input("Masukkan harga: "))
    stok_awal = str(input("Masukkan stok awal: "))
    while nama_game == '' or kategori == '' or tahun_rilis == '' or harga == '' or stok_awal == '':
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")
    if int(tahun_rilis) < 0 or int(harga) < 0 or int(stok_awal) < 0 :
        print("Tahun rilis atau harga atau angka tidak boleh bernilai negatif")
    else:
        L = [id,nama_game,kategori,tahun_rilis,harga,stok_awal]
        game += [L]
        print(f"Selamat! berhasil menambahkan game {L[1]}.")