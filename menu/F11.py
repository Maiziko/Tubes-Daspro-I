import menu.function as funct

def search_game_at_store(game):
  game_id = input("Masukan ID Game: ")
  game_name = input("Masukan Nama Game: ")
  price = input("Masukan Harga Game: ")
  category = input("Masukan Kategori Game: ")
  year = input("Masukan Tahun Rilis Game")
  temp = game[:]
  result = []
  if game_id!="":
    for row in temp:
      if row[0].lower()==game_id.lower():
        result += [row]
    temp = result[:]
    result = []
  if game_name!="":
    for row in temp:
      if row[1].lower()==game_name.lower():
        result += [row]
    temp = result[:]
    result = []
  if price!="":
    for row in temp:
      if row[4]==str(price):
        result += [row]
    temp = result[:]
    result = []
  if category!="":
    for row in temp:
      if row[2].lower()==category.lower():
        result += [row]
    temp = result[:]
    result = []
  if year!="":
    for row in temp:
      if row[3]==str(year):
        result += [row]
    temp = result[:]
    result = []
  result = temp[:]
  if not(result):
    print("Tidak ada game yang memenuhi kriteria")
  else:
    for row in result:
      print(funct.justify(row[0], "left", 10), "| ", end="")
      print(funct.justify(row[1], "left", 45), "| ", end="")
      print(funct.justify(row[2], "left", 25), "| ", end="")
      print(funct.justify(row[3], "left", 10), "| ", end="")
      print(funct.justify(row[4], "left", 15), "| ", end="")
      print(funct.justify(row[5], "left", 5))