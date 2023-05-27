def pilihan_Admin():
    print('Apakah anda ingin kembali ke menu help? (y/n)')
    yn = input(">>> ")
    while yn != 'Y' and yn !='y' and yn != 'N' and yn != 'n':
        print('Sistem Error! Silahkan memilih kembali')
        yn = input(">>> ")

    if yn == 'Y' or yn == 'y':
        Help_Admin()
    #elif n ???

def pilihan_User():
    print('Apakah anda ingin kembali ke menu help? (y/n)')
    yn = input(">>> ")
    while yn != 'Y' and yn !='y' and yn != 'N' and yn != 'n':
        print('Sistem Error! Silahkan memilih kembali')
        yn = input(">>> ")

    if yn == 'Y' or yn == 'y':
        Help_User()
    #elif n ???

def pilihan_guest():
    print('Apakah anda ingin kembali ke menu help? (y/n)')
    yn = input(">>> ")
    while yn != 'Y' and yn !='y' and yn != 'N' and yn != 'n':
        print('Sistem Error! Silahkan memilih kembali')
        yn = input(">>> ")

    if yn == 'Y' or yn == 'y':
        Help_Guest()

def Help_Guest():
    print('''
1. login - Untuk melakukan login ke dalam sistem. Anda harus login sebelum bisa mengakses menu lain.
''')
    pilihan = input('>>> ')
    if pilihan == "login":
      print('''
--login--
Untuk mengakses seluruh fitur dari BNMO, anda harus masuk terlebih dahulu.

Buka halaman login dengan mengetik login pada kolom pilihan di halaman utama, kemudian masukkan seluruh informasi dengan benar agar dapat masuk ke halaman utama BNMO. apabila salah satu masukan tidak valid, sistem akan mengeluarkan pesan error. Silahkan memasukkan informasi login anda dengan benar.
''')
      pilihan_guest()

