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

# url=sys.argv[1]

# print(f"Timp raspuns pt {url} : ", url_response_time(url))

# 2. Adaugati încă o funcție ce primește doi parametrii (un url si un numar de repetari): 

def functie_2 (url,repetari):
    # ○ Funcția va face într-un for sau while un număr de cal-uri către url și va memora timpurile de răspuns într-o listă (folosind prima metoda)
    call=0
    list_durata =[]
    while call < repetari :
        call +=1
        durata = url_response_time(url)
        if durata is not None:
            list_durata.append(durata)
        else:
            print(f'Eroare cerere HTTTp la incercarea {call} din {repetari}')
        time.sleep(2)
    # ○ Funcția va face o medie și va întoarce într-un tuplu 3 valori în următoarea ordine: (min, media, max) 

    if list_durata:
        maxim = max(list_durata)
        minim = min(list_durata)
        medie = sum(list_durata) / len(list_durata)
        return (minim, medie , maxim)
    else:
        return(None, None, None)

rezultat = functie_2 (url="https://www.google.com/",repetari=5)
print(f'\nTimp minim: {rezultat[0]:.2f} ms')
print(f'\nTimp mediu: {rezultat[1]:.2f} ms')
print(f'\nTimp maxim: {rezultat[2]:.2f} ms')
    # ○ Rulați de cateva ori funcția cu cateva url-uri si afisati rezultatele