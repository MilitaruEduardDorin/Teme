#!/bin/bash
#! /bin/bash

##Adaugati in variabila de mediu PATH directorul cu calea ~/bin-itschools/ doar dacă acesta exista.
##Faceți acest lucru în mod automat de fiecare data cand se porneste o sesiune cu login pentru userul curent.
##Adaugati un script în acel director și încercați să-l executați de oriunde.

###Dorin: initial am bagat cerinta in ChatGPT. Dar eu zic ca l-am folosit doar  pentru pointers. ":$PATH:" pe asta nu am inteles-o din ce a zis ChatGPT. Poti sa o explici?

Dir="$HOME/bin-itschools/"

echo $PATH | grep -qE "(^|:)$HOME/bin-itschools/(:|$)"

in_PATH=$?
	
if [ ! -d "$Dir" ];then
	echo "Directorul $HOME/bin-itschools/ nu exista"
	read -p "Doriti sa fie creat, si sa contina si un script de test? Da/Nu:" creat 

	if [ "$creat" == "Da" ];then
		mkdir $Dir
		echo "echo "Hello.Eu sunt scriptul de test pentru exercitiul 10!"" > $Dir/hello_test_ex10.sh
		chmod u+x $Dir/hello_test_ex10.sh
	fi

fi
	
if  [ -d "$Dir" ] && [ "$in_PATH" -ne 0 ];then
	echo "export PATH=$PATH:$Dir" >> $HOME/.bashrc
	source $HOME/.bashrc
elif [ "$in_PATH" -eq 0 ];then
	echo "Directorul $HOME/bin-itschools/ exista in variabila PATH"
fi

if [ $creat != "Da" ];then
	echo "Directul $HOME/bin-itschools/ nu exista, nu a fost creat, si nu a fost adaugat in variabila PATH"
fi


