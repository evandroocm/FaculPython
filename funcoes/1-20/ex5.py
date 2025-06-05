#Escreva uma função que receba uma lista de números e retorne o maior elemento.
numeros = [10, 5, 6, 8, 9, 12, 15, 3, 7, 4]

def maior_elemento(lista):
    if not lista: 
        return None
    maior = lista[0] 
    for num in lista:
        if num > maior:
            maior = num
    return maior

print("O maior elemento da lista é:", maior_elemento(numeros))