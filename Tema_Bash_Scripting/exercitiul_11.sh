#!/bin/bash
#! /bin/bash

##Log rotation: Faceți un script ce face log rotation la un fisier de loguri primit ca argument. 
##Pentru simplitate log rotation-ul se face automat la un numar de secunde primit ca argument. 
##Cand se face log rotation se copiază fișierul curent într-un nou fișier cu același nume ca fișierul original + un timestamp iar fișierul original se golește. 
##Fisierele de log rotation se și arhivează pentru a ocupa mai puțin spațiu.
##Faceți un script simplu ce printeaza la nesfarsit in loguri pentru a testa scriptul de log rotation (vedeti hello.sh de la curs). 

if [ $# -ne 2 ];then
	echo "Utilizare: $0 <fisier_loguri> <interval_log_rotation>"
	exit 1
fi

Fisier_loguri=$1
interval_rotation=$2

if [ ! -f "$Fisier_loguri" ];then
	echo " $Fisier_loguri nu este fisier"
	exit 2
fi

if [  "$interval_rotation" -le 0 ];then
	echo "Intervalul de log rotation trebuie sa fie > 0"
	exit 3
fi

while true; do
	sleep "$interval_rotation"

	TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")
	BACKUP_FILE="$Fisier_loguri_$TIMESTAMP"

###Dorin : cele doua variabile de mai sus sunt copiate din exercitiul 5

	cp "$Fisier_loguri" "$BACKUP_FILE"
	echo "" > "$Fisier_loguri"

	gzip "$BACKUP_FILE"
done
	
