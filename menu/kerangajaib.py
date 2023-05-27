def angkaRandom(arrayforkerangajaib):
  random_number = (5*arrayforkerangajaib[len(arrayforkerangajaib)-1]+1) % 8
  arrayforkerangajaib += [random_number]
  return random_number

def jawabankerang(arrayforkerangajaib):
  global angkaRandom
  N = input("Apa pertanyaanmu? ")
  Jawaban_Kerang = angkaRandom(arrayforkerangajaib)

  if Jawaban_Kerang == 0:
    print("Ya.")
  elif Jawaban_Kerang == 1:
    print("Bisa jadi.")
  elif Jawaban_Kerang == 2:
    print("Tidak.")
  elif Jawaban_Kerang == 3:
    print("Mungkin Iya.")
  elif Jawaban_Kerang == 4:
    print("Mungkin tidak.")
  elif Jawaban_Kerang == 5:
    print("Tentunya")
  elif Jawaban_Kerang == 6:
    print("Tidak tahu")
  elif Jawaban_Kerang == 7:
    print("Mungkin besok")