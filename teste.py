f = open("file.txt", "r")
print(f.read())
f.close()

z = open("file.txt", "a")
z.write("adicionando conteudo")
z = open("file.txt", "r")
print(z.read())
z.close()

f = open("file.txt", "w") #escrever

f = open("file.txt", "x") #cria o arquivo especificado