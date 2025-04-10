#Crie uma lista e remova os espaços em branco dos elementos.
lista = [" copo ", " copo2 ", " copo3 ", " waffles com carne "]

semEspaco = [esp.strip(" ") for esp in lista]

print(semEspaco)