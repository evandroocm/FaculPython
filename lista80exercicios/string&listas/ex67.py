#Crie uma lista de frases e utilize .split() para transformar cada frase em lista de palavras.
phrases = [
    "nirvana é vida",
    "tears fors fears é vida",
    "musica é vida"
]

listasPalavras = [phrase.split() for phrase in phrases]

print("Listas de palavras:", listasPalavras)