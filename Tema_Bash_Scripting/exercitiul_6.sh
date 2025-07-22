#!/bin/bash
#! /bin/bash

##Faceți un script ce face backup la fiecare 5 secunde la un director (doar la fisierele ce s-au modificat din acel director). 
##Scriptul primește ca argument numele directorului la care trebuie făcut backup.
##Frecvența la care se face backup este citită dintr-o variabila de mediu cu numele FRECVENTA_BACKUP (cu valoare implicită de 5 secunde).

if [ -z "$FRECVENTA_BACKUP"  ];then
	echo "Frecventa de backup va fi setata la 5 secunde"
fi

FRECVENTA_BACKUP=${FRECVENTA_BACKUP:-"5"}
DIR_FOR_BACKUP=$1
BACKUP_DIR="$(dirname "$DIR_FOR_BACKUP")/got_your_back"


if [ ! -d "$DIR_FOR_BACKUP" ];then
	echo "Argumentul introdus nu este un director"
	exit 1
fi

mkdir -p "$BACKUP_DIR"

while true;do

	for OG_FILE in "$DIR_FOR_BACKUP"/*.txt; do ### Dorin: pentru usurinta testarii am vrut sa ma limitez doar la un singur fisier
		if [ -f "$OG_FILE" ];then
			OG_HASH=$(sha256sum "$OG_FILE" | awk '{print $1}')
			
			FILE_NAME=$(basename "$OG_FILE")
		        BACKED_FILE="$BACKUP_DIR/$FILE_NAME"


			if [ -f "$BACKED_FILE" ];then
				BACKED_HASH=$(sha256sum "$BACKED_FILE" | awk '{print $1}')
				if [ "$OG_HASH" != "$BACKED_HASH" ]; then
						cp "$OG_FILE" "$BACKED_FILE"
				fi
			else
				cp "$OG_FILE" "$BACKED_FILE"
			fi
		fi
	done
 
		
	
	sleep "$FRECVENTA_BACKUP"
done	




