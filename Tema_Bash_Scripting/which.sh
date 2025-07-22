#!/bin/bash
#! /bin/bash

##Faceti un script cu numele which.sh ce:
	##Parseaza variabila PATH și pune într-un array toate căile.
	##Itereaza cu un for pe acest array de cai și pentru fiecare cale:
	##cauta dacă acea cale contine un fisier executabil cu numele primit ca argument la script (de exemplu ./which.sh ls)
	##afișează toate căile ce conțin acel executabil.
	##Dacă nu a găsit nicio cale ce contine acel executabil afișați în mesaj de eroare și terminati scriptul cu un cod de eroare.

if [ $# -ne 1 ]; then
	echo "Utilizare: $0 <fisier_executabil>"
	exit 1
fi

fisier_executabil=$1
gasit=0

IFS=':' read -ra array_PATH <<< "$PATH"

for executabil in "${array_PATH[@]}"; do

	if [ -x "$executabil/$fisier_executabil" ]; then
		echo "$executabil/$fisier_executabil"
		gasit=1
	fi
done

if [ "$gasit" -eq 0 ]; then
	echo "Executabilul mentionat NU e in PATH"
	exit 2
fi
