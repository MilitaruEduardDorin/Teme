#!/bin/bash
#! /bin/bash

##Faceți un script ce așteaptă (la nesfarsit) după un fisier pe disk sa fie creat (ce fișier doriti). După ce fișierul a fost create scriptul afișează un mesaj și iese cu succes.

waiting_for=$(ls | grep -w fisier_pt_exercitiul_1.sh) #Fisier de verificat

# while true; do
# 	if [ -f "$waiting_for" ]; then
# 		echo "Fisierul $waiting_for exista "
# 		break
# 	else
# 		waiting_for=$(ls | grep -w fisier_pt_exercitiul_1.sh)
# 		echo "Inca nu exista fisierul cautat. Rulez pana cand acesta va fi creat"
# 		sleep 5
# 		continue
# 	fi
# done

# echo "Rularea in bucla s-a incheiat dupa gasirea fisierului"


##Bonus (dificultate medie): Modificați scriptul să nu aștepte la nesfarsit ci maxim 1 minut. Dar daca fisierul este create mai devreme de 1 minut scriptul trebuie sa se termine mai devreme.

Cronometru=0

while [ "$Cronometru" -le 60  ] ; do

	 if [ "$Cronometru " -eq 60 ]; then
               echo "Fisierul nu exista nici dupa 1 minute de asteptare. Voi inchide rularea"
               break
	 fi
	
       	if [ -f "$waiting_for" ]; then
               echo "Fisierul $waiting_for exista "
               break
       else
               waiting_for=$(ls | grep -w fisier_pt_exercitiul_1.sh)
               echo "Inca nu exista fisierul cautat. Rulez pana cand acesta va fi creat, sau pana trec 60 de secunde"
               sleep 1
	       ((Cronometru ++))
	       echo "Au trecut $Cronometru secunde"
               continue
       fi

done


### Dorin:  Nu am vrut sa creez doua fisiere separate. Le-am rulat comentand cand o cerinta cand pe cealalta
