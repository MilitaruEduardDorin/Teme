#!/bin/bash
#! /bin/bash

##Faceți un script ce compara dacă 2 fișiere (primite ca argument) sunt identice ca si continut. (sha256sum).

first_file=$1
second_file=$2

if [ ! $# -eq 2 ]; then
	echo -e "Scriptul ruleaza cu exact doua fisiere distincte primite ca argument.\nUtilizare: $0 fisier1 fisier2"
	read -p "Primul fisier:" first_file
	read -p "Al doilea fisier:" second_file
fi

if [ ! -f "$first_file" ] || [ ! -f "$second_file" ]; then
	echo "Cel putin unul din argumente nu este un fisier"
	exit 1
fi
cale_first_file=$(pwd $first_file)
echo "$cale_first_file"
cale_second_file=$(pwd $second_file)
echo "$cale_second_file"

### Dorin: echo "~/ITSchool/Tema_Bash_Scripting/exercitiul_1.sh" | awk -F'/' '{for(i=1;i<NF;i++) printf "%s/", $i; print ""}' O ora m-am chinuit la asta pana sa imi dau seama ca pwd era cea mai la indemana :))

#echo $cale_first_file
#echo $cale_second_file

if [ "$cale_first_file" = "$cale_second_file" ] && [ "$first_file" = "$second_file" ] ;then
	echo "Scriptul are nevoie de doua fisiere distincte"
	exit 2
else
	echo "O sa compar fisierele"

fi

sha_first_file=$(sha256sum $first_file| awk '{print $1}') 
sha_second_file=$(sha256sum $second_file| awk '{print $1}')

### Dorin: [[$(sha256sum $first_file| awk '{print $1}') == $(sha256sum $second_file| awk '{print $1}')]] Cum puteam sa utilizez asta ca si conditie a IF-ului ?


if [ "$sha_first_file" = "$sha_second_file" ];then
	echo $sha_first_file
	echo $sha_second_file
	echo "Cele doua fisiere au continut identic"
else
        echo $sha_first_file
        echo $sha_second_file
	echo "Cele doua fisiere NU au continut identic"
fi


##Bonus (dificultate ridicata): În loc de 2 fișiere comparati o lista de oricât de multe fișiere. Dacă oricare 2 fișiere din lista sunt diferite intoarce-ti un mesaj de eroare.  



