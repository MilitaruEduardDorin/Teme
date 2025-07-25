# Faceti un script de python care primeste ca argument un string base64 si un nume de fisier. 
# Scriptul o sa creeze pe disk un fișier cu numele primit ca argument și o sa ii puna ca și conținut stringul decodat din base64.
# Testati scriptul.

import os
import shutil
import base64
import argparse

def decode_b64_string(string):
    string_to_bytes=string.encode('utf-8')
    decoded_string_as_bytes=base64.b64decode(string_to_bytes)
    decoded_string_as_string=decoded_string_as_bytes.decode('utf-8')
    return decoded_string_as_string

parser=argparse.ArgumentParser(description='Scriptul ruleza cu un string base64 si un nume de fisier')
parser.add_argument('b64_string')
parser.add_argument('file_name')
args=parser.parse_args()

with open(args.file_name, 'w') as file:
        file.write(decode_b64_string(args.b64_string))

#/bin/python3 /home/eu/ITSchool/Teme/Tema2_Python/Tema2_Ex7.py 'c2FsdXQ=' 'Tema2_Ex7_file.txt'

