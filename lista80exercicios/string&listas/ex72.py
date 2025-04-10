#Crie uma lista de frases e extraia a primeira palavra de cada frase.
phrases = [
    "nirvana é vida",
    "tears fors fears é vida",
    "musica é vida"
]

primeiraPalavras = [phrase.split()[0] for phrase in phrases]

print("Listas de palavras:", primeiraPalavras)