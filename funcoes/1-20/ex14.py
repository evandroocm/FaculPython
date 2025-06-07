#Crie uma função que receba uma lista e retorne a média dos elementos.
def media_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)