def Help_Admin():
    print('''
1. register - Untuk melakukan registrasi user baru
2. login - Untuk melakukan login ke dalam sistem
3. tambah_game - Untuk menambah game yang dijual pada toko
4. ubah_game - Untuk mengubah detil game
5. ubah_stok - Untuk mengubah jumlah stok game
6. list_game_toko - Untuk melihat list game yang dijual pada toko
7. search_game_at_store - Untuk mencari game yang ada pada toko
8. topup - Untuk menambah saldo user
9. save - Untuk menyimpan perubahan
          
Silahkan mengetikkan kata kunci untuk mengakses menu ''')
    pilihan = input('>>> ')

    if pilihan == "register":
        print('''
--register--

Untuk mengakses seluruh fitur dari BNMO, anda harus memiliki akun BNMO. Akun BNMO dapat diperoleh dengan membuka halaman register. 

Anda dapat memasukkan seluruh informasi yang diminta pada menu register dengan mengetik register pada kolom pilihan di halaman utama. Apabila username telah terpakai, sistem akan mengeluarkan pesan error berbunyi "Username [nama username] telah terpakai, silahkan menggunakan username lain".

Apabila sistem mengeluarkan pesan berhasil, maka anda sudah memiliki akun BNMO dan anda dapat mengakses seluruh fitur dari BNMO.
''')
        pilihan_Admin()
    elif pilihan == "login":
        print('''
--login--
Untuk mengakses seluruh fitur dari BNMO, anda harus masuk terlebih dahulu.

Buka halaman login dengan mengetik login pada kolom pilihan di halaman utama, kemudian masukkan seluruh informasi dengan benar agar dapat masuk ke halaman utama BNMO. apabila salah satu masukan tidak valid, sistem akan mengeluarkan pesan error. Silahkan memasukkan informasi login anda dengan benar.
''')
        pilihan_Admin()
    elif pilihan == "tambah_game":
        print('''
--tambah_game--
sebagai admin, anda dapat menambahkan game anda untuk dapat dibeli oleh user.

Silahkan buka halaman tambah game dengan mengetik tambah_game pada kolom pilihan di halaman utama, masukkan seluruh informasi dengan benar agar informasi game dapat tersimpan dengan baik dalam server. apabila salah satu informasi tidak terisi, sistem akan mengeluarkan pesan error dan meminta anda kembali untuk memasukkan seluruh informasi game dengan benar.

Jangan lupa untuk melakukan penyimpanan seluruh perubahan dalam fungsi "save". Untuk informasi lebih lanjut, anda dapat melihat pada halaman "Help" ini dengan memilih pilihan "save".
''')
        pilihan_Admin()
    elif pilihan == "ubah_game":
        print('''
--ubah_game--
sebagai admin, anda dapat melakukan perubahan informasi terhadap game yang anda miliki, kecuali stok game (stok game diubah dalam halaman "ubah_stok").

Silahkan buka halaman ubah game dengan mengetik ubah_game pada kolom pilihan di halaman utama, masukkan ID game dan isi perubahan pada kolom yang ingin dirubah informasinya.

Jangan lupa untuk melakukan penyimpanan seluruh perubahan dalam fungsi "save". Untuk informasi lebih lanjut, anda dapat melihat pada halaman "Help" ini dengan memilih pilihan "save".
''')
        pilihan_Admin()
    elif pilihan == "ubah_stok":
        print('''
--ubah_stok--
Pada halaman ini, anda dapat mengubah stok game yang tersedia.

Silahkan membuka halaman ubah stok dengan mengetik ubah_stok pada kolom pilihan di halaman utama, masukan ID game dan silahkan mengisi perubahan jumlah pada kolom tersebut.

Jangan lupa untuk melakukan penyimpanan seluruh perubahan dalam fungsi "save". Untuk informasi lebih lanjut, anda dapat melihat pada halaman "Help" ini dengan memilih pilihan "save".
''')
        pilihan_Admin()
    elif pilihan == "list_game_toko":
        print('''
--list_game_toko--
Toko dapat melakukan listing game berdasarkan 2 skema sorting yang telah ditentukan. anda dapat melakukan skema sorting berdasarkan tahun rilis atau harga secara descending(-) dan ascending(+)

Silahkan membuka halaman listing game di toko dengan mengetik list_game_toko pada kolom pilihan di halaman utama, lalu ketik skema sorting yang akan dipilih

terdapat 4 pilihan skema sorting:
tahun- (Digunakan untuk menampilkan daftar game di toko dengan sorting tahun secara menurun)
tahun+ (Digunakan untuk menampilkan daftar game di toko dengan sorting tahun secara menaik)
harga- (Digunakan untuk menampilkan daftar game di toko dengan sorting harga secara menurun)
harga+ (Digunakan untuk menampilkan daftar game di toko dengan sorting harga secara menaik)

apabila kolom skema sorting tidak diisi, sistem akan secara otomatis melakukan sorting berdasarkan ID secara menaik.
''')
        pilihan_Admin()
    elif pilihan == "search_game_at_store":
        print('''
--search_game_at_store--
Pada halaman ini, sistem dapat melakukan pencarian game pada toko berdasarkan ID, nama, harga, kategori, maupun tahun rilis game.

Silahkan buka halaman pencarian game pada toko dengan mengetik search_game_at_store pada kolom pilihan di halaman utama, kemudian masukkan salah satu atau lebih informasi untuk mencari game yang diinginkan.
''')
        pilihan_Admin()

    elif pilihan == "topup":
        print('''
--topup--
Sebagai admin, anda dapat menambahkan saldo user agar user dapat membeli game.

Silahkan buka halaman top up pada toko dengan mengetik topup pada kolom pilihan di halaman utama, kemudian masukkan id user dan nominal top up saldo.
''')
        pilihan_Admin()
    elif pilihan == "save":
        print('''
--save--
Untuk menyimpan seluruh perubahan pada sistem BNMO, anda diharuskan untuk menyimpan perubahan dengan mengakses halaman save.

Silahkan buka halaman penyimpanan dengan mengetik save pada kolom pilihan di halaman utama,kemudian masukkan sana folder penyimpanan agar perubahan dapat disimpan.
''')
        pilihan_Admin()
    

