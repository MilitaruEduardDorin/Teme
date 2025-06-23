# Vrei să monitorizezi timpul de răspuns al unui site web pentru a verifica dacă serverulrăspunde rapid. 
# Scriptul va trimite cereri HTTP la fiecare 2 secunde și va afișa timpul de răspuns în milisecunde.

import os
import requests
import sys

# 1. Scrieți o funcție ce primește ca parametru un url și întoarce timpul de răspuns al paginii (cat dureaza sa primim un răspuns). folosește libraria time pt asta. 

import time

def url_response_time (url="https://www.google.com/"):
    start=time.time()
    try:
        raspuns=requests.get(url)
        raspuns.raise_for_status()
    except requests.RequestException as exceptie:
        print (f"Eroare aruncata la accesarea URL-ului:  {exceptie}")
        return None
    end=time.time()
    durata_ms=(end - start) * 1000
    return durata_ms

url=sys.argv[1]

print(f"Timp raspuns pt {url} : ", url_response_time(url))

# 2. Adaugati încă o funcție ce primește doi parametrii (un url si un numar de repetari): 
    # ○ Funcția va face într-un for sau while un număr de cal-uri către url și va memora timpurile de răspuns într-o listă (folosind prima metoda) 
    # ○ Funcția va face o medie și va întoarce într-un tuplu 3 valori în următoarea ordine: (min, media, max) 
    # ○ Rulați de cateva ori funcția cu cateva url-uri si afisati rezultatele