# Faceți un modul de utils (sau adaugati in modulul creat la exercițiile precedente) in care adaugati 2 metode: 
# una care face encode base64 la un text si alta care face decode base64 la text. 
# Testați aceste metode de utils dintr-un alt script de python.

import base64

def encode_text(text='test'):
    text_as_bytes=text.encode('utf-8')
    encoded_text=base64.b64encode(text_as_bytes)
    encoded_as_str=encoded_text.decode('utf-8')
    return  encoded_as_str

#print(encode_text())

def decode_text(encoded_as_str='dGVzdA=='):
    encoded_as_bytes=encoded_as_str.encode('utf-8')
    decoded_text=base64.b64decode(encoded_as_bytes)
    text_as_str=decoded_text.decode('utf-8')
    return text_as_str

#print(decode_text())