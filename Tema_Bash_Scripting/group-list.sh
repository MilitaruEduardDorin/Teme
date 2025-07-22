#!/bin/bash
#! /bin/bash

##Faceți un script de shell numit group-list.sh ce imi afiseaza toți userii ce se afla într-un grup separati prin spațiu. 
##Scriptul primește ca argument obligatoriu numele grupului. 
##Dacă nu este niciun user în grup nu afișează nimic.

if [ -z $1 ];then
	echo "Trebuie sa oferi ca argument numele grupului"
	exit 1
fi

nume_grup=$1

membri=$(cat /etc/group | grep -e "$nume_grup:" |awk -F ':' '{print $4}' | tr ',' ' ')

if [ -n "$membri" ];then
       echo "In grup sunt: " $membri
fi       

