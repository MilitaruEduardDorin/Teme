#!/bin/bash
#! /bin/bash

##Faceti un script de shell cu numele group-copy.sh ce copiaza userii dintr-un grup in altul.
##Scriptul primește 2 parametrii obligatorii și diferiți: grupul sursa și grupul destinatie (in ordinea aceasta)

if [ !  $# -eq 2 ] || [ $1 = $2 ];then
	echo "Scriptul ruleza cu exact doua nume de grupuri diferite. Utilizare; $0 <grup_sursa> <grup_destinatie>"
	exit 1
fi

existenta_grup_destinatie="$(cat /etc/group | grep -e "$2:" | awk -F':' '{print $1}')"
existenta_grup_sursa="$(cat /etc/group | grep -e "$1:" | awk -F':' '{print $1}')"

if [ -z "$existenta_grup_destinatie" ];then
        echo "Grupul destinatie nu exista. Nu se va efectua transferul"
        exit 2
fi

if [ -z "$existenta_grup_sursa" ];then
        echo "Grupul sursa nu exista. Nu se va efectua transferul"
        exit 3
fi



read -ra transfer <<< "$(cat /etc/group | grep -e "$1:" | awk -F':' '{print $4}' | tr ',' ' ')"

if [ "${#transfer[@]}" -eq 0 ];then
	echo "Grupul sursa nu are useri. Nu se va efectua transferul"
	exit 4
fi

for user in "${transfer[@]}";do
	if id "$user" &> /dev/null;then
		if id -nG "$user" | grep -qw $2;then
			echo "Userul "$user" exista deja in grupul $2"
		else
			sudo usermod -aG $2 "$user"
			users_adaugati+=("$user")
		fi
	
	else
		echo "Userul "$user" nu exista"
	fi
done

if [ "${#users_adaugati[*]}" -gt 0 ];then
	echo "${users_adaugati[@]} -> au fost adaugati in grupul $2"
fi


