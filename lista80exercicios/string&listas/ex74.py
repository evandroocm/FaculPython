#Crie uma lista de palavras e remova todas que tenham mais de 6 letras.
words = ["smileeee", "keep", "moving", "treeeeeee", "oau", "omg", "no"]

wordsMaisDeSeis = [word for word in words if len(word) < 6]

print("Palavras com menos de 6 letras:", wordsMaisDeSeis)