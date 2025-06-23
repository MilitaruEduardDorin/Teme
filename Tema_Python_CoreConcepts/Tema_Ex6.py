# Vrei să monitorizezi o aplicație pe care ai lansat-o (de exemplu, un script sau un serviciu) și  să te asiguri că procesul rulează continuu. 
# Dacă procesul se oprește, scriptul va încerca să îl  pornească din nou.

import os
import subprocess
import time

# 5. Numele procesului ce trebuie monitorizat este hardcodat într-o variabila la începutul scriptului. 

script_dir=os.path.dirname(os.path.abspath(__file__))
process_name=os.path.join(script_dir,"process_for_ex6.py")
#process_name="process_for_ex6.py"

# 1. Folosește o buclă while pentru a monitoriza în mod continuu procesul. 

number_of_restats=3
restart_curent=1


while restart_curent <= number_of_restats:
# 2. Verifică dacă procesul este activ folosind comanda pgrep. 
    process_check = subprocess.run(["pgrep", "-f", process_name], capture_output=True) #, text=True)
    #print(f"{process_check.stdout}")
# 3. Dacă procesul nu este găsit, pornește aplicația din nou.
    if process_check.returncode != 0:
# 4. Afișează un mesaj de avertizare de fiecare dată când procesul este repornit.
        print(f"{process_name} nu ruleaza, il voi reporni pt a {restart_curent} data","\n")
        subprocess.Popen(["python3", process_name],stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
        time.sleep(5)
        restart_curent=restart_curent + 1



        
        
        

