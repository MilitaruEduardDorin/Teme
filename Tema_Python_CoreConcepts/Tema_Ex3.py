# Faceti un script in python care primeste 2 parametrii (numele utilizatorului și varsta  acestuia): 
# 1. Importa libraria sys 

import sys
import os

# 2. Dacă nu au fost pasati parametrii, aruncati o exceptie. 

# print(f'{sys.argv}')
# print (f'{len(sys.argv)}')

if len(sys.argv) != 3:
    print (f'Utilizare:  python3 {sys.argv[0]} nume_user varsta_user')
    sys.exit(1)
# 3. Dacă au fost pasati parametrii:  a. printati mesajul “Au fost pasati <n> parametrii”. 
else:
    print(f'Au fost pasati {len(sys.argv) - 1} parametrii')
# b. daca varsta este mai mare de 18 ani, creati un subdirector pe disk cu numele  utilizatorului. 
    if int(sys.argv[2]) > 18:
        print("Este major")
        if os.path.isdir(f"dir_{sys.argv[1]}"):
            print("Directorul exista")
        else:
            os.makedirs(f"dir_{sys.argv[1]}", exist_ok=True)
    else:
        print( "Varsta < 18 ani" )

