# Imachetati intr-o imagine de docker un script de python ce muta fisiere dintr-un director “input” intr-un director “output”. 
# După fiecare fișier mutat scriptul de python “doarme” 5 secunde.
# Porniti imagine de docker si mapati input si output folder la 2 directoare de pe masina VM.
# Hint: Puteți avea mai multe -v augmentes la același run:

#   -v /tmp/input:/input \
#   -v /tmp/output:/output

# Porniti 4 containere de docker configurate identic. Verificati ca sunt mutate fișierele de 4 ori mai repede.  

import os
import shutil
import time
import random

source='/input'
destination='/output'

while True:
    fisiere=sorted(os.listdir(source))
    cale_completa_source=source+'/'+fisiere[0]
    cale_completa_destination=destination+'/'+fisiere[0]
    shutil.move(cale_completa_source, cale_completa_destination)
    time.sleep(random.randint(2,5))
