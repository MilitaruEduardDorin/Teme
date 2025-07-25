# Faceți un modul de utils in care adaugati 2 metode: una care face sha256 hash la un string si alta la un fisier. 
# Testați aceste metode de utils dintr-un alt script de python.
# Hint:
# hashlib.sha256(text.encode()).hexdigest()
# hashlib.sha256(f.read()).hexdigest()

# Bonus question: Folosiți libraria facuta de voi pentru a genera un sha256 hash pentru un fisier de pe disk si comparati-l cu valoarea obtinuta ruland comanda de linux sha256sum.


import argparse
from Tema2_Ex2_utils import sha_string, sha_file

parser=argparse.ArgumentParser(description='Testare functii de sha pt ex 2')
parser.add_argument('--string', help='String pt hash SHA256 prin functia sha_string')
parser.add_argument('--fisier',help='Fisier pt hash SHA256 prin functia sha_file')
args=parser.parse_args()

if args.string:
    print ('SHA256 pt string:')
    print(sha_string(args.string))

if args.fisier:
    print ('SHA256 pt fisier:')
    print (sha_file(args.fisier))