def Help_User():
    print('''
1. login - Untuk melakukan login ke dalam sistem
2. list_game_toko - Untuk melihat list game yang dijual pada toko
3. buy_game - Untuk membeli game
4. list_game - Untuk melihat game yang dimiliki
5. search_my_game - Untuk meencari game yang dimiliki
6. search_game_at_store - Untuk mencari game yang ada pada toko
7. riwayat - Untuk melihat riwayat pembelian
8. save - Untuk menyimpan seluruh perubahan

Silahkan mengetikkan kata kunci untuk mengakses menu
''')    
    pilihan = input('>>> ')

    if pilihan == "login":
        print('''
--login--
Untuk mengakses seluruh fitur dari BNMO, anda harus masuk terlebih dahulu.

Buka halaman login dengan mengetik login pada kolom pilihan di halaman utama, kemudian masukkan seluruh informasi dengan benar agar dapat masuk ke halaman utama BNMO. apabila salah satu masukan tidak valid, sistem akan mengeluarkan pesan error. Silahkan memasukkan informasi login anda dengan benar.
''')
        pilihan_User()
    elif pilihan == "list_game_toko":
        print('''
--list_game_toko--
Toko dapat melakukan listing game berdasarkan 2 skema sorting yang telah ditentukan. anda dapat melakukan skema sorting berdasarkan tahun rilis atau harga secara descending(-) dan ascending(+).

Silahkan membuka halaman listing game di toko dengan mengetik list_game_toko pada kolom pilihan di halaman utama, lalu ketik skema sorting yang akan dipilih.

terdapat 4 pilihan skema sorting:
tahun- (Digunakan untuk menampilkan daftar game di toko dengan sorting tahun secara menurun)
tahun+ (Digunakan untuk menampilkan daftar game di toko dengan sorting tahun secara menaik)
harga- (Digunakan untuk menampilkan daftar game di toko dengan sorting harga secara menurun)
harga+ (Digunakan untuk menampilkan daftar game di toko dengan sorting harga secara menaik)

apabila kolom skema sorting tidak diisi, sistem akan secara otomatis melakukan sorting berdasarkan ID secara menaik.
''')
        pilihan_User()
    elif pilihan == "buy_game":
        print('''
--buy_game--
Sebagai user, anda dapat membeli game dengan cara mengakses halaman pembelian game dengan mengetik buy_game pada kolom pilihan di halaman utama, kemudian masukkan ID game yang ingin dibeli.

Sistem akan mengeluarkan pesan berhasil apabila saldo yang dimiliki cukup untuk membeli game tersebut. Sistem akan mengeluarkan pesan error apabila saldo user tidak cukup untuk membeli game tersebut, user telah memiliki game tersebut, atau stok game tersebut sedang habis.
''')
        pilihan_User()
    elif pilihan == "list_game":
        print('''
--list_game--
Anda dapat melihat daftar game yang telah dimiliki dengan cara mengetik list_game pada kolom pilihan di halaman utama, kemudian sistem akan mengeluarkan tabel yang berisi daftar game yang telah dimiliki. Sistem akan mengeluarkan pesan error apabila user belum pernah membeli game sama sekali.
''')
        pilihan_User()
    elif pilihan == "search_my_game":
        print('''
--search_my_game--
Pada halaman ini, sistem dapat melakukan pencarian game yang dimiliki berdasarkan ID maupun tahun rilis game.

Silahkan buka halaman pencarian game pada toko dengan mengetik search_my_game pada kolom pilihan di halaman utama, kemudian masukkan salah satu atau lebih informasi untuk mencari game yang diinginkan.
''')
        pilihan_User()
    elif pilihan == "search_game_at_store":
        print('''
--search_game_at_store--
Pada halaman ini, sistem dapat melakukan pencarian game pada toko berdasarkan ID, nama, harga, kategori, maupun tahun rilis game.

Silahkan buka halaman pencarian game pada toko dengan mengetik search_game_at_store pada kolom pilihan di halaman utama, kemudian masukkan salah satu atau lebih informasi untuk mencari game yang diinginkan.
''')
        pilihan_User()
    elif pilihan == "riwayat":
        print('''
--riwayat--
Pada halaman ini, anda dapat melihat daftar riwayat pembelian anda.

Silahkan membuka halaman riwayat dengan mengetik riwayat pada kolom pilihan di halaman utama, kemudian sistem akan mengeluarkan daftar game yang telah dibeli user. Sistem akan mengeluarkan pesan error apabila user tidak memiliki game.
''')
        pilihan_User()
    elif pilihan == "save":
        print('''
--save--
Untuk menyimpan seluruh perubahan pada sistem BNMO, anda diharuskan untuk menyimpan perubahan dengan mengakses halaman save.

Silahkan buka halaman penyimpanan dengan mengetik save pada kolom pilihan di halaman utama,kemudian masukkan sana folder penyimpanan agar perubahan dapat disimpan.
''')
        pilihan_User()

""" Ini nanti masuk main program aja, biar disini isinya prosedur semua
if role == "admin" or role == "ADMIN" or role == "Admin":
    Help_Admin()
elif role == "user" or role == "USER" or role == "User":
    Help_User()"""