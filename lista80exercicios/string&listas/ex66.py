#Crie uma lista de palavras e utilize .replace() para trocar uma letra específica em cada palavra.
words = ["smile", "keep", "moving", "tree"]

wordsReplace = [word.replace("e", "a") for word in words]

print(wordsReplace)