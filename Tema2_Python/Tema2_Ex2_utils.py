# Faceți un modul de utils in care adaugati 2 metode: una care face sha256 hash la un string si alta la un fisier. 
# Testați aceste metode de utils dintr-un alt script de python.
# Hint:
# hashlib.sha256(text.encode()).hexdigest()
# hashlib.sha256(f.read()).hexdigest()

# Bonus question: Folosiți libraria facuta de voi pentru a genera un sha256 hash pentru un fisier de pe disk si comparati-l cu valoarea obtinuta ruland comanda de linux sha256sum.

import hashlib


def sha_string (string):
    return hashlib.sha256(string.encode()).hexdigest()

def sha_file (fisier):
    with open(fisier , 'rb') as fisier:
        return hashlib.sha256(fisier.read()).hexdigest()