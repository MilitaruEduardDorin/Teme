#!/bin/bash
#! /bin/bash

##Faceți un script ce dă restart la serviciul de sshd dacă este oprit. Puneți scriptul in crontab sa ruleze la fiecare minut. 

if ! systemctl is-active --quiet sshd ;then
	sudo systemctl start sshd &>> exercitiu_9.log
fi

