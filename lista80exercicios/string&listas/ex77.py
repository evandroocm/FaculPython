#Crie uma lista e rotacione seus elementos uma posição à esquerda.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listaRotacionada = lista[1:] + [lista[0]]

print(f"Lista rotacionada: {listaRotacionada}")