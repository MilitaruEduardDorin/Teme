#!/bin/bash
#! /bin/bash

## Faceti un script cu numele config.sh ce face load în variabilele de mediu la variabilele definite intr-un fisier config.txt

###Dorin: Rezolvarea era deja in PDF-ul de Shell Scripting. Am citit-o si am icercat sa o refac aici.

##Cum facem ca variabilele setate automat în script să fie disponibile și în sesiunea de shell curentă?

if (return 0 &>/dev/null); then
	echo "Scriptul e rulat cu 'source'"
else
	echo "Scriptul TREBUIE rulat cu 'source'"
	exit 1
fi

###Dorin : If-ul de mai jos e doar pt teste, sa nu mai fac unset cat testez scriptul

if (printenv DB_PORT &>/dev/null) || (printenv DB_USER &>/dev/null) ; then
	echo "Voi elimina 3 variabile de mediu setate anterior pt a testa scriptul "
	unset DB_PORT
	unset DB_USER
	unset DB_FORTAM_EROARE
fi


###Dorin: Initial ma gandisem la un script de laucher care sa ruleze . ./config.sh. Varianta cu return am descoperit-o prin ChatGPT

while read line; do ###Dorin: Am incercat initial cu cat config.txt | while... dar nu merge pt ca while-ul e considerat subshell al cat-ului, si presupun ca variabile ar fi fost exportate in cat

	key=$(echo "$line" | cut -d ":" -f1)
	value=$(echo "$line" | cut -d ":" -f2)

	if [ -z "$key" ] || [ -z "$value" ]; then
		echo "Linia $line NU se poate seta ca si variabila de mediu"

##Cum facem să le setam doar dacă nu sunt deja setate?
	else
		if (printenv "$key" &>/dev/null);then
			echo "Variabila $key este deja setata"
			continue
		else
			echo "Linia $line va fi setata ca variabila de mediu"
			export "$key=$value" 
##Cum facem ca variabilele să fie disponibile de fiecare dată când deschidem un terminal nou al userului curent?
			echo "export "$key=$value"" >> ~/.bashrc
		
		
### Dorin: variabilele trebuie tinute in quote-uri pt a fi parsate ca argument intreg catre export. Spatiile sau caracterele speciale pot duce la erori

			if  printenv | grep "$key" &> /dev/null ; then
				echo "A fost setata variabila $key"
			else
				echo "NU a fost setata variabila $key"
			
			fi
	

		fi
	fi
done < config.txt
