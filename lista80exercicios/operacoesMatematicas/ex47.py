#Crie uma lista e utilize min() para encontrar o segundo menor valor.
lista = [23,52,34,654,234,76,26,7]

menor = min(lista)
lista.remove(menor)
segundoMenor = min(lista)

print("O segundo maior valor é:", segundoMenor)