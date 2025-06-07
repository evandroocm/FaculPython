#Escreva uma função que conte quantas vogais há em uma string.
def vogais(texto):
    vogais = 'AEIOU'
    contador = 0
    for n in texto.upper():
        if n in vogais:
            contador += 1
    return contador

texto = input('Digite um texto: ')
print(f'O texto possui {vogais(texto)} vogais.')