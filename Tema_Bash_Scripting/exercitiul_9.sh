#!/bin/bash
#! /bin/bash

##Faceți un script ce dă restart la serviciul de sshd dacă este oprit. Puneți scriptul in crontab sa ruleze la fiecare minut. 

#if [ "$EUID" -ne 0 ];then
#	echo "Scriptul trebuie rulat cu sudo"
#	exit 1
#fi

###Dorin: Am inteles initial ca crontab poate fi rulat doar de sudo, si de aceea am folosit verificarea. Macar poate retin $EUID :))

cron_job="* * * * * exercitiul_9_watchdog.sh"

(crontab -l 2>/dev/null | grep -Fv "$cron_job"; echo "$cron_job")| crontab -

if [ $? -eq 0 ] ;then
	echo "Cron job adaugat cu succes"
else
	echo "Cron job-ul NU a putut fi adaugat"
fi
