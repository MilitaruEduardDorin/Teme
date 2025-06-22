# Scrieti un program in python care: 
# ● Citește o variabila cu numele “parolă” introdusă de utilizator, folosind metoda input() 

import os

parola = input("Introdu parola: ")

# ● Verifica dacă variabila are aceeași valoare ca o variabila de mediu cu numele PAROLA_SECRETA 

        # eu@DevOps-ITSchool:~$ export PAROLA_SECRETA=parola 
        # eu@DevOps-ITSchool:~$ echo $PAROLA_SECRETA
        # parola

PAROLA_SECRETA = os.environ['PAROLA_SECRETA']

if parola == PAROLA_SECRETA:
# ● Dacă are aceeași valoare, printati “Parola corecta”, în caz contrar afișați parola greșită.
    print ('Parola corecta')
else:
    print ('Parola gresita')

# ● Rulați programul cu mai multe valori și verificati ca face ce trebuie.