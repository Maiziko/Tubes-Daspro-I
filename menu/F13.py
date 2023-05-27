import menu.function as funct
def riwayatpembelian(user_id, riwayat):
  riwayat_user = []
  for row in riwayat:
    if row[3]==user_id: 
      riwayat_user += [[row[i] for i in range(5) if i != 4]]
  if bool(riwayat_user):
    for row in riwayat_user:
      print(funct.justify(row[0], "left", 10), "| ", end="")
      print(funct.justify(row[1], "left", 45), "| ", end="")
      print(funct.justify(row[2], "left", 25), "| ", end="")
      print(funct.justify(row[3], "left", 15))
  else:
    print("Maaf, kamu tidak ada riwayat pembelian game. Ketik 'Beli Game' untuk membeli.")
