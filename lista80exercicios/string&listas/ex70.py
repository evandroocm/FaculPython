#Crie uma lista de palavras e encontre a mais curta com min(lista, key=len).
words = ["smile", "keep", "moving", "tree"]

curta = min(words, key=len)

print(curta)