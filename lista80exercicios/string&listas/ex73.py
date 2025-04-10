#Crie uma lista de palavras e remova todas que tenham menos de 4 letras.
words = ["smile", "keep", "moving", "tree", "oau", "omg", "no"]

wordsQuatro = [word for word in words if len(word) >= 4]

print("Palavras com 4 letras ou mais:", wordsQuatro)