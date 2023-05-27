import os

def read_csv(filename):
  data_dir = list_to_string_1_line(folder_path())+"database\\"
  f = open(data_dir+filename)
  #lines = [line.strip() for line in f]
  lines = [strip(line, ' ') for line in f]
  list_detail = []
  for line in lines:
    #elem = line.split(";")
    elem = split(line, ";")
    list_detail += [elem]
  f.close()
  return list_detail

def split(text, separator):
  list_word = []
  word = ""
  for char in text:
    if char != separator:
      word += char
    else:
      list_word += [word]
      word = ""
  if word != "":
    list_word += [word]       
  return list_word

def list_to_string(list):
  string = ""
  for row in list:
    newrow = ""
    for elem in row:
      if newrow=="":
        newrow += elem
      else:
        newrow += ';'+elem
    if row != list[length(list)-1]:
      newrow += '\n'
    string += newrow
  return string

def length(string):
  length = 0
  for letter in string:
    length += 1
  return length

def strip(string, char):
    stripped=''
    indeksawal = 0
    indeksakhir = length(string) - 1
    i = 0
    while i < length(string):
        if (string[i] in char) or string[i] == '\n':
            i += 1
        else:
            indeksawal = i
            break
    j = length(string) - 1
    while j >= 0:
        if (string[j] in char) or string[j] == '\n':
            j -= 1
        else:
            indeksakhir = j
            break
    for k in range(indeksawal, indeksakhir+1):
        stripped+=string[k]
    return stripped

def justify(string, tipe, num): #(string, left/right/center, int)
  strlen = length(string)
  newstring = ""
  if num <= strlen:
    return string
  else:
    if tipe == "left":
      newstring = string + (" "*(num-strlen))
    elif tipe == "right":
      newstring = (" "*(num-strlen)) + string
    elif tipe == "center":
      newstring = (" "*((num-strlen)//2)) + string + (" "*((num-strlen)//2))
  return newstring
      
def sortlist(lst, category, ascending): #(list, int, bool)
  if ascending:
    for i in range(length(lst)-1, 0, -1):
      for j in range(i):
        if int(strip(lst[j][category], "GAME"))>int(strip(lst[j+1][category], "GAME")):
          temp = lst[j]
          lst[j] = lst[j+1]
          lst[j+1] = temp
                
  else:
    for i in range(length(lst)-1, 0, -1):
      for j in range(i):
        if int(strip(lst[j][category], "GAME"))<int(strip(lst[j+1][category], "GAME")):
          temp = lst[j+1]
          lst[j+1] = lst[j]
          lst[j] = temp
  return lst

def validasi_input(word):
    valid_input = True
    i = 0
    while i < length(word) and valid_input == True:
        if word[i] == ';':
            valid_input = False
        else:
            i += 1
    return valid_input

# validasi keunikan username
def username_unik(word, user):
    valid_input = True
    for i in range(1,length(user)):
        if user[i][1] == word:
            valid_input = False
            break
    return valid_input
        
# validasi username
def validasi_username(word):
    valid_input = True
    for letter in word:
        if not (ord(letter) >= 97 and ord(letter) <= 122 or ord(letter) >= 65 and ord(letter) <= 90 or ord(letter) >= 48 and ord(letter) <= 57 or letter == '-' or letter == '_') :
            valid_input = False
            break
    return valid_input

# menghitung id baru
def count_user_id(array):
  urutan = length(array)
  if urutan > 0 and urutan < 10 :
    id = "00" + str(urutan)
  elif urutan >= 10 and urutan < 100 : 
    id = "0" + str(urutan)
  else:
    id = str(urutan)
  return id

def count_game_id(array):
  urutan = length(array)
  if urutan > 0 and urutan < 10 :
    id = "GAME" + "00" + str(urutan)
  elif urutan >= 10 and urutan < 100 : 
    id = "GAME" + "0" + str(urutan)
  else:
    id = "GAME" + str(urutan)
  return id

def validasi_skema(skema):
  if ((strip(skema, "+-").lower()!="tahun")&(strip(skema, "+-").lower()!="harga"))&(skema!="")&\
     ((strip(skema, "aghnrtu")!="+")&(strip(skema, "aghnrtu")!="-")): #aghnrtu biar tahun sama harga ke strip
    return False
  else:
    return True

def skema(skema):
  if skema=="":
    category = 0
    ascending = True
  else:
    category = strip(skema, "+-")
    if category=="tahun":
      category = 3
    elif category=="harga":
      category = 4
    ascending = strip(skema, "aghnrtu")=="+"
  return category, ascending

def validasi_id_game(game, game_id): # yang ini di F05 validasi_id_game sebelumnya validasi_game_id
  valid = False
  for row in game:
    if row[0]==game_id.upper():
      valid = True
  return valid

def delete_first_row(list):
  temp = []
  for i in range(1, length(list)):
    temp += [list[i]]
  return temp

def username_exist(user, username):
  for row in user:
    if row[1]==username:
      return True
  return False

def list_to_string_1_line(list):
  string = ""
  for elem in list:
    string += str(elem)
  return string

def folder_path():
  cwd = os.path.dirname(os.path.realpath(__file__))
  list_cwd = split(cwd, '\\')
  new_list = []
  for dir in list_cwd:
    if dir=='menu':
      continue
    new_list += [dir+'\\']
  return new_list

def current_folder():
  path = folder_path()
  return strip(path[-1], '\\')