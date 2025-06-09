#Crie uma função que receba uma lista e retorne a média dos elementos.
def media_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

if __name__ == "__main__":
    lista = [10, 20, 30, 40, 50]
    resultado = media_lista(lista)
    print(f"A média dos elementos da lista {lista} é: {resultado}")
    
    lista_vazia = []
    resultado_vazio = media_lista(lista_vazia)
    print(f"A média dos elementos da lista vazia é: {resultado_vazio}")