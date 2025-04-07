#Crie uma lista e utilize max() para encontrar o segundo maior valor.
lista = [23,52,34,654,234,76,26,7]

maior = max(lista)
lista.remove(maior)
segundoMaior = max(lista)

print(segundoMaior)