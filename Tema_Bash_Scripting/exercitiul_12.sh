#!/bin/bash

###Dorin: initial nu am adaugat shebang-ul in fisier ca sa testez chiar pe el insusi. Dupa mine nu ar trebui sa functioneze pt ca scriptul teoretic se sterge pana sa se termine de executat ( comanda mv ). ceea ce se demonstreaza si prin faptul ca permisiunile se modifica de la 777, cum erau initial

###Dorin : E cumva de la faptul ca fisierul in sine e "intr-un proces de shell", si ce se ruleaza din el este in "alt proces de shell" care face load din fisier pana sa inceapa executia si ca urmare nu il mai intereseaza fisierul in sine?

##Adauga automat hasbang in fisierele de sh in care nu este prezent. 
##Scriptul verifica toate scripturile sh dintr-un director primit ca parametru.

Dir=$1

if [ -z "$Dir" ] || [ ! -d "$Dir" ] ;then
	echo " Utilizare: $0 <director>"
	echo " In loc sa fac exit din script voi folosi directorul $0"
	Dir=$(dirname "$0")
else
	echo " Scriptul va adauga #!/bin/bash in toate scripturile de shell  di directorul "$Dir", unde #!/bin/bash nu e setat deja"
fi
	
for script in "$Dir"/*.sh;do
	if [ -f "$script" ];then
		shebang=$(head -n 1 "$script")

		if [ "$shebang" != "#!/bin/bash" ];then
			{ echo "#!/bin/bash"; cat "$script"; } >"$script.tmp"
			mv "$script.tmp" "$script"
			chmod +x "$script"
		fi
	fi
done

