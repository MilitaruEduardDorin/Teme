# 1. Defineste cate o variabila din fiecare tip invatat: 

string = "Sir caractere"
number = 314
boolean = True
none = None
list = [1,3,"text", 10, "alt text"]
set = {"piulita","saiba", "surub"}
Dictionary = {
    'nume': "Popescu",
    'prenume': 'Ion',
    'nota': '8.34'
}
Tuple  = ('unu', 3, 'noua', 4.56)

# 2. Pentru fiecare variabila afișați valoarea și tipul ei folosind metoda print 
print("Variabila de timpul: ", type(string).__name__)
print("Variabila de timpul: ", type(number).__name__)
print("Variabila de timpul: ", type(boolean).__name__)
print("Variabila de timpul: ", type(none).__name__)
print("Variabila de timpul: ", type(list).__name__)
print("Variabila de timpul: ", type(set).__name__)
print("Variabila de timpul: ", type(Dictionary).__name__)
print("Variabila de timpul: ", type(Tuple).__name__)
print(list)

# 3. Creați o alta variabila cu numele documentație de tip string pe mai multe linii in care sa puneti pentru fiecare variabila ceva de genul: 

Documentatie = f"""
Variabila string este de tipul {type(string).__name__} si are valoarea {string}
Variabila number este de tipul {type(number).__name__} si are valoarea {number}
Variabila boolean este de tipul {type(boolean).__name__} si are valoarea {boolean}
Variabila none este de tipul {type(none).__name__} si are valoarea {none}
Variabila list este de tipul {type(list).__name__} si are valoarea {list}
Variabila set este de tipul {type(set).__name__} si are valoarea {set}  /# de ce se schimba ordinea la fiecare rulare
Variabila Dictionary este de tipul {type(Dictionary).__name__} si are valoarea {Dictionary}
Variabila Tuple este de tipul {type(Tuple).__name__} si are valoarea {Tuple}
"""

# 4.Afisati si acest string documentatie in consola. 

print (f"{Documentatie}")