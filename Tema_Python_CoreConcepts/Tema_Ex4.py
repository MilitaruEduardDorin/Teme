# 1. Pentru acest exercițiu trebuie creat un fisier pe disk cu numele urls.txt ce conține pe fiecare linie cate o adresa url, de genul:  https://httpstat.us/201 

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
url_file_path = os.path.join(script_dir, "urls.txt")

urls = [
"https://httpstat.us/201",
"https://httpstat.us/400",
"https://httpstat.us/500",
"https://httpstat.us/404",
"https://httpstat.us/201",
"https://httpstat.us/503",
"https://httpstat.us/200",
"https://httpstat.us/303"
]

if not os.path.exists(url_file_path):
    with open(url_file_path, "w") as url_file:
        for url in urls:
            url_file.write(url.strip()+"\n")
    print("""Fisierul urls.txt a fost creat
          """)
else:
    print ("""Fisierul urls.txt exista deja
           """)
# 2. Citește linie cu line conținutul fișierului urls.txt 

with open(url_file_path, "r") as url_file:
    urls_citite=[]
    for line in url_file:
        urls_citite += [
            line.strip()
        ]
    print("Am citit liniile:")
    for url_line in urls_citite:
        print(url_line)
    print("")

# 3. Folosește libraria requests pentru a face un call http catre fiecare url 

import requests

status_success=[]
status_error=[]

for url in urls:
    try:
        raspuns=requests.get(url)#, timeout=90)
        code_status=raspuns.status_code
# 4. Daca url-ul a intors un status de success (intre 200 si 299) adauga url-ul intr-un fisier cu numele success.txt 
        if 200 <= code_status <= 299:
            status_success +=[
                url.strip()
            ]
# 5. Daca url-ul a intors un status de eroare (orice status intre 300 si 599) adauga url-ul intr-un fisier cu numele errors.txt 
        elif 300 <= code_status <= 599:
            status_error +=[
                url.strip()
            ]
    except requests.exceptions.RequestException as exceptie:
            status_error += [
               f"{url} Exceptie: {str(exceptie).strip()}"
            ]
success_file_path = os.path.join(script_dir, "success.txt")
errors_file_path = os.path.join(script_dir, "errors.txt")

with open(success_file_path, "w") as succes_file:
    for url in status_success:
        succes_file.write (url.strip()+"\n")

with open(errors_file_path, "w") as errors_file:
    for url in status_error:
        errors_file.write (url.strip()+"\n")

print("Continut success.txt:")
with open(success_file_path, "r") as succes_file:
    print(f"{succes_file.read()}""\n")

print("continut errors.txt:")
with open(errors_file_path, "r") as errors_file:
    print(f"{errors_file.read()}""\n")

