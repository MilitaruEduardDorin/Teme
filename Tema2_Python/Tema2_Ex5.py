# Faceți un script de python ce muta unul cate unul fisierele dintr-un director în celalat. 


# Incercati sa porniti in acelasi timp 2 instante ale scriptului și verificati ca ambele funcționează corect.
# Hint:

# src_path = os.path.join(source_dir, filename)
# os.rename(src_path, lock_path)
# time.sleep(random.randint(1, 5))
# shutil.move(lock_path, dest_path)

import argparse
import os
import shutil
import time
import random

# Directorul sursa este primul argument al scriptului iar destinatie al doilea. 
parser=argparse.ArgumentParser(description='Scriptul ruleaza cu src_path si dest_path in ordinea asta')
parser.add_argument('src_path', help='Directorul sursa')
parser.add_argument('dest_path', help='Directorul destinatie')
args=parser.parse_args()

def file_mover(src_path, dest_path):
    files_to_move=sorted(os.listdir(src_path), reverse=True)
    os.makedirs(dest_path, exist_ok=True)
    for file_name in files_to_move:
        src_file=os.path.join(src_path,file_name)

        if not os.path.isfile(src_file):
            continue

        lock_path=src_file + '.lock'

        try:
            os.rename(src_file, lock_path)
            dest_file=os.path.join(dest_path,file_name)
            shutil.move(lock_path,dest_file)
            # După fiecare mutare de fișier scriptul doarme un numar random de secunde intre 1 si 5 (pentru a simula un long running process). 
            sleep_time=random.randint(1,5)
            time.sleep(sleep_time)
            print(f'Am mutat fisierul {file_name} in locatia {dest_file} si am asteptat {sleep_time} secunde')
        except FileNotFoundError:
            print (f'Nu am gasit {file_name}')
        except PermissionError:
            print(f'Nu am permisiunile necesare pt a muta {file_name}')
        except OSError as eroare:
            print(f'Am intampinat eroarea: {eroare}')

file_mover(args.src_path, args.dest_path)

#/bin/python3 /home/eu/ITSchool/Teme/Tema2_Python/Tema2_Ex5.py /home/eu/ITSchool/f2/sf1/sf2 /home/eu/ITSchool/f2/sf1/sf1