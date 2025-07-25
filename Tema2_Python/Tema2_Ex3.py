# Faceti un script de python ce face backup la un fisier (doar dacă acesta a fost modificat). 
# Calea catre fișierul la care face backup este primita ca argument.  
# Puneti scriptul de python in crontab sa ruleze automat la fiecare minut.
# Hint: 
# hashlib.sha256(f.read()).hexdigest() (reutilizati metoda de la ex2)
# os.listdir(backup_dir)
# os.path.isfile(file_path)
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# shutil.copy2(file_path, backup_name)
 
import argparse
from Tema2_Ex2_utils import sha_file
import os
from datetime import datetime
import shutil
import sys

def get_latest_backup_hash (backup_dir):
    backups=sorted(os.listdir(backup_dir), reverse=True)
    for backup_file in backups:
        backup_full_path=os.path.join(backup_dir, backup_file)
        if os.path.isfile(backup_full_path):
            return sha_file(backup_full_path)  

parser=argparse.ArgumentParser(description='E nevoie de calea catre fisier pt acest script')
parser.add_argument('file_path', help='Calea catre fisierul pt care trebuie sa se faca backup')
args=parser.parse_args()

if not os.path.isfile(args.file_path):
    print ('Nu ai furnizat calea catre un fisier')
    sys.exit(1)

backup_dir=os.path.join(os.path.dirname(__file__), 'Tema2_Ex3_Backup')
os.makedirs(backup_dir, exist_ok=True)

current_hash = sha_file(args.file_path)
last_backup_hash = get_latest_backup_hash(backup_dir)

if current_hash != last_backup_hash:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.basename(args.file_path)
    backup_name = os.path.join(backup_dir, f'{filename}_{timestamp}')
    shutil.copy2(args.file_path,backup_name)
    print (f'S-a realizat backup pt {args.file_path} in {backup_name}')
else:
    print('Nu s-a schimbat nimic. Nu se va face backup')

