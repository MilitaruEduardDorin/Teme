#!/bin/bash
#! /bin/bash

## Scrieți un script care verifica dacă un site este available (status code între 200 si 399). Scriptul verifică de un număr maxim de ori primit tot ca argument.

verificari_maxime=$1

nr_incercari=1

	
if [ -z "$verificari_maxime" ];then

	while true; do
		echo "Utilizare: $0 <integer>"
                echo -e "Pentru a renunța introdu \"cancel\"\nTrebuie să introduci un număr de verificări maxime:"
                read verificari_maxime

		if [ "$verificari_maxime" = 'cancel' ] ; then
		        echo "Verificarea NU va continua "
       			 exit 1
		fi


		if [[ ! "$verificari_maxime" =~ ^-?[0-9]+$ ]]; then
			echo "Nu ai introdus un numar intreg"
			continue
		else
			if [ "$verificari_maxime" -lt 1 ]; then
				echo "Numarul trebuie sa fie mai mare ca 0"
				continue

			else
				echo "Incep verificarea site-ului https://example.com"
				break

			fi
		fi
	done
fi

### Dorin: Am vrut sa introduc si o verificare pt site daca ar fi fost primit ca si parametru, dar m-am dat batut cand ma gandeam la cate combinatii trebuia sa verific.
### Dorin: ca si dovada:
### eu@DevOps-ITSchool:~/ITSchool/Tema_Bash_Scripting$ curl -o /dev/null -s -w "%{http_code}\n" https://example.cm -> 302


while [ "$nr_incercari" -le "$verificari_maxime " ];do

	echo "Verificarea numarul " $nr_incercari

	status_site=$(curl -o /dev/null -s -w "%{http_code}\n" https://example.chior) ### Dorin: pt a testa ambele variante am inlocui .com cu .chior

	if [ "$status_site" -ge 200 ] && [ "$status_site" -lt 400 ]; then
		echo "Site-ul https://example.com este disponibil"
		break
	else
		echo "Site-ul https://example.com NU  este disponibil"
	fi

	((nr_incercari++))

	sleep 5

done

echo "Verificarea s-a incheiat"

### Dorin: Am vazut dupa ca exercitiul avea rezolvarea in PDF-ul de Shell Scripting. Am interpretat prost si cerinta, pana acum intelegeam ca singurul argument obligatoriu era nr de incercari maxime, nu si site-ul
