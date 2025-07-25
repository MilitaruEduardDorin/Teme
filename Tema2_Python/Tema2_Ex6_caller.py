from Tema2_Ex6_utils import encode_text, decode_text
import argparse

parser=argparse.ArgumentParser(description='Acest script face fie encoding fie decodin la un text')
parser.add_argument('--encode',help='Pentru encode trebuie furnizat un string, ex: "SALUT"')
parser.add_argument('--decode', help='Pentru decode trebuie furnizat codul de bytes, ex: "dGVzdA=="')
args=parser.parse_args()


if args.encode:
    print(encode_text(args.encode))

if args.decode:
    print(decode_text(args.decode))

if not args.encode and not args.decode:
    print('Trebuie transmis macar un argument, fie --encode fie --decode')