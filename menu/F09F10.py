import menu.function as funct

def list_game(user_id, game, kepemilikan, var):
  owned_game_id = []
  owned_game = []
  for row in kepemilikan:
    if row[1] == user_id:
      owned_game_id += [row[0]]
  for row in game:
    if row[0] in owned_game_id:
      owned_game += [row]
  if var:
    return owned_game
  elif funct.length(owned_game)==0:
    print("Maaf, kamu belum memiliki game. Ketik perintah beli_game untuk beli.")
  else:
    for row in owned_game:
      print(funct.justify(row[0], "left", 10), "| ", end="")
      print(funct.justify(row[1], "left", 45), "| ", end="")
      print(funct.justify(row[2], "left", 25), "| ", end="")
      print(funct.justify(row[3], "left", 10), "| ", end="")
      print(funct.justify(row[4], "left", 15), "| ", end="")
      print(funct.justify(row[5], "left", 5))


def search_my_game(user_id, kepemilikan, game):
  game_id = input("Masukkan ID Game: ")
  year = input("Masukkan Tahun Rilis Game: ")
  owned_game = list_game(user_id, game, kepemilikan, True)
  filtered_game = []
  if (game_id != "") & (year != ""):
    for row in owned_game:
      if (row[0] == game_id) & (row[3] == str(year)):
        filtered_game += [row]
  elif game_id != "":
    for row in owned_game:
      if row[0] == game_id:
        filtered_game += [row]
  elif year != "":
    for row in owned_game:
      if row[3] == str(year):
        filtered_game += [row]
  else:
    filtered_game = owned_game
  if not(filtered_game):
    print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
  else:
    print("Daftar game pada inventory yang memenuhi kriteria:")
    for row in filtered_game:
      print(funct.justify(row[0], "left", 10), "| ", end="")
      print(funct.justify(row[1], "left", 45), "| ", end="")
      print(funct.justify(row[2], "left", 25), "| ", end="")
      print(funct.justify(row[3], "left", 10), "| ", end="")
      print(funct.justify(row[4], "left", 15), "| ", end="")
      print(funct.justify(row[5], "left", 5))

