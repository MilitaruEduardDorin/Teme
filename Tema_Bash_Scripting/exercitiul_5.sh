#!/bin/bash
#! /bin/bash

##Creați un script ce face backup la un fișier primit ca parametru printr-o variabila de mediu cu numele  BACKUP_FILE_PATH, doar dacă fișierul a fost modificat. Cerințe:

	##a.Toate backupurile sunt ținute într-un subdirector. Numele subdirectorului de backup este și el primit tot ca variabila de mediu (și are valoare implicită backup în caz că nu a fost setată).
	##b.Fiecare fișier de backup are un timestamp în nume.  
	##c.Dacă variabilă de mediu BACKUP_FILE_PATH nu a fost setată se afișează o eroare.
	##d.Dacă există deja un fișier de backup cu același conținut doar îl redenumim cu timestamp-ul curent  (nu mai facem încă un backup). 

BACKUP_FILE_PATH=${BACKUP_FILE_PATH}
BACKUP_DIRECTORY=${BACKUP_dir:-"./backup"}
TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")

if [ -z "$BACKUP_FILE_PATH" ];then
	echo 'ERR: $BACKUP_FILE_PATH nu e setata'
	exit 1
else
	if [ ! -f "$BACKUP_FILE_PATH" ]; then
		echo 'ERR $BACKUP_FILE_PATH nu este fisier'
		exit 2
	fi
fi

mkdir -p "$BACKUP_DIRECTORY"

OG_HASH=$(sha256sum "$BACKUP_FILE_PATH" | awk '{print $1}')
BACKUP_FILE="$BACKUP_DIRECTORY/$(basename "$BACKUP_FILE_PATH")_$TIMESTAMP" 

for EXISTINGS_BACKUPS in "$BACKUP_DIRECTORY"/*;do
	if [ -f "$EXISTINGS_BACKUPS" ]; then
		BKUS_HASH=$(sha256sum "$EXISTINGS_BACKUPS" | awk '{print $1}')

		if [ "$BKUS_HASH" == "$OG_HASH" ];then
			mv "$EXISTINGS_BACKUPS" "$BACKUP_FILE"
			echo "Backup exitent redenumit ca si: $BACKUP_FILE"
			exit 0
		fi
	fi
done

cp "$BACKUP_FILE_PATH" "$BACKUP_FILE" 
echo "Backup creat: $BACKUP_FILE"

###Dorin: Si pe asta l-am facut cu rezolvarea in fata. Dar am inteles logica. Fara rezolvare nu ma prindeam cum trebuia facut


