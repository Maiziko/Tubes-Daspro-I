import menu.function as funct

def list_toko(game):
  skema = input("Skema sorting: ")
  if funct.validasi_skema(skema)==False:
    print("Skema sorting tidak valid!")
  else:
    category, ascending = funct.skema(skema)
    sorted_list = funct.sortlist(funct.delete_first_row(game), category, ascending)
    for row in sorted_list:
      print(funct.justify(row[0], "left", 10), "| ", end="")
      print(funct.justify(row[1], "left", 45), "| ", end="")
      print(funct.justify(row[2], "left", 25), "| ", end="")
      print(funct.justify(row[3], "left", 10), "| ", end="")
      print(funct.justify(row[4], "left", 15), "| ", end="")
      print(funct.justify(row[5], "left", 5))

