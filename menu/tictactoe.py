def menang(papan):
    for row in papan:
        if row[0]==row[1] and row[1]==row[2] and row[2]!='#':
            return row[0], True
    for i in range(3):
        if papan[0][i]==papan[1][i] and papan[1][i]==papan[2][i] and papan[2][i]!='#':
            return papan[i][0], True
    return None, False

def print_papan(papan):
    for row in papan:
        string = ""
        for i in range(3):
            string += row[i]
        print(string)

def valid(x, y, papan):
    if x>3 or y>3:
      print("Kotak tidak valid")
      return False
    if papan[y-1][x-1] != '#':
      print("Kotak sudah terisi. silahkan pilih kotak lain")
      return False
    return True

def seri(papan):
    for row in papan:
      for column in row:
        if column == '#':
          return False
    return True

def tictactoe():
  pemenang = None
  papan = [['#' for i in range(3)] for j in range(3)]
  selesai = False
  print("""
Legenda: 
# Kosong
X pemain 1
O pemain 2
  """)
  print()
  print("Status Papan: ")
  print_papan(papan)
  print()
  while selesai==False:
      print("Giliran Pemain 'X'")
      x = int(input("X: "))
      y = int(input("Y: "))
      while not(valid(x, y, papan)):
        x = int(input("X: "))
        y = int(input("Y: "))
      papan[y-1][x-1] = "X"
      print("Status papan:")
      print_papan(papan)
      print()
      pemenang, selesai = menang(papan)
      if seri(papan) and pemenang==None:
        print("Seri. tidak ada yang menang")
        selesai = True
        break
      elif pemenang!=None:
        print(f"Pemain '{pemenang}' menang.")
        selesai = True
        break
      print("Giliran Pemain 'O'")
      x = int(input("X: "))
      y = int(input("Y: "))
      while not(valid(x, y, papan)):
        x = int(input("X: "))
        y = int(input("Y: "))
      papan[y-1][x-1] = "O"
      print("Status papan:")
      print_papan(papan)
      print()
      pemenang, selesai = menang(papan)
      if seri(papan) and pemenang==None:
        print("Seri. tidak ada yang menang")
        selesai = True
        break
      elif pemenang!=None:
        print(f"Pemain '{pemenang}' menang.")
        selesai = True
        break