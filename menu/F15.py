import argparse
import os
import menu.function as funct

def load():
  parser = argparse.ArgumentParser()
  parser.add_argument('nama_folder', nargs="?")
  args = parser.parse_args()
  
  # print(f"{args.nama_folder}")
  # print(f"{funct.current_folder()}")
  if not(args.nama_folder):
    print("Tidak ada nama folder yang diberikan!")
    exit()
  if funct.current_folder()!=args.nama_folder:
    print(f"Folder {args.nama_folder} tidak ditemukan.")
    exit()