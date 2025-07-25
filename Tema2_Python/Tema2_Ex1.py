# Faceți un script de python ce genereaza un log fake. 
# Cerinte: 
# fiecare linie de log contine:
    

    # data și ora la care s-a printat mesajul și nivelul de logging
# Folosiți cateva comenzi de shell sa explorati log-ul generat.
    
import logging
import random
import uuid
from datetime import datetime
import argparse

# Log to file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# fiecare linie este scrisă cu un level de logging random (INFO, WARNING, sau ERROR);
levels =[logging.INFO, logging.WARNING, logging.ERROR]

# un mesaj random dintr-o lista de mesaje predefinite de voi
Mesaje_random = [
    "User authenticated successfully.",
    "Database connection failed.",
    "Fetching data from API.",
    "Timeout while waiting for response.",
    "User session expired.",
    "File uploaded successfully.",
    "Permission denied for resource.",
    "Service restarted automatically.",
    "Invalid input received.",
    "Configuration loaded from environment."
]

# un request id random dintr-o lista fixa de 10 request id-uri generata la începutul scriptului (fiecare request id este un UUID)
request_id = [str(uuid.uuid4()) for _ in range(10)]

# scriptul primește ca argument cate linii de log să genereze; 
parser = argparse.ArgumentParser(description='Genereaza un log fake')
parser.add_argument('--nr_linii', type=int, help='Numar de linii din log')
args=parser.parse_args()

for i in range(args.nr_linii):
    level = random.choice(levels)
    mesaj = random.choice(Mesaje_random)
    req_uuid = random.choice(request_id)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"{timestamp} - {logging.getLevelName(level)} - [UUID : {req_uuid}] - {mesaj} "

    if level == logging.INFO:
        logging.info(log_line)
    elif level == logging.WARNING:
        logging.warning(log_line)
    elif level == logging.ERROR:
        logging.error(log_line)