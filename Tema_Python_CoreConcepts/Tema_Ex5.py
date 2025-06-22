# Pornind de la un fișier text numit logs.txt în care sunt stocate mesaje de log de la mai multe servere, fiecare mesaj pe o linie, 
# vrem să identificăm toate liniile care conțin cuvântul ERROR și să le afisam împreună cu numărul liniei. 

import os

scrip_dir=os.path.dirname(os.path.abspath(__file__))
log_file_path=os.path.join(scrip_dir,"logs.txt")

default_log=[
'INFO: Server started successfully.', 
'WARNING: Disk space low.',
'ERROR: Unable to connect to database.',
'INFO: Scheduled backup completed.',
'ERROR: Failed to send email.',
]

if not os.path.exists(log_file_path):
    with open(log_file_path, "w") as log:
        for log_line in default_log:
            log.write(log_line.strip()+"\n")
    print ("""
Fisierul logs.txt a fost creat cu valori default
        """)
else:
    print("""
Fisierul logs.txt exista deja
          """)

# 1. Folosește o buclă for pentru a parcurge fiecare linie din fișier. 

with open(log_file_path,"r") as log:
    for line_number,log_line in enumerate(log,start=1):
# 2. Verifică dacă linia conține cuvântul ERROR. 
        if "ERROR" in log_line:
# 3. Afișează linia și numărul acesteia dacă conține ERROR. 
            print(f"{line_number} : {log_line}")







