# Faceți un script de python ce verifica dacă nivelul de ocupare al discului este mai mare de un prag (configurable printr-o variabila de mediu - implicit 90%). 
# În cazul în care ocuparea discului este mai mare de acest prag printeaza un mesaj de alertă în consola.
# Puneti acest script sa ruleze in ~/.bashrc

import os
import shutil

def disk_storage ():

    prag=int(os.getenv('DISK_STORAGE_TRESHOLD', 90))

    total, used, free = shutil.disk_usage('/')

    procent_folosit=int((used/total)*100)

    return procent_folosit, prag

for i in range(0,1):
    rezultate=list(disk_storage())
    if rezultate[0] > rezultate[1]:
        print (f'ALERTA: Discul e folosit {rezultate[0]}%, peste PRAGUL de {rezultate[1]}%')
    elif rezultate[0] == rezultate[1]:
        print(f'ALERTA: Discul e folosit {rezultate[0]}%, FIX la valoarea PRAGULUI {rezultate[1]}%')
    else:
        print(f'Discul e folosit {rezultate[0]}%, mai ai {rezultate[1] - rezultate[0]}% pana sa atingi Pragul de {rezultate[1]}')

###NU am adaugat scriptul in ~/.bashrc. Pt testare trebuie 'export DISK_STORAGE_TRESHOLD=60' inainte de rulare script 
